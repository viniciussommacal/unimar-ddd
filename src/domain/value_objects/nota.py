# Domain Layer - Value Objects

from dataclasses import dataclass

@dataclass(frozen=True)
class Nota:
    """
    Value Object: Valor
    Representa uma nota de avaliação válida.
    Aplicando DDD: Value Object imutável com validação.
    """
    valor: int

    def __post_init__(self):
        if self.valor < 1 or self.valor > 5:
            raise ValueError(f"Nota deve estar entre 1 e 5: {self.valor}")
    
    def __str__(self):
        return str(self.valor)
