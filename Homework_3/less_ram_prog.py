import psutil

ram_before = psutil.virtual_memory()[3] // 1048576
print(ram_before, "Mb")  # physical memory usage
f = open("4_Gbyte.txt", "r")

elements = [0 for _ in range(121)]
n = 0
while True:
    n += 1
    print(n)
    print(psutil.virtual_memory()[3] // 1048576, "Mb")  # physical memory usage
    print("Difference:1 ",psutil.virtual_memory()[3] // 1048576 - ram_before, "Mb")  # physical memory usage
    line = f.readline(4_000_000)
    line = line.split()
    if line:
        for i in line:
            elements[int(i)] += 1

    else:
        break

print(elements)
ram_after = psutil.virtual_memory()[3] // 1048576
print(ram_before, "Mb")  # physical memory usage
print(ram_after, "Mb")  # physical memory usage
print("Difference:3 ",psutil.virtual_memory()[3] // 1048576 - ram_before, "Mb")  # physical memory usage

f.close()

print()
print()

a = open("sorted.txt", "a")
lenn = 0
size = 1_000_000
for i in range(121):
    lenn = elements[i]
    strr = str(i) + " "
    print("Difference:5 ",psutil.virtual_memory()[3] // 1048576 - ram_before, "Mb")  # physical memory usage
    while True:
        if lenn < size:
            a.write(strr * lenn)
            break
        a.write(strr * size)
        lenn -= size
    print("Difference:5.5 ",psutil.virtual_memory()[3] // 1048576 - ram_before, "Mb")  # physical memory usage
    
a.close()

a = open("sorted.txt", "r")

line = a.readline(162319564) # printing [0; 10]
line = line.split()
print(line)

a.close()


