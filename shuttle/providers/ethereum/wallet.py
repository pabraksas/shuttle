#!/usr/bin/env python3

from eth_wallet import Wallet as ETHWallet

# from .rpc import get_balance, account_create


# Ethereum Wallet.
class Wallet:
    """
    Ethereum Wallet class.

    :param path: ethereum derivation path, defaults to "m/44'/60'/0'/0/0".
    :type path: str
    :returns:  Wallet -- ethereum wallet instance.
    """

    # PyShuttle Ethereum (BTM) wallet init.
    def __init__(self, path="m/44'/60'/0'/0/0"):

        # Derivation path
        self._path = path
        # Ethereum wallet initialization.
        self.ethereum = None
        # Wallet info's
        self.dumps = None

    # Ethereum wallet from entropy
    def from_entropy(self, entropy, passphrase=None, language=None):
        """
        Initiate ethereum wallet from entropy.

        :param entropy: Ethereum wallet entropy.
        :type entropy: str.
        :param passphrase: mnemonic passphrase, defaults to None.
        :type passphrase: str.
        :param language: mnemonic language, defaults to None.
        :type language: str.
        :returns:  Wallet -- ethereum wallet instance.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet(path="m/44'/60'/0'/0/0'")
        >>> wallet.from_entropy("8d7454bb99e8e68de6adfc5519cbee64")
        <shuttle.providers.ethereum.wallet.Wallet object at 0x040DA268>
        """

        # Ethereum wallet initialization.
        self.ethereum = ETHWallet()
        self.ethereum.from_entropy(entropy=entropy, passphrase=passphrase, language=language)
        self.ethereum.from_path(path=self._path)
        self.dumps = self.ethereum.dumps()
        return self

    # Ethereum wallet from mnemonic
    def from_mnemonic(self, mnemonic, passphrase=None, language=None):
        """
        Initiate ethereum wallet from mnemonic.

        :param mnemonic: Ethereum wallet mnemonic.
        :type mnemonic: str.
        :param passphrase: mnemonic passphrase, defaults to None.
        :type passphrase: str.
        :param language: mnemonic language, defaults to None.
        :type language: str.
        :returns:  Wallet -- ethereum wallet instance.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet(path="m/44'/60'/0'/0/0'")
        >>> wallet.from_mnemonic("occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo")
        <shuttle.providers.ethereum.wallet.Wallet object at 0x040DA268>
        """

        # Ethereum wallet initialization.
        self.ethereum = ETHWallet()
        self.ethereum.from_mnemonic(mnemonic=mnemonic, passphrase=passphrase, language=language)
        self.ethereum.from_path(path=self._path)
        self.dumps = self.ethereum.dumps()
        return self

    # Ethereum wallet from seed
    def from_seed(self, seed):
        """
        Initiate ethereum wallet from seed.

        :param seed: Ethereum wallet seed.
        :type seed: str.
        :returns:  Wallet -- ethereum wallet instance.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet(path="m/44'/60'/0'/0/0'")
        >>> wallet.from_seed("a0f734f68f800f1f43719473fbdcdb64b83a3d180add1d6f819ccbf5abbcb852c791d7e8249a62e1bbda60322de7ce0d0f3d5649e368431d058bbe6879ad2cd6")
        <shuttle.providers.ethereum.wallet.Wallet object at 0x040DA268>
        """

        # Ethereum wallet initialization.
        self.ethereum = ETHWallet()
        self.ethereum.from_seed(seed=seed)
        self.ethereum.from_path(path=self._path)
        self.dumps = self.ethereum.dumps()
        return self

    # Ethereum wallet from private key
    def from_private_key(self, private_key):
        """
        Initiate ethereum wallet from private key.

        :param private_key: Ethereum wallet private key.
        :type private_key: str.
        :returns:  Wallet -- ethereum wallet instance.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet()
        >>> wallet.from_private_key("6fc58f27cec4b943e8a1f53bf7d54ecb0a22bd01c21e7d383870e99531b2ba24")
        <shuttle.providers.ethereum.wallet.Wallet object at 0x040DA268>
        """

        # Ethereum wallet initialization.
        self.ethereum = ETHWallet()
        self.ethereum.from_private_key(private_key=private_key)
        self.dumps = self.ethereum.dumps()
        return self

    # Path derivation
    def from_path(self, path):
        self.ethereum.from_path(path=path)
        self.dumps = self.ethereum.dumps()
        return self

    # Getting private key
    def private_key(self):
        """
        Get ethereum wallet private key.

        :return: str -- ethereum private key.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet(path="m/44'/60'/0'/0/0'")
        >>> wallet.from_mnemonic("occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo")
        >>> wallet.private_key()
        "6fc58f27cec4b943e8a1f53bf7d54ecb0a22bd01c21e7d383870e99531b2ba24"
        """

        return self.dumps["private_key"]

    # Getting public key
    def public_key(self):
        """
        Get ethereum wallet public key.

        :return: str -- ethereum public key.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet(path="m/44'/60'/0'/0/0'")
        >>> wallet.from_mnemonic("occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo")
        >>> wallet.public_key()
        "024de8f3421dc1138c1d1ccd9bfe22d727d7639475eb852c54cc8b3fddd9c5e9e6"
        """

        return self.dumps["public_key"]

    # Getting uncompressed public key
    def uncompressed(self):
        """
        Get ethereum wallet uncompressed public key.

        :return: str -- ethereum uncompressed public key.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet(path="m/44'/60'/0'/0/0'")
        >>> wallet.from_mnemonic("occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo")
        >>> wallet.uncompressed()
        "4de8f3421dc1138c1d1ccd9bfe22d727d7639475eb852c54cc8b3fddd9c5e9e66c153cd99d81f9db5985e5ba0ba4ca49d51086c8c89a7fdbc568c394fcfdfb3e"
        """

        return self.dumps["uncompressed"]

    # Getting entropy
    def entropy(self):
        """
        Get ethereum wallet entropy.

        :return: str -- entropy.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet()
        >>> wallet.from_entropy("8d7454bb99e8e68de6adfc5519cbee64")
        >>> wallet.entropy()
        "8d7454bb99e8e68de6adfc5519cbee64"
        """

        return self.dumps["entropy"]

    # Getting mnemonic
    def mnemonic(self):
        """
        Get ethereum wallet mnemonic.

        :return: str -- 12 word mnemonic.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet()
        >>> wallet.from_entropy(entropy="8d7454bb99e8e68de6adfc5519cbee64", language="italian")
        >>> wallet.mnemonic()
        "occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo"
        """

        return self.dumps["mnemonic"]

    # Getting language
    def language(self):
        """
        Get ethereum wallet mnemonic language.

        :return: str -- language.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet()
        >>> wallet.from_mnemonic("occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo")
        >>> wallet.language()
        "italian"
        """

        return self.dumps["language"]

    # Getting seed
    def seed(self):
        """
        Get ethereum wallet seed.

        :return: str -- ethereum seed.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet(path="m/44'/60'/0'/0/0'")
        >>> wallet.from_mnemonic("occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo")
        >>> wallet.seed()
        "a0f734f68f800f1f43719473fbdcdb64b83a3d180add1d6f819ccbf5abbcb852c791d7e8249a62e1bbda60322de7ce0d0f3d5649e368431d058bbe6879ad2cd6"
        """

        return self.dumps["seed"]

    # Getting path
    def path(self):
        """
        Get ethereum wallet derivation path.

        :return: str -- ethereum derivation path.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet()
        >>> wallet.from_mnemonic("occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo")
        >>> wallet.path()
        "m/44'/60'/0'/0/0"
        """

        return self.dumps["path"]

    # Getting address
    def address(self):
        """
        Get ethereum wallet address.

        :return: str -- ethereum address.

        >>> from shuttle.providers.ethereum.wallet import Wallet
        >>> wallet = Wallet(path="m/44'/60'/0'/0/0'")
        >>> wallet.from_mnemonic("occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo")
        >>> wallet.address()
        "0x89f64dFE79777217BD16a278EE675DaE9c089729"
        """

        return self.dumps["address"]

    # # Getting balance
    # def balance(self):
    #     """
    #     Get ethereum wallet balance.
    #
    #     :return: int -- ethereum balance.
    #
    #     >>> from shuttle.providers.ethereum.wallet import Wallet
    #     >>> wallet = Wallet(network="mainnet")
    #     >>> wallet.from_mnemonic("occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo")
    #     >>> wallet.balance()
    #     2450000000
    #     """
    #
    #     return get_balance(address=self.address(), network=self.network)
