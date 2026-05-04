def check_risk(trade):
    if trade["entry"] <= 0:
        return False
    return True
