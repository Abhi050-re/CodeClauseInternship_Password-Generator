import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="{}?@*#$%^&+-"
all=lower+upper+numbers+symbols
length=10
for i in range(1):
    password="".join(random.sample(all,length))
    print(password)