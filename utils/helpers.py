from datetime import datetime

def format_trade(symbol, side, entry, sl, tp):
    return {
        "symbol": symbol,
        "side": side,
        "entry": float(entry),
        "sl": float(sl),
        "tp": float(tp),
        "timestamp": str(datetime.now())
    }


def validate_trade(data):
    required = ["symbol", "side", "entry", "sl", "tp"]
    for field in required:
        if field not in data:
            return False, f"Missing {field}"
    return True, "OK"
