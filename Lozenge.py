n = int(input("Please Enter Number: "))
r = 0

while r<n :
    j =1
    r+=1
    while j <= n-r :
        print(end='')
        j+=1
    k = 1
    while k <= 2*r-1 :
        print(end='*')
        k+=1
    print()
r = 0
while r < n :
    r+=1
    j = 1
    while j <= r :
        print(end='')
        j+=1
    k = 1
    while k<=2*(n-r)-1 :
        print(end='*')
        k+=1
    print()                    
 
 
 
 
 
 
 
 
 
 
# for i in range(n):
#     print(' * ' * (i+1))
