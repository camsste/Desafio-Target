import argparse
from src import commissions, stock, interest
from pathlib import Path

def cmd_commissions(args):
    totals, details = commissions.commissions_by_seller()
    print("Comissões por vendedor (R$):")
    for v,t in totals.items():
        print(f" - {v}: R$ {t:.2f}")

def cmd_movimentar(args):
    try:
        res = stock.movimentar(args.codigo, args.quantidade, args.descricao)
        print("Movimentação realizada:")
        print(f"  id: {res['movimentacao']['id']}")
        print(f"  produto: {res['movimentacao']['codigoProduto']}")
        print(f"  descrição: {res['movimentacao']['descricao']}")
        print(f"  quantidade: {res['movimentacao']['quantidade']}")
        print(f"  estoque final: {res['estoqueFinal']}")
    except Exception as e:
        print("Erro:", e)

def cmd_juros(args):
    dias, juros = interest.juros_simples(args.valor, args.vencimento)
    print(f"Dias de atraso: {dias}")
    print(f"Juros acumulado: R$ {juros:.2f}")

def build_parser():
    p = argparse.ArgumentParser(prog="desafio")
    sub = p.add_subparsers(dest="cmd")
    c1 = sub.add_parser("comissoes", help="Calcula comissões por vendedor a partir de data/vendas.json")
    c1.set_defaults(func=cmd_commissions)

    c2 = sub.add_parser("movimentar", help="Movimenta estoque: --codigo CODE --quantidade N --descricao 'texto'")
    c2.add_argument("--codigo", type=int, required=True)
    c2.add_argument("--quantidade", type=int, required=True)
    c2.add_argument("--descricao", type=str, required=True)
    c2.set_defaults(func=cmd_movimentar)

    c3 = sub.add_parser("juros", help="Calcula juros: --valor 1000 --vencimento YYYY-MM-DD")
    c3.add_argument("--valor", type=float, required=True)
    c3.add_argument("--vencimento", type=str, required=True)
    c3.set_defaults(func=cmd_juros)
    return p

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
