# Domain Layer - Value Objects

from dataclasses import dataclass


@dataclass(frozen=True)
class Comentario:
    """
    Value Object: Valor
    Representa o comentário de uma avaliação.
    Aplicando DDD: Value Object imutável com validação.
    """
    valor: str

    def __post_init__(self):
        if len(self.valor.strip()) < 10:
            raise ValueError("Comentário muito curto. Deve ter no mínimo 10 caracteres.")
        if len(self.valor) > 500:
            raise ValueError("Comentário muito longo. Deve ter no máximo 500 caracteres.")

    def __str__(self):
        return self.valor
