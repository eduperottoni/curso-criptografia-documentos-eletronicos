"""AES Wrapper implementation"""

import binascii
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

KEYS_BY_SIZE = {
    "128": bytes.fromhex('637572736F63727970746F6772616679'),
    "192": bytes.fromhex('637572736F63727970746F6772616679637572736F637279'),
    "256": bytes.fromhex('637572736F63727970746F6772616679637572736F63727970746F6772616679')
}


class AESWrapper:
    """Wrapper que encapsula os métodos fornecidos pela biblioteca Cryptodome"""
    def __init__(self, key_size: str, mode: str):
        self.mode = getattr(AES, f'MODE_{mode}')

        nonce = bytes(8)
        iv = bytes(16)
        key = KEYS_BY_SIZE[key_size]

        self.cipher = AES.new(key=key, mode=self.mode)
        if self.mode in [AES.MODE_CBC, AES.MODE_OFB]:
            self.cipher = AES.new(key=key, mode=self.mode, iv=iv)
        if self.mode == AES.MODE_CTR:
            self.cipher = AES.new(key=key, mode=self.mode, nonce=nonce)

    def encrypt(self, plaintext: str) -> str:
        """Cifra texto plano usando chave pré-definida"""

        plaintext = plaintext.encode()
        if self.mode in [AES.MODE_CBC, AES.MODE_ECB]:
            plaintext = pad(plaintext, 16)
        return binascii.hexlify(self.cipher.encrypt(plaintext)).decode('utf-8')

    def decrypt(self, ciphertext: str) -> str:
        """Decifra texto plano com chave pré-definida"""
        deciphered = self.cipher.decrypt(binascii.unhexlify(bytes(ciphertext.encode('utf-8'))))
        if self.mode in [AES.MODE_CBC, AES.MODE_ECB]:
            deciphered = unpad(deciphered, 16)
        return deciphered.decode()


MODE = input()
KEY_SIZE = input()
ACTION = input()
TEXT = input()

aes_wrapper = AESWrapper(KEY_SIZE, MODE)
print(aes_wrapper.encrypt(TEXT) if ACTION == 'E' else aes_wrapper.decrypt(TEXT))
