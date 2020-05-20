#!/usr/bin/env python3

from datetime import datetime


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
def ethereum(project_id=None):
    if project_id is None:
        project_id = "4414fea5f7454211956b1627621450b4"
    return {
        "mainnet": {
            "url": "https://mainnet.infura.io/v3/%s" % project_id,
            "hash": {
                "eth": "",
                "erc20": "",
                "erc721": ""
            },
            "contract_address": {
                "eth": "",
                "erc20": "",
                "erc721": ""
            }
        },
        "ropsten": {
            "url": "https://ropsten.infura.io/v3/%s" % project_id,
            "hash": {
                "eth": "",
                "erc20": "",
                "erc721": ""
            },
            "contract_address": {
                "eth": "",
                "erc20": "",
                "erc721": ""
            }
        },
        "ganache": {
            "url": "http://localhost:8545",
            "hash": {
                "eth": "",
                "erc20": "",
                "erc721": ""
            },
            "contract_address": {
                "eth": "",
                "erc20": "",
                "erc721": ""
            }
        },
        "gas": 3000000,
        "timeout": 60,
        "time": int(datetime.timestamp(datetime.now())) + (3600 * 1)  # 1 hour
    }
