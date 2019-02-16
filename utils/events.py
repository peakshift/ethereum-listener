import time
import decimal
from web3 import Web3
import utils.database as storage


db = storage.Database()
current_price = 277.00


def handle_event(w3, event, address):
    """
    This function searches for transactions to
    the given address and sends the transaction
    to be stored inside of a database.

    param:
    w3(object): ethereum node connection
    event(string): latest block hash
    address(string): ethereum address

    """
    block = w3.eth.getBlock(w3.toHex(event), True)

    for txn in block['transactions']:
        if txn['to'] == address:
            response = store(txn)
            if response is True:
                print(f"Incoming Transaction for address: {address} was recorded.")
            else:
                print(f"Transaction for address: {address} was not inserted.")
                print(f"Please manually insert: {txn} \n")
        else:
            continue


def log_loop(event_filter, poll_interval, address, w3):
    """
    This functions starts the event listener and watches
    new blocks.

    param:
    event_filter(object): block filter object
    poll_interval(int): time check interval
    address(string): ethereum address
    w3(object): etehreum node connection
    """
    while True:
        for event in event_filter.get_new_entries():
            handle_event(w3, event, address)
        time.sleep(poll_interval)


def store(txn) -> bool:
    """
    This function stores relevant
    details of a transaction inside
    the Transaction database

    param:
    txn(object): transaction block

    return:
    response(bool): database insert response
    """
    data = {
        "to": txn["to"],
        "gas": txn["gas"],
        "from": txn["from"],
        "value": txn["value"],
        "gas_price": txn["gasPrice"],
        "block_number": txn["blockNumber"]
    }

    data["usd"] = calculate(data["value"], current_price)
    response = db.insert('Transactions', data)

    return response


def calculate(value, current_price) -> float:
    """
    This function calculates the
    USD equivalent of the transaction
    value and returns it to be stored

    param:
    value(int): transaction value in Wei
    current_price(float): ethereum market price in USD

    return:
    usd(float): USD equivalent
    """
    value_ether = Web3.fromWei(value, 'ether')
    usd = float(decimal.Decimal(value_ether)) * current_price

    return round(usd, 2)
