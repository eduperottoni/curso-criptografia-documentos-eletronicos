"""Vigenere Cipher exercise"""

import string
from typing import Callable


class VigenereCipher:
    """Class to handle Vigenere scripts"""
    __alphabet = list(string.ascii_uppercase)

    @classmethod
    def __get_replacement_char_for_cipher(
        cls, original: str, shift: str
    ) -> str:
        total_shift = (
            cls.__alphabet.index(original) + cls.__alphabet.index(shift)
        )
        return cls.__alphabet[total_shift % 26]

    @classmethod
    def __get_replacement_char_for_decipher(
        cls, original: str, shift: str
    ) -> str:
        total_shift = (
            cls.__alphabet.index(original) - cls.__alphabet.index(shift)
        )
        return cls.__alphabet[total_shift % 26]

    @classmethod
    def __general_operation(
        cls,
        original_text: str,
        secret_key: str,
        substitution_function: Callable
    ) -> str:
        """General Vigenere operation. In this cipher, ciphering and
        deciphering work the same way, just changing the substitution function
        """
        secret_key_length = len(secret_key)
        final_text = ''
        for i, char in enumerate(original_text):
            secret_key_shift = secret_key[(i % secret_key_length)]
            final_text += substitution_function(char, secret_key_shift)

        return final_text

    @classmethod
    def cipher(cls, plain_text: str, secret_key: str) -> str:
        """Cipher a plain text based on a secret key"""
        return cls.__general_operation(
            plain_text, secret_key, cls.__get_replacement_char_for_cipher
        )

    @classmethod
    def decipher(cls, ciphered_text: str, secret_key: str) -> str:
        """Decipher a ciphered text based on a secret key"""
        return cls.__general_operation(
            ciphered_text, secret_key, cls.__get_replacement_char_for_decipher
        )


# TEXT = input().strip()
# KEY = input().strip()
# OPERATION = input().strip()


TEXT = 'AULA NO SABADO E BOM'
KEY = 'SEGURO'
OPERATION = 'c'

print(
    VigenereCipher.cipher(TEXT, KEY)
    if OPERATION == 'c'
    else VigenereCipher.decipher(TEXT, KEY)
)
