import psutil

ram_before = psutil.virtual_memory()[3] // 1048576
print(ram_before, "Mb")  # physical memory usage
f = open("4_Gbyte.txt", "r") # file with 100 million random integers

n = 0
while True:
    print(n)
    print(psutil.virtual_memory()[3] // 1048576, "Mb")  # physical memory usage
    print("Difference:1 ",psutil.virtual_memory()[3] // 1048576 - ram_before, "Mb")  # physical memory usage
    line = f.readline(4_000_000) # Size of one file
    line = line.split()
    if line:
        for i in range(len(line)):
            line[i] = int(line[i])
        line.sort()
        for i in range(len(line)):
            line[i] = str(line[i])    
        fstr = f"files/file_N_{n}.txt"
        file = open(fstr, "w")
        for i in range(len(line)):
            file.write(line[i])    
            file.write("\n")
        file.close()        
        n += 1

    else:
        break

ram_after = psutil.virtual_memory()[3] // 1048576
print(ram_before, "Mb")  # physical memory usage
print(ram_after, "Mb")  # physical memory usage
print("Difference:3 ",psutil.virtual_memory()[3] // 1048576 - ram_before, "Mb")  # physical memory usage

f.close()

print()
print()

a = open("sorted.txt", "a") # file with 1 bilion sorted integers from range[0; 120]

ls = []
for i in range(n):
    ls.append(-1)
ls_links = []
for i in range(n):
    ls_links.append(0)

for i in range(n):
    ls_links[i] = open(f"files/file_N_{i}.txt", "r")
    var = ls_links[i].readline()        
    if var:
        ls[i] = var[:-1]
    else:
        ls[i] = None

for i in range(n):
    ls[i] = int(ls[i])
print("Difference:5 ",psutil.virtual_memory()[3] // 1048576 - ram_before, "Mb")  # physical memory usage

can_loop = True
while can_loop:
    can_loop = False
    minn = 1_000_000_000
    minn_index = -1

    for i in range(n):
        if ls[i]:
            if ls[i] < minn:
                minn = ls[i]
                minn_index = i
                can_loop = True
        else:
            continue        
    if can_loop:    
        a.write(str(minn) + " ")
        var = ls_links[minn_index].readline()        
        if var:
            ls[minn_index] = int(var[:-1])
        else:
            ls[minn_index] = None
print("Difference:7 ",psutil.virtual_memory()[3] // 1048576 - ram_before, "Mb")  # physical memory usage

for i in range(n):
    ls_links[i].close()
    
a.close()

