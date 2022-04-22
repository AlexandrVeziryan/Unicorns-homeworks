def find_mean(ls):
    return sum(ls) / len(ls)

def find_median(ls):
    return ls[len(ls) // 2]

def find_mode(ls):
    lst = [0 for _ in range(ls[-1] + 1)]
    for i in ls:
        lst[i] += 1
    maxx = lst[1]
    mode = 0
    for i in range(2, len(lst)):
        if lst[i] > maxx:
            maxx = lst[i]
            mode = i
    return mode        


text = """In computer science and computer programming, a data type or simply type is an attribute of data
which tells the compiler or interpreter how the programmer intends to use the data. Most programming languages support 
basic data types of integer numbers (of varying sizes), floating-point numbers (which approximate real numbers), 
characters and Booleans. A data type constrains the values that an expression, such as a variable or a function, 
might take.This data type defines the operations that can be done on the data, the meaning of the data, 
and the way values of that type can be stored. A data type provides a set of values from 
which an expression (i.e. variable, function, etc.) may take its values.[1][2]"""

list_of_splitted_text = text.split()
ls = []
for word in list_of_splitted_text:
    ls.append(len(word))
ls.sort()


mean = find_mean(ls)
median = find_median(ls)
mode = find_mode(ls)

print("Mean   :", mean)
print("Median :", median)
print("Mode   :", mode)
       



