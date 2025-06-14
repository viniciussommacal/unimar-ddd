from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid
from ..value_objects.email import Email

@dataclass
class Usuario:
    """
    Entity Usuario
    Aplicando DDD: Entidade com identidade e comportamentos
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    nome: str = ""
    email: Email = None
    ativo: bool = True
    data_criacao: datetime = field(default_factory=datetime.utcnow)
    
    def __post_init__(self):
        if not self.nome:
            raise ValueError("Nome é obrigatório")
        if not self.email:
            raise ValueError("Email é obrigatório")
    
    def desativar(self) -> None:
        """
        Comportamento de domínio: desativar usuário
        """
        if not self.ativo:
            raise ValueError("Usuário já está inativo")
        self.ativo = False
    
    def ativar(self) -> None:
        """
        Comportamento de domínio: ativar usuário
        """
        if self.ativo:
            raise ValueError("Usuário já está ativo")
        self.ativo = True
    
    def pode_emprestar(self) -> bool:
        """
        Regra de negócio: usuário pode emprestar livros
        """
        return self.ativo
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Usuario):
            return False
        return self.id == other.id
    
    def __hash__(self) -> int:
        return hash(self.id)