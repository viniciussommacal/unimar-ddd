import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Email:
    """
    Value Object para Email
    Aplicando DDD: Objeto de valor imutável com validação
    """
    value: str
    
    def __post_init__(self):
        if not self._is_valid_email(self.value):
            raise ValueError(f"Email inválido: {self.value}")
    
    def _is_valid_email(self, email: str) -> bool:
        """Valida formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def __str__(self) -> str:
        return self.value