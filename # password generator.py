import string
import random


s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

charchter_number = input("how mant charchters for password ")

while True:
    try:
            charchter_number=int(charchter_number)

            if charchter_number < 6:

                print("please enter least 6 number")
                charchter_number = input("how mant charchters for password ")
            else :
                break
    except:
        print("please enter only numbers")
        charchter_number = input("how mant charchters for password ")


random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(charchter_number * (30/100)) 
part2 = round(charchter_number * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])


for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

password = "".join(password[0:])
print (password)