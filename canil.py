from datetime import datetime
from petshop import ChowChawgas, MeuCaninoFeliz, PetShop, TamanhoCachorro, VaiRex

# As diferentes instâncias dep petshops podem ser construídas por uma fábrica de objetos que utiliza, por exemplo, dados vindo de um banco.
# No nosso caso retornamos um array em memória para fins de simplicidade.
def obter_petshops() -> 'list[PetShop]':
    """Retorna os petshops cadastrados no sistema"""
    return [MeuCaninoFeliz(), VaiRex(), ChowChawgas()]

def obter_orcamento_banhos(data: datetime, qt_pequenos: int, qt_grandes: int) -> 'tuple[PetShop, float]':
    """Retorna uma tupla representando o orçamento, contendo: ([o petshop mais barato mais perto], [o valor cobrado pelo serviço])"""

    petshops = obter_petshops()
    orcamentos = [(petshop, _calcular_valor_banhos(petshop, data, qt_pequenos, qt_grandes)) for petshop in petshops]
    ordenados_por_valor: 'list[tuple[PetShop, float]]' = sorted(orcamentos, key=lambda x: x[1])

    mais_barato = ordenados_por_valor[0]
    orcamentos_restantes = ordenados_por_valor[1:]

    petshop_escolhido, valor_escolhido = mais_barato

    # verificando se existe um petshop mais perto e com o mesmo valor
    for petshop, valor in orcamentos_restantes:
        if valor == valor_escolhido and petshop.distancia_metros < petshop_escolhido.distancia_metros:
            petshop_escolhido = petshop

    return (petshop_escolhido, valor_escolhido)

def _calcular_valor_banhos(petshop: PetShop, data: datetime, quantidate_pequenos: int, quantidade_grandes: int) -> float:
    preco_g = petshop.get_preco_banho(TamanhoCachorro.GRANDE, data)
    preco_p = petshop.get_preco_banho(TamanhoCachorro.PEQUENO, data)
    return (preco_g * quantidade_grandes) + (preco_p * quantidate_pequenos)