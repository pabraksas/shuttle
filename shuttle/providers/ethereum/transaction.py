#!/usr/bin/env python3

from web3 import Web3
from web3.providers import HTTPProvider
from binascii import unhexlify, hexlify
from eth_typing import URI

import json

from ..config import ethereum
from .wallet import Wallet
from .htlc import HTLC


# Ethereum configuration
ethereum = ethereum()


class FundTransaction:

    # Initialization fund transaction
    def __init__(self, web3=None, network="testnet"):

        self.htlc = None
        self.construct_txn = None

        # Ethereum network setup.
        if web3 and not isinstance(web3, Web3):
            raise ValueError("invalid web3 instance, only takes Wallet class")
        elif web3 is not None:
            self.web3 = web3
            self._hash = None
            self._contract_address = None
        elif network not in ["mainnet", "testnet"]:
            raise ValueError("invalid network type, please choose only mainnet or testnet.")
        elif network == "mainnet":
            self._hash = ethereum["mainnet"]["infura"]["hash"]["eth"]
            self._contract_address = ethereum["mainnet"]["infura"]["contract_address"]["eth"]
            self.web3 = Web3(HTTPProvider(
                    URI(ethereum["mainnet"]["infura"]["url"]),
                    request_kwargs={
                        "timeout": ethereum["timeout"]
                    }
                )
            )
        elif network == "testnet":
            self._hash = ethereum["mainnet"]["infura"]["hash"]["eth"]
            self._contract_address = ethereum["testnet"]["infura"]["contract_address"]["eth"]
            self.web3 = Web3(HTTPProvider(
                    URI(ethereum["testnet"]["infura"]["url"]),
                    request_kwargs={
                        "timeout": ethereum["timeout"]
                    }
                )
            )

    # Building transaction
    def build_transaction(self, wallet, htlc, amount):

        # Checking build transaction arguments instance
        if not isinstance(wallet, Wallet):
            raise TypeError("invalid wallet instance, only takes ethereum Wallet class")
        if not isinstance(htlc, HTLC):
            raise TypeError("invalid htlc instance, only takes ethereum HTLC class")
        if not isinstance(amount, int):
            raise TypeError("invalid amount instance, only takes integer type")

        # Getting HTLC instances
        self.htlc = self.web3.eth.contract(
            address=htlc.contract_address(),
            abi=htlc.abi()
        )

        assert htlc.contract_init[3] == Web3.toChecksumAddress(wallet.address())

        self.construct_txn = self.htlc.functions.newContract(
            htlc.contract_init[0],
            htlc.contract_init[1],
            htlc.contract_init[2]
        ).buildTransaction({
            "from": Web3.toChecksumAddress(wallet.address()),
            "nonce": self.web3.eth.getTransactionCount(Web3.toChecksumAddress(wallet.address())),
            "value": int(amount)
        })

        # tx_receipt = self.web3.eth.waitForTransactionReceipt(construct_txn)

        return self

    # Signing transaction using fund solver
    def sign(self, private_key):

        account = self.web3.eth.account.privateKeyToAccount(private_key)
        signed = account.signTransaction(self.construct_txn)
        return signed

    def submit(self, signed):
        tx_hash = self.web3.eth.sendRawTransaction(signed.rawTransaction)
        return hexlify(tx_hash).decode()

        # if not isinstance(solver, FundSolver):
        #     raise TypeError("invalid solver instance, only takes ethereum FundSolver class")
        # if not self.unspent or not self.previous_transaction_indexes or not self.transaction:
        #     raise ValueError("transaction script or unspent is none, build transaction first")
        # outputs = self.outputs(self.unspent, self.previous_transaction_indexes)
        # self.transaction.spend(outputs, [solver.solve() for _ in outputs])
        # return self
