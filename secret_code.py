import random
import string
str = string.ascii_letters
command = input("Enter 'code' for Encrypt and 'decode' for decrypt: ")
message_delivered = ""
if command == "code" :
    message = input("Enter Your Message: ")
    action = message.split(" ")
    for el in action:
        if len(el) < 3 :
            a = ''.join(reversed(el))
            message_delivered = message_delivered + " " + a
        else : 
            a = el[0]
            new = el[1:]
            new += a
            for i in range(3):
                r1 = random.choice(str)
                r2 = random.choice(str)
                new = r1 + new + r2
            message_delivered = message_delivered + " " + new
    print("your coded message is\n", message_delivered)
elif command == "decode":
    message = input("Enter Your Coded Message: ")
    action = message.split(" ")
    for el in action:
        if len(el) < 3 :
            a = ''.join(reversed(el))
            message_delivered = message_delivered + " " + a
        else :
            new = el[3:-3]
            a = new[-1]
            new = a + new[0:-1]
            message_delivered = message_delivered + " " + new
    print("your decoded message is\n", message_delivered)
else :
    print("Invalid input")

