def max_num(num1=0,num2=2,num3=8):
    if num1>=num2 and num1>=num3:
        return num1 
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    
print(max_num())
    