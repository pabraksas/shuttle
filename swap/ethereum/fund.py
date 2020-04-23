#!/usr/bin/env python3

from web3 import Web3, HTTPProvider
from eth_typing import URI
from datetime import datetime

import os

from shuttle.providers.ethereum.wallet import Wallet
from shuttle.providers.ethereum.htlc import HTLC
from shuttle.providers.ethereum.transaction import FundTransaction


web3 = Web3(
    HTTPProvider(
        URI(
            os.environ.get(
                "GANACHE_CLI_HTTP_PROVIDER_URI",
                "http://localhost:8545"
            )
        ), request_kwargs={
            "timeout": 60
        }
    )
)


print("=" * 10, "Sender Ethereum Account")

sender_mnemonic = "divorce trap battle prosper either evoke wreck mammal chase envelope kingdom valley"
# Initialize ethereum sender wallet form mnemonic
sender_wallet = Wallet(account_index=2).from_mnemonic(mnemonic=sender_mnemonic)
# Getting sender ethereum wallet information's
sender_entropy = sender_wallet.entropy()
print("Sender Entropy:", sender_entropy)
sender_mnemonic = sender_wallet.mnemonic()
print("Sender Mnemonic:", sender_mnemonic)
sender_language = sender_wallet.language()
print("Sender Language:", sender_language)
sender_seed = sender_wallet.seed()
print("Sender Seed:", sender_seed)
sender_private_key = sender_wallet.private_key()
print("Sender Private Key:", sender_private_key)
sender_public_key = sender_wallet.public_key()
print("Sender Public Key:", sender_public_key)
sender_finger_print = sender_wallet.finger_print()
print("Sender Finger Print:", sender_finger_print)
sender_path = sender_wallet.path()
print("Sender Path:", sender_path)
sender_address = sender_wallet.address()
print("Sender Address:", sender_address)

print("=" * 10, "Building new transaction Hash Time Lock Contract (HTLC) and Initializing HTLC.")

# Building new HTLC transaction.
htlc = HTLC(web3=web3).build_transaction(
    wallet=sender_wallet,
    amount=0
)
# Initializing HTLC.
htlc.init(
    secret_hash="3a26da82ead15a80533a02696656b14b5dbfd84eb14790f2e1be5e9e45820eeb",
    recipient_address="0x983f9F6A150CD8A788D5Fa9Cc572500491cEE50b",
    sender_address="0x31AA61a5D8756c84eBdF0F34e01caB90514f2a57",
    end_time=int(datetime.timestamp(datetime.now())) + 3600
)

# Getting ethereum HTLC information's
htlc_hash = htlc.hash()
print("HTLC Hash:", htlc_hash)
htlc_contract_address = htlc.contract_address()
print("HTLC Contract Address:", htlc_contract_address)
htlc_bytecode = htlc.bytecode()
print("HTLC Bytecode:", htlc_bytecode)
htlc_opcode = htlc.opcode()
print("HTLC OP_Code:", htlc_opcode)
htlc_abi = htlc.abi()
print("HTLC ABI:", htlc_abi)


fund_transaction = FundTransaction(web3=web3).build_transaction(
    wallet=sender_wallet,
    htlc=htlc,
    amount=100
)

print(fund_transaction.construct_txn)
signed = fund_transaction.sign(sender_wallet.private_key())
print(signed)
print(fund_transaction.submit(signed))

