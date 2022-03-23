import locale
import sys
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

from canil import obter_orcamento_banhos


def main(argv: 'list[str]'):
    args = argv[1:]
    if len(args) < 3:
        raise SystemExit(
            f'Modo de usar: {argv[0]} <data (DD/MM/AAAA)> <quantidade de cães pequenos> <quantidade de cães grandes>')

    data, qt_pequenos, qt_grandes = (
        datetime.strptime(args[0], '%d/%m/%Y'),
        int(args[1]),
        int(args[2])
    )

    petshop, valor = obter_orcamento_banhos(data, qt_pequenos, qt_grandes)
    print(f'O melhor orçamento para o dia {args[0]} é no petshop {petshop.nome} ({petshop.distancia_metros // 1000} km).'
          f'Valor total dos banhos: {locale.currency(valor)}.')


if __name__ == '__main__':
    main(sys.argv)
