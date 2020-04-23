#!/usr/bin/env python3


# Bitcoin network
def bitcoin(blockcypher_token=None):
    if blockcypher_token is None:
        blockcypher_token = "c6ef693d3c024088810e6fac2a1494ee"
    return {
        "mainnet": {
            "blockchain": "https://blockchain.info",
            "smartbit": "https://api.smartbit.com.au/v1/blockchain",
            "blockcypher": {
                "url": "https://api.blockcypher.com/v1/btc/main",
                "token": blockcypher_token
            }
        },
        "testnet": {
            "blockchain": "https://testnet.blockchain.info",
            "smartbit": "https://testnet-api.smartbit.com.au/v1/blockchain",
            "blockcypher": {
                "url": "https://api.blockcypher.com/v1/btc/test3",
                "token": blockcypher_token
            }
        },
        "timeout": 60,
        "sequence": 100
    }


# Bytom network
def bytom():
    return {
        "mainnet": {
            "bytom": "http://localhost:9888",
            "blockmeta": "https://blockmeta.com/api/v2",
            "blockcenter": "https://bcapi.bystack.com/api/v2/btm"
        },
        "solonet": {
            "bytom": "http://localhost:9888",
            "blockmeta": "https://blockmeta.com/api/v2",
            "blockcenter": "https://bcapi.bystack.com/api/v2/btm"
        },
        "testnet": {
            "bytom": "http://localhost:9888",
            "blockmeta": "https://blockmeta.com/api/wisdom",
            "blockcenter": "https://bcapi.bystack.com/api/v2/wisdom"
        },
        "timeout": 60,
        "BTM_asset": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        "fee": 10000000,
        "confirmations": 1,
        "sequence": 100
    }


# Ethereum network
def ethereum():
    return {
        "mainnet": {
            "infura": {
                "url": "http://localhost:9888",
                "contract_address": {
                    "eth": "",
                    "erc20": ""
                }
            }
        },
        "testnet": {
            "infura": {
                "url": "http://localhost:9888",
                "contract_address": {
                    "eth": "",
                    "erc20": ""
                }
            }
        },
        "wait_for_transaction_receipt_timeout": 120,
        "gas": 3000000,
        "timeout": 60,
        "time": 1  # hour
    }
