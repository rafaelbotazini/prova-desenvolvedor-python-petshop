
from datetime import datetime
from enum import Enum


class TamanhoCachorro(Enum):
    """Tamanhos de cachorro aceitos pelos petshops"""
    GRANDE = 1,
    PEQUENO = 2

# Classe base para petshops
class PetShop:
    nome: str
    distancia_metros: int
    preco_banho_grande: float
    preco_pequeno: float

    def __init__(self, nome: str, distancia_metros: int, preco_banho_grande: float, preco_banho_pequeno: float) -> None:
        self.nome = nome
        self.distancia_metros = distancia_metros
        self.preco_banho_grande = preco_banho_grande
        self.preco_banho_pequeno = preco_banho_pequeno

    def get_preco_banho(self, tamanho: TamanhoCachorro, _: datetime = None):
        """Obtém o preço de um banho de acordo com o tamanho do cachorro"""
        return self.preco_banho_grande if tamanho == TamanhoCachorro.GRANDE else self.preco_banho_pequeno


class MeuCaninoFeliz(PetShop):
    def __init__(self) -> None:
        super().__init__(nome='Meu Canino Feliz', distancia_metros=2000, preco_banho_grande=40, preco_banho_pequeno=20)

    def get_preco_banho(self, tamanho: TamanhoCachorro, data: datetime):
        preco_base = super().get_preco_banho(tamanho, data)
        return preco_base if eh_dia_de_semana(data) else preco_base * 1.2


class VaiRex(PetShop):
    def __init__(self) -> None:
        super().__init__(nome='Vai Rex', distancia_metros=1700, preco_banho_grande=50, preco_banho_pequeno=15)

    def get_preco_banho(self, tamanho: TamanhoCachorro, data: datetime):
        if eh_dia_de_semana(data):
            return super().get_preco_banho(tamanho, data)
        return 55 if tamanho == TamanhoCachorro.GRANDE else 20


class ChowChawgas(PetShop):
    def __init__(self) -> None:
        super().__init__(nome='Chow Chawgas', distancia_metros=800, preco_banho_grande=45, preco_banho_pequeno=30)


def eh_dia_de_semana(data):
    """Verifica se o dia na data providenciada está entre segunda-feira e sexta-feira"""
    return data and data.weekday() in range(0, 5)
