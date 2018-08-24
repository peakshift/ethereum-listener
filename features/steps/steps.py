import json
from web3 import Web3
from behave import * 
from utils.events import *
import utils.database as storage


db = storage.Database()


# Database scenario
@given(u'inputdata is')
def step_impl(context):
	context.data = json.loads(context.text)


@when(u'the insert("{collection}", inputdata) method is invoked')
def step_impl(context, collection):
	context.response = db.insert(collection, context.data)


@then(u'the new document is inserted')
def step_impl(context):
	assert context.response is True


# Calculation scenario
@given(u'the current price of ETH is "{price}"$ on coinmarketcap')
def step_impl(context, price):
	context.price = float(price)

@when(u'a new transaction is detected')
def step_impl(context):
	context.data = json.loads(context.text)

@when(u'the transaction value is "{value}" ETH')
def step_impl(context, value):
	# transaction value is returned in Wei
	context.value = Web3.toWei(value,'ether')


@then(u'the current USD price * transaction value is calculated')
def step_impl(context):
	context.response = calculate(context.value, context.price)

@then(u'added to the database along with the transaction')
def step_impl(context):
	context.data["usd"] = context.response
	assert (db.insert("Transactions",context.data)) is True