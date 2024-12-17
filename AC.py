from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta
import random


class AC:
    def __init__(self):
        self.certificados = {}
        self.ca_certificate = None
        self.ca_private_key = None
        self.ca_name = None

    def __get_not_before_and_not_after(self):
        """
        Obtém tempos de validade do certificado
        """
        not_before = datetime.now()
        not_after = not_before + timedelta(days=365)
        return (not_before, not_after)

    def issueSelfsignedCertificate(self, common_name="AC-Raiz", country="BR", state="SC", locality="Fln", organization="UFSC"):
        """
        Cria um certificado autoassinado com validade de 1 ano para a CA.

        Args:
            common_name (str): O nome comum (CN) do certificado.
            country (str): O pais do certificado. 
            state (str): O estado do certificado. 
            locality (str): A cidade ou endereco do certificado. 
            organization (str): O nome da CA. 

        Returns:subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name)
        ])
            tuple: O certificado X.509 autoassinado e sua chave privada.
        """
        self.ca_private_key = rsa.generate_private_key(65537, 2048)
        not_before, not_after = self.__get_not_before_and_not_after()

        self.ca_name = subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name)
        ])

        self.ca_certificate = x509.CertificateBuilder(issuer,
                                                      subject,
                                                      self.ca_private_key.public_key(),
                                                      x509.random_serial_number(),
                                                      not_before,
                                                      not_after).sign(self.ca_private_key, hashes.SHA256)

    def issueEndCertificate(self, public_key, common_name, country, state, locality, organization):
        """
        Emite um certificado final assinado pela CA com validade de 1 ano.

        Args:
            public_key (CryptoRSA.RsaKey): A chave publica do requerente do certificado.
            common_name (str): O nome comum (CN) do certificado.
            country (str): O pais do certificado. 
            state (str): O estado do certificado. 
            locality (str): A cidade ou endereco do certificado. 
            organization (str): O nome da organizacao requerente. 

        Returns:
            cert (Certificate): O certificado X.509.
        """
        subject = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name)
        ])
        not_before, not_after = self.__get_not_before_and_not_after()
        return x509.CertificateBuilder(self.ca_name,
                                       subject,
                                       public_key,
                                       x509.random_serial_number(),
                                       not_before,
                                       not_after).sign(self.ca_private_key, hashes.SHA256)

    def validateCertificate(self, cert):
        """
        Recupera a chave pública de um certificado se este não estiver expirado e tenha sido assinado por esta AC.
        Obs: a validacao feita neste metodo apenas se refere a data de validade do certificado e se este foi assinado pela AC, sendo assim, uma simplificação.

        Args:
            cert (Certificate): O certificado a ser validado.

        Returns:
            CryptoRSA.RsaKey or None: A chave publica do certificado, ou None se o certificado não for valido.
        """
