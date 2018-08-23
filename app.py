import os
from flask import Flask, jsonify
from web3 import Web3
from utils.events import *


app = Flask(__name__)
url = os.environ['server']  # blockchain server
w3 = Web3(Web3.HTTPProvider(url))


def main():
	address = input("Enter address to search for: ")
	block_filter = w3.eth.filter('latest')
	log_loop(block_filter, 2, address, w3)


if __name__ == '__main__':
	main()
	

