#/usr/bin/env python
#coding:utf8
# Author : liufapeng
# Date :2019-6-11
# test jira wit gitlab  2019.8.1
# test second time , the first was failureed 
# invited langge close to me . 3th  
# Closes TIS-1 failured 
# Resolves TIS-1 failureed
# TIS-2 test
# Closes TIS-2 starting 
# Closes TIS-2 second time
#  Closes TIS-2 third time
# commit again test TIS-2
# # commit again third TIS-2

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes, serialization
from cryptography import x509
from cryptography.x509.oid import NameOID
import datetime


########################################################################
class IssueCertificate(object):
    """This is a issuer for TLS certificate, it can genarate a root ca 
    certificate and service's certificate"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        #issuer information
        self.common_name = u'Root CA'
        self.organization_name = u'Root'
        self.country_name = u'CN'
        self.state_or_province_name = u'BEIJING'
        self.organization_unit_name = u'architecture centre'
        self.issuer_email_address = u'pengfaliu@163.com'
        
        #valid date for certificate (day)
        self.default_days = 1
                
        # the format for certificate
        self.rootCA_private_key_and_certificate_of_PEM = "PaulRooCA.pem"
        self.rootCA_certificate = "PaulRootCA.crt"

        
    #----------------------------------------------------------------------
    def validate(self):
        """data caculate"""
        one_day = datetime.timedelta(days=self.default_days)
        today = datetime.date.today()
        
        yest = today - one_day
        tom = today + one_day
        yesterday = datetime.datetime(yest.year, yest.month, yest.day)
        tomorrow = datetime.datetime(tom.year, tom.month, tom.day)        
        
        return (yesterday,tomorrow)
    #----------------------------------------------------------------------
    def GenerateRootCertificate(self):
        """"""
        yesterday = self.validate()[0]
        tomorrow = self.validate()[1]
        #生成根CA证书的私钥
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        
        #指定根CA机构的名称,国家,邮箱信息等
        ca_name = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, self.common_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, self.organization_name),
            x509.NameAttribute(NameOID.COUNTRY_NAME, self.country_name),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, self.organization_unit_name),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME,self.state_or_province_name),
            x509.NameAttribute(NameOID.EMAIL_ADDRESS, self.issuer_email_address)
        ])
        
        #基于X509 V3格式构建根CA证书内容
        serial_number = x509.random_serial_number()
        public_key = private_key.public_key()
        builder = x509.CertificateBuilder()
        builder = builder.subject_name(ca_name)
        builder = builder.issuer_name(ca_name)
        builder = builder.not_valid_before(yesterday)
        builder = builder.not_valid_after(tomorrow)
        builder = builder.serial_number(serial_number) #x509.random_serial_number()
        builder = builder.public_key(public_key)
        
        #基于X509 V3的格式的构建根证书的扩展字段
        builder = builder.add_extension(
            x509.BasicConstraints(ca=True, path_length=None),
            critical=True)
        
        
        #基于x509的根CA证书的签名方法
        certificate = builder.sign(
            private_key=private_key, algorithm=hashes.SHA256(),
            backend=default_backend()
        )
        
        #根CA证书私钥格式
        private_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        #根CA证书公钥格式
        public_bytes = certificate.public_bytes(
            encoding=serialization.Encoding.PEM)
        
        #写入根证书的私钥文件和公共证书
        with open(self.rootCA_private_key_and_certificate_of_PEM, "wb") as fout:
            fout.write(private_bytes + public_bytes)
        with open(self.rootCA_certificate, "wb") as fout:
            fout.write(public_bytes)        
        
        #返回颁发者的ca,公钥，私钥信息
        return ca_name,public_key,private_key
  



    #----------------------------------------------------------------------
    def GenerateSubjectCertificate(self,subject_domain = 'service.test.local' ):
        """"""
        yesterday = self.validate()[0]
        tomorrow = self.validate()[1]
        
        #subject certificate information
        subject_private_key_and_certificate_of_PEM = subject_domain+".pem"
        subject_certificate = subject_domain+".crt"
        
        #颁发者的相关信息
        ca_name = self.GenerateRootCertificate()[0]
        public_key = self.GenerateRootCertificate()[1]
        private_key = self.GenerateRootCertificate()[2]
        
        #生成申请者的证书私钥
        service_private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        
        #生成申请者证书的公钥
        service_public_key = service_private_key.public_key()
        builder = x509.CertificateBuilder()
        
        #申请者证书:基于X509证书格式
        builder = builder.subject_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, subject_domain)
        ]))
        builder = builder.issuer_name(ca_name)
        builder = builder.serial_number(123456)
        builder = builder.not_valid_before(yesterday)
        builder = builder.not_valid_after(tomorrow)
        builder = builder.public_key(public_key)
        
        #基于X509 V3的格式的构建申请者证书的扩展字段
        builder = builder.add_extension(
            x509.BasicConstraints(ca=False, path_length=None),
            critical=True)
        
        #申请者证书:基于X509证书格式，签名
        certificate = builder.sign(
            private_key=private_key, algorithm=hashes.SHA256(),
            backend=default_backend()
        )
        
        #申请者证书:私钥证书格式
        private_bytes = service_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        #申请者证书:公共证书格式
        public_bytes = certificate.public_bytes(
            encoding=serialization.Encoding.PEM
        )
        
        #生成申请者证书
        with open(subject_private_key_and_certificate_of_PEM, "wb") as fout:
            fout.write(private_bytes + public_bytes)        
        with open(subject_certificate, "wb") as fout:
            fout.write(public_bytes)        

if __name__ == "__main__":
    subject_name = u"www.test.lo"
    test = IssueCertificate()
    test.GenerateRootCertificate()
    test.GenerateSubjectCertificate(subject_domain=subject_name)
