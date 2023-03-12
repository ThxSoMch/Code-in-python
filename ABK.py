import  random

s = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Введите длину пароля  "))

pas = ''

for i in range (length):
    pas += s[random.randint(0, len(s))]

print(pas)
