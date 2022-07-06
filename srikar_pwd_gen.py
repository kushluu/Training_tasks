import string
import random
from IPython.display import clear_output
#import getpass
lis = list(string.ascii_letters +"!@#$%^&*()" + string.digits)
random.shuffle(lis)
def pwd_gen():
    length=int(input())# getpass.getpass()
    clear_output()
    password = ""
    for i in range(int(length)):
        password += random.choice(lis)
    print(password)
pwd_gen()
