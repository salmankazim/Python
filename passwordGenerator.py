
#Password Generator

import string,random
# print(string.printable[0:95])
dataset = string.printable[0:95]
while True:
    number = int(input("Enter the number: "))
    if number >= 6 and number <= 50:
        password1 = random.sample(dataset,number)
        password2 = ''.join(password1)
        password3 = password2.replace(' ','')
        print(password3)
        break
    else:
        print("Give me other number less than 6 or greater than 50: ")
        

