#!/usr/bin/env python3

from web3 import Web3
from web3.providers import HTTPProvider
from eth_typing import URI

from ..config import ethereum
from ...utils.exceptions import AddressError

# Ethereum configuration
ethereum = ethereum()


def get_web3(network: str) -> (str, str, Web3):
    # Ethereum network setup.
    if network not in ["mainnet", "ropsten", "ganache"]:
        raise ValueError("invalid network type.")
    elif network == "mainnet":
        _hash = ethereum["mainnet"]["hash"]["eth"]
        _contract_address = ethereum["mainnet"]["contract_address"]["eth"]
        _web3 = Web3(HTTPProvider(
                URI(ethereum["mainnet"]["url"]),
                request_kwargs={
                    "timeout": ethereum["timeout"]
                }
            )
        )
        return _hash, _contract_address, _web3
    elif network == "ropsten":
        _hash = ethereum["ropsten"]["hash"]["eth"]
        _contract_address = ethereum["ropsten"]["contract_address"]["eth"]
        _web3 = Web3(HTTPProvider(
                URI(ethereum["ropsten"]["url"]),
                request_kwargs={
                    "timeout": ethereum["timeout"]
                }
            )
        )
        return _hash, _contract_address, _web3
    elif network == "ganache":
        _hash = ethereum["ganache"]["hash"]["eth"]
        _contract_address = ethereum["ganache"]["contract_address"]["eth"]
        _web3 = Web3(HTTPProvider(
                URI(ethereum["ganache"]["url"]),
                request_kwargs={
                    "timeout": ethereum["timeout"]
                }
            )
        )
        return _hash, _contract_address, _web3
    
    
# Get balance by address
def get_balance(address, network="ropsten") -> int:
    """
    Get ethereum balance.

    :param address: ethereum address.
    :type address: str
    :param network: ethereum network, defaults to ropsten.
    :type network: str
    :returns: int -- ethereum balance.

    >>> from shuttle.providers.ethereum.rpc import get_balance
    >>> get_balance(ethereum_address, "ropsten")
    25800000
    """

    if not isinstance(address, str):
        raise TypeError("recipient address must be string format")
    if not Web3.isAddress(address):
        raise AddressError("invalid ethereum recipient %s address" % address)

    _, _, web3 = get_web3(network=network)
    _balance = web3.eth.getBalance(
        web3.toChecksumAddress(address)
    )
    return int(_balance)
