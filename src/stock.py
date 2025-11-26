import json
from pathlib import Path
from uuid import uuid4

DATA = Path(__file__).parent.parent / "data" / "estoque.json"

def load_stock(path=None):
    p = Path(path) if path else DATA
    with open(p, encoding='utf-8') as f:
        return json.load(f)

def save_stock(obj, path=None):
    p = Path(path) if path else DATA
    with open(p, "w", encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def movimentar(codigo_produto, quantidade, descricao, path=None):
    """Cria uma movimentação (entrada se quantidade>0, saída se quantidade<0).
    Retorna dict com id da movimentação e quantidade final do produto.
    """
    obj = load_stock(path)
    for p in obj.get("estoque", []):
        if p.get("codigoProduto") == codigo_produto:
            p["estoque"] = int(p.get("estoque",0)) + int(quantidade)
            movimentacao = {
                "id": str(uuid4()),
                "codigoProduto": codigo_produto,
                "descricao": descricao,
                "quantidade": int(quantidade),
                "data": __import__('datetime').datetime.now().isoformat()
            }
            # You could persist movements in a separate file; for simplicity we only update estoque.json
            save_stock(obj, path)
            return {"movimentacao": movimentacao, "estoqueFinal": p["estoque"]}
    raise ValueError(f"Produto com código {codigo_produto} não encontrado.")
