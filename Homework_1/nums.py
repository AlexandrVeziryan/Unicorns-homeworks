nums = "0123456789"
res = []
while True:
    num = input("Enter a number: ")
    if num == "done" and len(res) != 0:
        print(sum(res), len(res), sum(res) / len(res))
        break    
    else:
        can_append = True
        for i in num:
            if not i in nums:
                print("Invalid input")    
                can_append = False
        if can_append:
            res.append(int(num))        
