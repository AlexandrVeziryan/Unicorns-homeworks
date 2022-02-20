import sys
inFile = sys.argv[1]
with open(inFile,'r') as i:
    lines = i.readlines()
for i in range(len(lines)):
    if lines[i][-1] == "\n":
        lines[i] = lines[i][:-1]


memory = {}  #  {name : [type, value]}
data_types = ["int", "str"]
numbers = "0123456789"
number_of_lines = 0
condition_keys = ["==","!=",">=","<=",">","<",]
nerdrvac_ifer = 0
e = 0


def multiple(a, b):
    return a * b

def devide(a, b):
    return a // b

def arythmetic_operations(ls):
    # + a + 3 + 6 + a - 3
    
    if ls[-1] == "+" or ls[-1] == "-" or ls[-1] == "*" or ls[-1] == "/":
        return False,
    for i in ls[::2]:
        if i != "+" and i != "-" and i != "*" and i != "/":
            return False,
    for i in ls[1::2]:
        if i == "+" or i == "-" or i == "*" or i == "/":
            return False,
        if i[0] == "\"" and i[-1] == "\"":
            return False,
    summ = 0
    if "*" in ls or "/" in ls: # multiple or devide
    
        lenn = len(ls)
        ii = 0
        while ii < lenn:
            if ls[ii] == "*":
                if ls[ii - 1].isdigit() and ls[ii + 1].isdigit():
                    summ = multiple(int(ls[ii - 1]), int(ls[ii + 1]))

                elif ls[ii - 1].isdigit() and ls[ii + 1] in memory and memory[ls[ii + 1]][0] == "int":
                    summ = multiple(int(ls[ii - 1]), memory[ls[ii + 1]][1])
                
                elif ls[ii + 1].isdigit() and ls[ii - 1] in memory and memory[ls[ii - 1]][0] == "int":
                    summ = multiple(memory[ls[ii - 1]][1], int(ls[ii + 1]))
                
                elif ls[ii + 1] in memory and memory[ls[ii + 1]][0] == "int" and ls[ii - 1] in memory and memory[ls[ii - 1]][0] == "int":
                    summ = multiple(memory[ls[ii - 1]][1], memory[ls[ii + 1]][1])
                    
                ls = ls[:ii - 1] + [str(summ)] + ls[ii + 2:]
                lenn -= 2
                ii -= 1
            elif ls[ii] == "/":
                if ls[ii - 1].isdigit() and ls[ii + 1].isdigit():
                    summ = devide(int(ls[ii - 1]), int(ls[ii + 1]))

                elif ls[ii - 1].isdigit() and ls[ii + 1] in memory and memory[ls[ii + 1]][0] == "int":
                    summ = devide(int(ls[ii - 1]), memory[ls[ii + 1]][1])
                
                elif ls[ii + 1].isdigit() and ls[ii - 1] in memory and memory[ls[ii - 1]][0] == "int":
                    summ = devide(memory[ls[ii - 1]][1], int(ls[ii + 1]))
                
                elif ls[ii + 1] in memory and memory[ls[ii + 1]][0] == "int" and ls[ii - 1] in memory and memory[ls[ii - 1]][0] == "int":
                    summ = devide(memory[ls[ii - 1]][1], memory[ls[ii + 1]][1])
                
                
                ls = ls[:ii - 1] + [str(summ)] + ls[ii + 2:]
                lenn -= 2
                ii -= 1
            ii += 1    

    res = 0
    i = 0
    while i < len(ls):
        plus = True
        if ls[i] == "-":
            plus = False
        i += 1    
        elem = str(ls[i])
        if elem.isdigit():
            if plus:
                res += int(elem)
            else:
                res -= int(elem)    
        else:
            if not elem in memory:
                return False,
            if memory[elem][0] != "int":
                return False,
            if plus:
                res += int(memory[elem][1])
            else:
                res -= int(memory[elem][1])        
        i += 1
    return True, res    

def compare(a, key, b):
    if key == "==":
        return a == b
    elif key == "!=":
        return a != b
    elif key == ">=":
        return a >= b
    elif key == "<=":
        return a <= b
    elif key == "<":
        return a < b
    else:
        return a > b
            
def execute_line(line):
    words = line.split()
    if len(words) == 0:
        return True
    if words[0] in data_types:
        if words[1] in memory:
            print(f"Error in line {number_of_lines} \nVariable was defined earlier")
            return False
        if len(words) == 2:
            memory[words[1]] = [words[0], None]
            return True
        if words[2] != "=":
            print("Invalid syntax")
            return False
        ls = words[3:]
        if ls[0][0] == "\"":
            if ls[0][-1] == "\"":
                memory[words[1]] = ["str", ls[0][1:-1]]
            elif len(ls) > 1:    
                end_is_checked = False
                summ = ls[0][1:]
                for word in ls[1:]:
                    if word[-1] == "\"":
                        end_is_checked = True
                        summ = summ + " " + word[:-1]
                    else:
                        summ = summ + " " + word
                if end_is_checked:
                    memory[words[1]] = ["str", summ]
                else:
                    print("Invalid syntax")
                    return False
            else:
                print("Invalid syntax")
                return False
            
        elif len(words) == 4:
            if words[3] in memory and words[0] == memory[words[3]][0]:
                memory[words[1]] = memory[words[3]]
            elif words[3].isdigit() and words[0] == "int":
                memory[words[1]] = [words[0], int(words[3])]
            # elif words[0] == "str" and words[3][0] == "\"" and words[3][-1] == "\"":
            #     memory[words[1]] = [words[0], words[3][1:-1]]
            else:
                print("Error7")                             ####
                return False
        else:
            arith_oper = arythmetic_operations(["+"] + words[3:]) 
            if arith_oper[0]:
                memory[words[1]] = [words[0], arith_oper[1]]    
            else:
                print("Error8")                             ####
                return False
        return True        
    
    elif words[0] == "tpel":
        ls = words[1:]
        if ls[0][0] == "\"":
            if ls[0][-1] == "\"":
                print(ls[0][1:-1])
            elif len(ls) > 1:    
                end_is_checked = False
                summ = ls[0][1:]
                for word in ls[1:]:
                    if word[-1] == "\"":
                        end_is_checked = True
                        summ = summ + " " + word[:-1]
                    else:
                        summ = summ + " " + word
                if end_is_checked:
                    print(summ)
                else:
                    print("Invalid syntax")
                    return False
            else:
                print("Invalid syntax")
                return False
        elif len(ls) == 1:
            if ls[0].isdigit():
                print(ls[0])
            # elif ls[0][0] == "\"" and ls[0][-1] == "\"":
            #     print(ls[0][1:-1])
            else:
                if not ls[0] in memory:
                    print("Error1")
                    return False
                print(memory[ls[0]][1])
        else:
            arith_oper = arythmetic_operations(["+"] + ls) 
            if arith_oper[0]:
                print(arith_oper[1]) 
            else:
                print("Error2")                             ####
                return False      
        return True        
        
    elif words[0] in memory:
        if len(words) == 1:
            return True
        if words[1] != "=":
            print("Error3")
            return False
        ls = words[2:]
        if ls[0][0] == "\"":
            if ls[0][-1] == "\"":
                memory[words[0]] = ["str", ls[0][1:-1]]
            elif len(ls) > 1:    
                end_is_checked = False
                summ = ls[0][1:]
                for word in ls[1:]:
                    if word[-1] == "\"":
                        end_is_checked = True
                        summ = summ + " " + word[:-1]
                    else:
                        summ = summ + " " + word
                if end_is_checked:
                    memory[words[0]] = ["str", summ]
                else:
                    print("Invalid syntax")
                    return False
            else:
                print("Invalid syntax")
                return False
            
        elif len(ls) == 1:
            if ls[0].isdigit() and memory[words[0]][0] == "int":
                memory[words[0]] = ["int", int(ls[0])]
            # elif ls[0][0] == "\"" and ls[0][-1] == "\"":
            #     memory[words[0]] = ["str", ls[0][1:-1]]    
            elif ls[0] in memory and memory[words[0]][0] == memory[ls[0]][0]:
                memory[words[0]] = memory[ls[0]]
            else:
                print("error4")    
                return False
        else:
            arith_oper = arythmetic_operations(["+"] + ls) 
            if arith_oper[0]:
                memory[words[0]] = ["int", arith_oper[1]]
            else:
                print("Error5")                             ####
                return False
        return True        

    elif words[0] == "if":
        if not if_impl(words, line):
            print("Error 11")
            return False
        return True    

    elif words[0] == "cikl":
        if not cikl_impl(words, line):
            print("Error 12")
            return False
        return True    


    else:
        print("Error666")
        return False

def cikl_impl(words, line):
    global e
    ident_count = 0
    cikl_e = 0
    for letter in line:
        if letter != " ":
            break
        else:
            ident_count += 1
    if ident_count % 4 != 0:

        return False
    ident_count //= 4
    ident_count += 1 
    
    condition_passed = False
    if words[1][0] != "\"": # Digits
        summ = [words[1]]
        res_1 = 0
        res_2 = 0
        i = 2
        condition_key = ""
        while i < len(words):
            
            if not words[i] in condition_keys:
                summ.append(words[i])
            else:
                condition_key = words[i]
                i += 1
                break    
            i += 1 

        if not condition_key:
            print("Error5rr")                             ####
            return False   
        
        arith_oper = arythmetic_operations(["+"] + summ) 
        if arith_oper[0]:
            res_1 = arith_oper[1]
        else:
            print("Error55")                             ####
            return False
        summ = []
        while i < len(words):
            summ.append(words[i])  
            i += 1
        arith_oper = arythmetic_operations(["+"] + summ) 
        if arith_oper[0]:
            res_2 = arith_oper[1]
        else:
            print("Error555")                             ####
            return False 
        if compare(res_1, condition_key, res_2):
            condition_passed = True
    elif len(words) == 4: # Strings

        if words[2] == "==" and words[1] == words[3]:
            condition_passed = True
        elif words[2] == "!=" and words[1] != words[3]:
            condition_passed = True
        elif words[2] == "<=" and words[1] <= words[3]:
            condition_passed = True
        elif words[2] == ">=" and words[1] >= words[3]:
            condition_passed = True
        elif words[2] == ">" and words[1] > words[3]:
            condition_passed = True
        elif words[2] == "<" and words[1] < words[3]:
            condition_passed = True
    e += 1
    cikl_e += 1
    if e < len(lines) - 1: 
        line = lines[e]
    if condition_passed:
        executed_lines_into_if = 0
        while True:
            if line[:4 * ident_count] == "    " * ident_count: 
                execute_line(line)
                executed_lines_into_if += 1
                if e == len(lines) - 1:
                    break 
                e += 1 
                cikl_e += 1
                line = lines[e] 
            else:
                cikl_e -= 1
                e -= 1 
                line = lines[e] 
                break    

        if executed_lines_into_if < 1:
            print("Error8")
            return False
        e = e - cikl_e        
        line = lines[e] 
        words = line.split()
        cikl_impl(words, line)
        # e += 1
        # line = lines[e]
        return True 

    else:
        passed_lines = 0
        while True:
            if line[:4 * ident_count] == "    " * ident_count:
                passed_lines += 1
                e += 1
                line = lines[e]  
                if e == len(lines) - 1: 
                    break
            else:
                e -= 1
                line = lines[e]
                break    
        if passed_lines < 1:
            print("Error: <<cikl>> must have at least one indent line")
            return False
        return True    

def if_impl(words, line):
    global e
    ident_count = 0
    for letter in line:
        if letter != " ":
            break
        else:
            ident_count += 1
    if ident_count % 4 != 0:

        return False
    ident_count //= 4
    ident_count += 1   
    
    condition_passed = False
    if words[1][0] != "\"": # Digits
        summ = [words[1]]
        res_1 = 0
        res_2 = 0
        i = 2
        condition_key = ""
        while i < len(words):
            
            if not words[i] in condition_keys:
                summ.append(words[i])
            else:
                condition_key = words[i]
                i += 1
                break    
            i += 1 

        if not condition_key:
            print("Error5")                             ####
            return False   
        
        arith_oper = arythmetic_operations(["+"] + summ) 
        if arith_oper[0]:
            res_1 = arith_oper[1]
        else:
            print("Error55")                             ####
            return False
        summ = []
        while i < len(words):
            summ.append(words[i])  
            i += 1
        arith_oper = arythmetic_operations(["+"] + summ) 
        if arith_oper[0]:
            res_2 = arith_oper[1]
        else:
            print("Error555")                             ####
            return False 
        if compare(res_1, condition_key, res_2):
            condition_passed = True
    elif len(words) == 4: # Strings

        if words[2] == "==" and words[1] == words[3]:
            condition_passed = True
        elif words[2] == "!=" and words[1] != words[3]:
            condition_passed = True
        elif words[2] == "<=" and words[1] <= words[3]:
            condition_passed = True
        elif words[2] == ">=" and words[1] >= words[3]:
            condition_passed = True
        elif words[2] == ">" and words[1] > words[3]:
            condition_passed = True
        elif words[2] == "<" and words[1] < words[3]:
            condition_passed = True


    e += 1
    line = lines[e]
    if condition_passed:
        executed_lines_into_if = 0
        while True:
            if line[:4 * ident_count] == "    " * ident_count:
                execute_line(line)
                executed_lines_into_if += 1
                if e <= len(lines) - 1:
                    break 
                e += 1 
                line = lines[e] 
            else:
                e -= 1 
                line = lines[e] 

                break     
        if executed_lines_into_if < 1:
            print("Error8")
            return False
        # e += 1
        # line = lines[e]
        return True 


    else:
        passed_lines = 0
        while True:
            if line[:4] == "    ":
                e += 1
                line = lines[e]  
                passed_lines += 1
            else:
                e -= 1
                line = lines[e]
                break    
        if passed_lines < 1:
            print("Error: <<if>> must have at least one indent line")
            return False
        return True    


if inFile[-3:] == ".eg":
    while e < len(lines):
        line = lines[e]  
        number_of_lines += 1  
        words = line.split()
        
        if len(line) > 0:
            if line[0] == " " and len(line.split()) > 0:
                print("Error9")
                break
            
        if execute_line(line):
            e += 1 
        else:
            break    

    # print()
    # print("Memory`")
    # print()
    # for elem in memory:
    #     print(elem, "\t", memory[elem])
else:
    print("Error: enter files with extension .eg")        
