from datetime import datetime, date

def juros_simples(valor, data_vencimento, hoje=None, multa_diaria_percent=2.5):
    """
    Calcula juros simples acumulados desde a data de vencimento até hoje.
    - multa_diaria_percent: percentagem por dia (2.5 significa 2.5% por dia)
    Retorna (dias_atraso, juros_total)
    """
    hoje = hoje or date.today()
    if isinstance(data_vencimento, str):
        # espera formato YYYY-MM-DD
        data_vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d").date()
    dias = (hoje - data_vencimento).days
    if dias <= 0:
        return 0, 0.0
    taxa = multa_diaria_percent/100.0
    juros = valor * taxa * dias
    return dias, round(juros,2)

if __name__ == "__main__":
    # exemplo de uso:
    valor = 1000.0
    venc = "2025-11-01"
    dias, juros = juros_simples(valor, venc)
    print(f"Dias atraso: {dias}; Juros: R$ {juros:.2f}")
