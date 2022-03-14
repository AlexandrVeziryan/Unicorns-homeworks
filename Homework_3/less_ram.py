import random

f = open("4_Gbyte.txt", "a")
strr = ""
for i in range(1_000_000):
    strr += (str(random.randint(1,120)))
    strr += " "

for i in range(1000):
    f.write(strr)


# if i % 10000 == 0:
#     f.write("\n")


