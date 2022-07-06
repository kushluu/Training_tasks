import string
import random
#import getpass
lis = list(string.ascii_letters +"!@#$%^&*()" + string.digits)
random.shuffle(lis)
def pwd_gen():
    length=int(input())# getpass.getpass()
    password = ""
    for i in range(int(length)):
        password += random.choice(lis)
    print(password)
pwd_gen()
