from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional
import uuid

@dataclass
class Emprestimo:
    """
    Entity Emprestimo (Aggregate Root)
    Aplicando DDD: Agregado que mantém consistência
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    livro_id: str = ""
    usuario_id: str = ""
    data_emprestimo: datetime = field(default_factory=datetime.utcnow)
    data_devolucao_prevista: datetime = field(default_factory=lambda: datetime.utcnow() + timedelta(days=14))
    data_devolucao_real: Optional[datetime] = None
    multa: float = 0.0
    
    def __post_init__(self):
        if not self.livro_id:
            raise ValueError("ID do livro é obrigatório")
        if not self.usuario_id:
            raise ValueError("ID do usuário é obrigatório")
    
    def devolver(self) -> float:
        """
        Comportamento de domínio: devolver livro e calcular multa
        Aplicando DDD: Lógica de negócio complexa no agregado
        """
        if self.data_devolucao_real:
            raise ValueError("Livro já foi devolvido")
        
        self.data_devolucao_real = datetime.utcnow()
        self.multa = self._calcular_multa()
        return self.multa
    
    def _calcular_multa(self) -> float:
        """
        Regra de negócio: calcular multa por atraso
        R$ 1,00 por dia de atraso
        """
        if not self.data_devolucao_real:
            return 0.0
        
        if self.data_devolucao_real <= self.data_devolucao_prevista:
            return 0.0
        
        dias_atraso = (self.data_devolucao_real - self.data_devolucao_prevista).days
        return dias_atraso * 1.0  # R$ 1,00 por dia
    
    @property
    def esta_em_atraso(self) -> bool:
        """
        Propriedade calculada: verifica se está em atraso
        """
        if self.data_devolucao_real:
            return False  # Já foi devolvido
        return datetime.utcnow() > self.data_devolucao_prevista
    
    @property
    def dias_atraso(self) -> int:
        """
        Propriedade calculada: dias de atraso
        """
        if not self.esta_em_atraso:
            return 0
        return (datetime.utcnow() - self.data_devolucao_prevista).days
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Emprestimo):
            return False
        return self.id == other.id
    
    def __hash__(self) -> int:
        return hash(self.id)