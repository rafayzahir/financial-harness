
def sma(values: list[float], period: int):
    if len(values) < period:
        return None

    return sum(values[-period:]) / period


def ema(values: list[float], period: int):
    if len(values) < period:
        return None

    multiplier = 2 / (period + 1)
    result = sum(values[:period]) / period

    for price in values[period:]:
        result = (price - result) * multiplier + result

    return result


def rsi(values: list[float], period: int = 14):
    if len(values) <= period:
        return None

    changes = [
        values[i] - values[i - 1]
        for i in range(1, len(values))
    ]

    gains = [max(change, 0) for change in changes]
    losses = [max(-change, 0) for change in changes]

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period

    if avg_loss == 0:
        return 100.0

    relative_strength = avg_gain / avg_loss
    return 100 - (100 / (1 + relative_strength))


def macd(values: list[float]):
    if len(values) < 35:
        return None

    multiplier_12 = 2 / 13
    multiplier_26 = 2 / 27

    ema12 = sum(values[:12]) / 12
    ema26 = sum(values[:26]) / 26

    macd_values = []

    for i, price in enumerate(values):
        if i >= 12:
            ema12 = (price - ema12) * multiplier_12 + ema12

        if i >= 26:
            ema26 = (price - ema26) * multiplier_26 + ema26

        if i >= 25:
            macd_values.append(ema12 - ema26)

    if len(macd_values) < 9:
        return None

    signal = ema(macd_values, 9)
    current_macd = macd_values[-1]

    return {
        "macd": current_macd,
        "signal": signal,
        "histogram": current_macd - signal,
    }


def calculate_indicators(candles: dict):
    if candles.get("s") != "ok":
        raise ValueError("Invalid candle data")

    closes = candles.get("c", [])

    if not closes:
        raise ValueError("No closing prices available")

    return {
        "sma_20": sma(closes, 20),
        "sma_50": sma(closes, 50),
        "ema_12": ema(closes, 12),
        "ema_26": ema(closes, 26),
        "rsi_14": rsi(closes, 14),
        "macd": macd(closes),
    }
