from config import ADMIN_ID

def copy_trade(trade):
    # MVP: just simulate copy logic
    print(f"Copying trade to admin {ADMIN_ID}: {trade['symbol']} {trade['side']}")
