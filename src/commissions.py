import json
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).parent.parent / "data" / "vendas.json"

def calc_commission_for_value(valor):
    if valor < 100:
        return 0.0
    elif valor < 500:
        return valor * 0.01
    else:
        return valor * 0.05

def commissions_by_seller(path=None):
    p = Path(path) if path else DATA
    with open(p, encoding='utf-8') as f:
        data = json.load(f)
    totals = defaultdict(float)
    details = defaultdict(list)
    for venda in data.get("vendas", []):
        vendedor = venda.get("vendedor")
        valor = float(venda.get("valor", 0))
        com = calc_commission_for_value(valor)
        totals[vendedor] += com
        details[vendedor].append({"valor": valor, "comissao": round(com,2)})
    # Round totals
    totals = {k: round(v,2) for k,v in totals.items()}
    return totals, details

if __name__ == "__main__":
    totals, details = commissions_by_seller()
    print("Comissões por vendedor (R$):")
    for v,t in totals.items():
        print(f" - {v}: R$ {t:.2f}")
