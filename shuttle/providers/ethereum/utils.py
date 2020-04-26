#!/usr/bin/env python3

from web3 import Web3
from binascii import hexlify, unhexlify

from ...utils.exceptions import BalanceError


def is_address(address: str) -> bool:
    """
    Check ethereum address.

    :param address: ethereum address.
    :type address: str
    :returns: bool -- ethereum valid/invalid address.

    >>> from shuttle.providers.ethereum.utils import is_address
    >>> is_address("0xd3CdA913deB6f67967B99D67aCDFa1712C293601")
    True
    """

    if not isinstance(address, str):
        raise TypeError("address must be string format!")

    return Web3.isAddress(address)


def to_checksum_address(address: str) -> str:
    """
    Change ethereum address to checksum address.

    :param address: ethereum address.
    :type address: str
    :returns: str -- ethereum checksum address.

    >>> from shuttle.providers.ethereum.utils import to_checksum_address
    >>> to_checksum_address("0xd3cda913deb6f67967b99d67acdfa1712c293601")
    "0xd3CdA913deB6f67967B99D67aCDFa1712C293601"
    """

    if not is_address(address):
        raise TypeError("invalid ethereum address.")

    return Web3.toChecksumAddress(address)


def submit(web3, signed):
    try:
        tx_hash = web3.eth.sendRawTransaction(signed)
    except ValueError as value_error:
        if str(value_error).find("sender doesn't have enough funds to send tx") != -1:
            raise BalanceError("insufficient spend balance")
        raise value_error
    return hexlify(tx_hash).decode()
