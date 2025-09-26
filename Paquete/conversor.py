def convertir_dolares(valor_dolares, moneda_destino):
    """
    Convierte un valor en dólares a otra moneda.

    Monedas soportadas:
    - EUR: Euros
    - LB: Libras Esterlinas
    - KRW: Won (Surcoreano)
    - BTC: Bitcoin

    Args:
        valor_dolares (float): Valor en dólares a convertir.
        moneda_destino (str): Moneda destino ("EUR", "LB", "KRW", "BTC").

    Returns:
        float: Valor convertido en la moneda destino.

    Raises:
        ValueError: Si la moneda no está soportada.
    """
    tasas = {"EUR": 0.93, "LB": 0.81, "KRW": 1343.50, "BTC": 0.000031}
    moneda_destino = moneda_destino.upper()
    if moneda_destino not in tasas:
        raise ValueError("Moneda no soportada. Use: EUR, LB, KRW, BTC")
    return valor_dolares * tasas[moneda_destino]
