import time
import utils.database as storage


db = storage.Database()


def handle_event(w3, event, address):
	block = w3.eth.getBlock(w3.toHex(event), True)

	for txn in block['transactions']:
		if txn['to'] == address:
			data = {
				"to": txn["to"],
				"gas": txn["gas"], 
				"from": txn["from"],
				"value": txn["value"],
				"gas_price": txn["gasPrice"], 
				"block_number": txn["blockNumber"]
			}
			response = db.insert('Transactions', data)
			if response is True:
				print("Incoming Transaction for address was recorded.")
			else:
				print("Transaction for address was not inserted.")
		else:
			continue


def log_loop(event_filter, poll_interval, address, w3):
	while True:
		for event in event_filter.get_new_entries():
			handle_event(w3, event, address)
		time.sleep(poll_interval)

