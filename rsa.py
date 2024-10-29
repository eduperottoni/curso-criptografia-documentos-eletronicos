"""
Implementação do modelo RSA fornecido no enunciado
"""


class RSA:
    """Classe que encapsula operações do algoritmo RSA"""

    def __init__(self, key_size: int = 2048, public_exponent: int = 65537) -> None:
        """
        Inicializa a classe RSA, gerando um par de chaves (pública e privada) com o tamanho e o expoente fornecidos.

        :param key_size: Tamanho da chave RSA em bits (padrão 2048).
        :param public_exponent: Expoente público para geração da chave (padrão 65537).
        :return: Nenhum valor de retorno (None).
        """
        self.private_key
        self.public_key
        self.generate_keys(key_size, public_exponent)

    def generate_keys(self, key_size: int, public_exponent: int) -> None:
        """
        Gera um par de chaves RSA e as armazena nos atributos da classe.

        :return: Nenhum valor de retorno (None).
        """
        pass

    def encrypt_message(self, message: str, public_key) -> str:
        """
        Criptografa uma mensagem utilizando a chave pública fornecida.

        :param message: A mensagem em texto plano que será criptografada.
        :param public_key: A chave pública do destinatário que será usada para a criptografia.
        :return: A mensagem criptografada, codificada em base64.
        """
        pass

    def decrypt_message(self, ciphertext: str) -> str:
        """
        Descriptografa uma mensagem criptografada usando a chave privada do destinatário (essa classe!).

        :param ciphertext: A mensagem criptografada em formato base64.
        :return: A mensagem em texto plano, após ser descriptografada.
        """
        pass

    def export_public_key(self) -> bytes:
        """
        Exporta a chave pública da instância em um formato externo (PEM).

        :return: A chave pública em formato exportável (bytes).
        """
        pass
