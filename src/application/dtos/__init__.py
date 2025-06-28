# Application Layer - DTOs (Data Transfer Objects)

from dataclasses import dataclass
from typing import Optional


@dataclass
class LivroDTO:
    """
    DTO para transferência de dados de Livro
    Aplicando Clean Architecture: DTOs na camada de aplicação
    """
    titulo: str
    autor: str
    isbn: str
    id: Optional[str] = None
    disponivel: Optional[bool] = True


@dataclass
class UsuarioDTO:
    """
    DTO para transferência de dados de Usuario
    """
    nome: str
    email: str
    id: Optional[str] = None
    creditos: Optional[float] = 0.0
    ativo: Optional[bool] = True


@dataclass
class EmprestimoDTO:
    """
    DTO para transferência de dados de Emprestimo
    """
    livro_id: str
    usuario_id: str
    data_emprestimo: str
    data_devolucao_prevista: str
    id: Optional[str] = None
    data_devolucao_real: Optional[str] = None
    multa: Optional[float] = 0.0
    esta_em_atraso: Optional[bool] = False
    dias_atraso: Optional[int] = 0


@dataclass
class EmprestimoRequestDTO:
    """
    DTO para requisição de empréstimo
    """
    livro_id: str
    usuario_id: str


@dataclass
class DevolucaoRequestDTO:
    """
    DTO para requisição de devolução
    """
    emprestimo_id: str

@dataclass
class DoacaoDTO:
    """
    DTO para requisição de devolução
    """
    id: Optional[str] = None
    livro_id: str
    usuario_id: str
    data_doacao: str
    creditos: Optional[float] = 0.0

