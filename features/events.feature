Feature: Event Listener


Scenario: Calculate and store USD conversion of transaction value
Given the current price of ETH is "277"$ on coinmarketcap
When a new transaction is detected
"""
{
	"block_number": 2, 
	"from": "0x4a78bA434908DDd69F55B804f7A79eB4CB4A3831", 
	"to": "0xaA431B5228c0875747f3076185959f004a9699aC", 
	"value": 1250000000000000000, 
	"gas": 121000, 
	"gas_price": 1
}
"""
And the transaction value is "1.25" ETH
Then the current USD price * transaction value is calculated
And added to the database along with the transaction


Scenario: Insert document into collection
Given inputdata is
"""
{
	"to": "0xaA431B5228c0875747f3076185959f004a9699aC",
	"from": "0x4a78bA434908DDd69F55B804f7A79eB4CB4A3831",
	"gas": 121000,
	"value": 1234567,
	"gas_price": 1,
	"block_number": 5
}
"""
When the insert("Transactions", inputdata) method is invoked
Then the new document is inserted

