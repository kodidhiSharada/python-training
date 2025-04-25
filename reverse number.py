x=int(input("enter the number:"))
reverse=0
while(x>0):
    rem=x%10
    reverse=(reverse*10)+rem
    x=x//10
print(reverse)    
