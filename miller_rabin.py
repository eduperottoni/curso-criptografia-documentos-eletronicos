"""Arquivo para implementação de teste de primalidade pelo algoritmo de Miller-Rabin"""


class MillerRabin:
    """Dado n ímpar, n-1 = 2^k*m
    Dado 1 < a < n-1:
        - testa se a^m mod n == 1
        - testa se [a^(2^i)m] mod n == n -1, p/ 0 < i < k

    Quanto mais a's forem testados, mais chances de certeza
    """
    def __init__(self):
        self.range_for_testing_a = range(2, 6)

    def __factorize_by_2_powers(self, n: int) -> 'tuple[int, int]':
        """Fatora um número par em potências de 2
        Escreve n (par) como [2^k * m]

        Returns:
            k e m, respectivamente, em uma tupla
        """
        m, k = n, 0
        while (m) % 2 == 0:
            m /= 2
            k += 1
        return (k, m)

    def __modular_power(self, base: int, exponent: int, module: int) -> 'int':
        """Calcula exponenciação utilizando regras de aritmética modular
        Isso deixa o cálculo mais eficiente
        (base^exponent) % module => (base % module)^exponent

        Args:
            base: base da exponenciação
            exponent: expoente inteiro
            module: módulo em que será feito o cálculo
        """

        base %= module
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % module
            base = (base * base) % module
            exponent //= 2
        return result

    def __test_is_prime(self, n: int, a: int, m: int, k: int) -> 'bool':
        """Aplica o teste de Miller-Rabin para um valor de a

        Args:
            n = número ao quela se testa a primalidade
            a = número "aleatório" para aplicação do teste (1 < a < n-1)
            m e k = vêm da expressão n-1 = 2^k * m
        """
        if n == 2:
            return True
        if n % 2 == 0:
            return False 

        # a^m mod n = 1 ?
        x = self.__modular_power(a, m, n)

        if x in (1, n-1):  # We already test here the case i = 0 of the loop below
            return True

        # [a^(2^i*m)] mod n = n-1 p/ algum 0 < i < k?
        for _ in range(k - 1):
            x = self.__modular_power(x, 2, n)
            if x == n-1:
                return True

        return False

    def test_for_many_a(self, n: int) -> 'list[tuple[int, bool]]':
        """Retorna o resultado do teste de Miller-Rabin para valores de
        a definidos no atributo self.range_for_testing_a

        Args:
            n: deve ser ímpar
                ex.: 7
        Return:
            lista de tuplas de inteiros e booleanos, onde cada tupla representa
            um teste feito com um valor diferente de a. Caso alguam tupla
            contenha o valor False, ela será a última, pois o algoritmo para
            caso o número seja certamente composto para algum valor de a.
                ex.: [
                    (2, True),
                    (3, True),
                    (4, True),
                    (5, True)
                ]
        """

        # Escrevendo n-1 como 2^k*m
        k, m = self.__factorize_by_2_powers(n-1)

        return_list = []

        for a in self.range_for_testing_a:
            prime = self.__test_is_prime(n, a, int(m), k)
            return_list.append((a, prime))
            if not prime:
                break

        return return_list


INPUT = int(input())

miller = MillerRabin()

tests_results = miller.test_for_many_a(INPUT)

# Formatando a saída
is_prime = True
for a, prime in tests_results:
    print(f"Teste a={a} -> {'Provavelmente primo' if prime else 'Composto'}")
    if not prime:
        is_prime = False
print(f"Resultado final: {INPUT} é {'provavelmente primo' if is_prime else 'composto'}")