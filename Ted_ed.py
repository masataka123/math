import random
import sys
def f(a,b,c):
    while a+b+c>1:
        if a<=b and a<=c:
            a+=1
            b-=1
            c-=1
        elif b<=a and b<=c:
            a-=1
            b+=1
            c-=1
        elif c<=a and c<=b:
            a-=1
            b-=1
            c+=1
    return a,b,c

#for i in range(10):
    #a=random.randint(1,100)
   # b = random.randint(1, 100)
    #c = random.randint(1, 100)
    #print(a,b,c)
    #print(f(a, b, c))
print(43,33,24)
print(f(43,33,24))

N=26
L=[1,3,4]
dp=[0]*N
#dp[0]=0
dp[1]=0
for i in range(2,N):
    s=1
    for l in L:
        if 1<=i-l:
            s*=dp[i-l]
    dp[i]=1-s
print(dp)
print(N)
p=N
while True:
    n=int(input())
    if p-n not in L:
        print("error")
        sys.exit()
    if n==0:
        print("lose")
        sys.exit()
    if n==1:
        print("win")
        sys.exit()
    s=1
    for l in L:
        if 1<= n-l and dp[n-l]==0:
            print(n-l)
            p=n-l
            s=0
            break
    if s==1:
        while True:
            l=random.randint(0,2)
            if 1<=n-L[l]:
                print(n-L[l])
                p=n-L[l]
                break