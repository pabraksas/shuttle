#!/usr/bin/env python3

from datetime import datetime

import json

from shuttle.providers.ethereum.wallet import Wallet
from shuttle.providers.ethereum.htlc import HTLC
from shuttle.providers.ethereum.transaction import FundTransaction
from shuttle.providers.ethereum.solver import FundSolver
from shuttle.providers.ethereum.signature import FundSignature
from shuttle.utils import sha256


# Setting Ganache CLI
NETWORK = "GANACHE".lower()

print("=" * 10, "Sender Ethereum Account")

# acquire law parade avocado pipe army welcome observe mixed lazy awesome brass
SENDER_MNEMONIC = "bamboo notice youth glove ocean whale bullet sniff stuff tube baby horse"
# Initialize ethereum wallet.
sender_wallet = Wallet(network=NETWORK)
# Getting sender wallet form mnemonic.
sender_wallet.from_mnemonic(mnemonic=SENDER_MNEMONIC)
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
sender_balance = sender_wallet.balance()
print("Sender Balance:", sender_balance)

print("=" * 10, "Recipient Ethereum Account")

RECIPIENT_ADDRESS = "0x31AA61a5D8756c84eBdF0F34e01caB90514f2a57"
# Initialize ethereum wallet.
recipient_wallet = Wallet(network=NETWORK)
# Getting sender wallet form mnemonic.
recipient_wallet.from_address(RECIPIENT_ADDRESS)
# Recipient wallet information's
recipient_address = recipient_wallet.address()
print("Recipient Address:", recipient_address)
recipient_balance = recipient_wallet.balance()
print("Recipient Balance:", recipient_balance)

print("=" * 10, "Building new transaction & Initializing Hash Time Lock Contract (HTLC).")

# Building new HTLC transaction.
htlc = HTLC(network=NETWORK).build_transaction(
    wallet=sender_wallet,
    amount=0
)
# Initializing HTLC.
htlc.init(
    secret_hash=sha256("Hello Meheret!".encode()).hex(),
    recipient_address=recipient_address,
    sender_address=sender_address,
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

print("=" * 10, "Unsigned Fund Transaction")

# Initializing fund transaction.
unsigned_fund_transaction = FundTransaction(network=NETWORK)
# Building transaction
unsigned_fund_transaction.build_transaction(
    wallet=sender_wallet,
    htlc=htlc,
    amount=100
)

print("Unsigned Fund Transaction Fee:", unsigned_fund_transaction.fee)
print("Unsigned Fund Transaction Hash:", unsigned_fund_transaction.hash())
print("Unsigned Fund Transaction Raw:", unsigned_fund_transaction.raw())
print("Unsigned Fund Transaction Json:", unsigned_fund_transaction.json())
print("Unsigned Fund Transaction Signature:", unsigned_fund_transaction.signature)

unsigned_fund_raw = unsigned_fund_transaction.unsigned_raw()
print("Unsigned Fund Transaction Unsigned Raw:", unsigned_fund_raw)

print("=" * 10, "Signed Fund Transaction")

# Initialize solver
fund_solver = FundSolver(
    private_key=sender_private_key
)

# Singing Hash Time Lock Contract (HTLC)
signed_fund_transaction = unsigned_fund_transaction.sign(fund_solver)

print("Signed Fund Transaction Fee:", signed_fund_transaction.fee)
print("Signed Fund Transaction Hash:", signed_fund_transaction.hash())
print("Signed Fund Transaction Raw:", signed_fund_transaction.raw())
print("Signed Fund Transaction Signature:", signed_fund_transaction.signature)
print("Signed Fund Transaction Json:", signed_fund_transaction.json())

print("=" * 10, "Fund Signature")

# Singing Hash Time Lock Contract (HTLC)
fund_signature = FundSignature(network=NETWORK)\
    .sign(unsigned_raw=unsigned_fund_raw, solver=fund_solver)

print("Fund Signature Fee:", fund_signature.fee)
print("Fund Signature Hash:", fund_signature.hash())
print("Fund Signature Raw:", fund_signature.raw())
print("Fund Signature Transaction Signature:", fund_signature.signature)
print("Fund Signature Json:", signed_fund_transaction.json())
# print("Fund Signature Json:", json.dumps(fund_signature.json(), indent=4))

signed_fund_raw = fund_signature.signed_raw()
print("Fund Signature Signed Raw:", signed_fund_raw)
