import random
import string

pass_len = int(input("Enter your desired password length 🔐: "))
str = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(pass_len):
    password += random.choice(str)
print("Your generated password is here! 🔐\n",password)

# #another method
# password = "".join([random.choice(str) for i in range(pass_len)])
# print("Your generated password is here! 🔐\n",password)