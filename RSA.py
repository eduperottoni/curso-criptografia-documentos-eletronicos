"""
Implementação do modelo RSA fornecido no enunciado
"""
import base64

from Cryptodome.PublicKey import RSA as rsa
from Cryptodome.Cipher import PKCS1_OAEP


class RSA:
    """Classe que encapsula operações do algoritmo RSA"""

    def __init__(self, key_size: int = 2048, public_exponent: int = 65537) -> None:
        """
        Inicializa a classe RSA, gerando um par de chaves (pública e privada) com o tamanho e o expoente fornecidos.

        :param key_size: Tamanho da chave RSA em bits (padrão 2048).
        :param public_exponent: Expoente público para geração da chave (padrão 65537).
        :return: Nenhum valor de retorno (None).
        """
        self.private_key, self.public_key = None, None
        self.generate_keys(key_size, public_exponent)
        self.cipher = PKCS1_OAEP.new(self.private_key)

    def generate_keys(self, key_size: int, public_exponent: int) -> None:
        """
        Gera um par de chaves RSA e as armazena nos atributos da classe.

        :return: Nenhum valor de retorno (None).
        """
        key: rsa.RsaKey = rsa.generate(bits=key_size, e=public_exponent)

        self.private_key = key
        self.public_key = key.public_key()

    def encrypt_message(self, message: str, public_key: rsa.RsaKey) -> str:
        """
        Criptografa uma mensagem utilizando a chave pública fornecida.

        :param message: A mensagem em texto plano que será criptografada.
        :param public_key: A chave pública do destinatário que será usada para a criptografia.
        :return: A mensagem criptografada, codificada em base64.
        """
        cipher = PKCS1_OAEP.new(public_key)
        ciphered = cipher.encrypt(message.encode())
        return base64.b64encode(ciphered).decode()

    def decrypt_message(self, ciphertext: str) -> str:
        """
        Descriptografa uma mensagem criptografada usando a chave privada do destinatário (essa classe!).

        :param ciphertext: A mensagem criptografada em formato base64.
        :return: A mensagem em texto plano, após ser descriptografada.
        """
        ciphertext = base64.b64decode(ciphertext)
        deciphered = self.cipher.decrypt(ciphertext)
        return deciphered.decode()

    def export_public_key(self) -> bytes:
        """
        Exporta a chave pública da instância em um formato externo (PEM).

        :return: A chave pública em formato exportável (bytes).
        """
        return self.public_key.export_key()  # exports in PEM format by default 
