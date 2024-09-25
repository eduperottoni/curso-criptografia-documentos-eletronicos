"""AES Wrapper implementation"""

import binascii
from enum import Enum
from Cryptodome.Cipher import AES


KEYS_BY_SIZE = {
    "128": bytes.fromhex('637572736F63727970746F6772616679'),
    "192": bytes.fromhex('637572736F63727970746F6772616679637572736F637279'),
    "256": bytes.fromhex('637572736F63727970746F6772616679637572736F63727970746F6772616679')
}

class AESWrapper:
    """Wrapper que encapsula os métodos fornecidos pela biblioteca Cryptodome"""
    def __init__(self, key_size: str, mode: str):
        self.cipher = AES.new(KEYS_BY_SIZE[key_size], getattr(AES, f"MODE_{mode}"))

    def encrypt(self, plaintext: str) -> str:
        """Cifra texto plano usando chave pré-definida"""
        return binascii.hexlify(self.cipher.encrypt(bytes(plaintext.encode('utf-8')))).decode('utf-8')

    def decrypt(self, ciphertext: str) -> str:
        """Decifra texto plano com chave pré-definida"""
        return binascii.hexlify(self.cipher.decrypt(bytes(ciphertext.encode('utf-8')))).decode('utf-8')


MODE = input()
KEY_SIZE = input()
ACTION = input()
TEXT = input()

aes_wrapper = AESWrapper(KEY_SIZE, MODE)
print(aes_wrapper.encrypt(TEXT) if ACTION == 'E' else aes_wrapper.decrypt(TEXT))
