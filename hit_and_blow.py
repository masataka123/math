from itertools import product, permutations,combinations
import random
from collections import Counter
import sys
from copy import deepcopy
N=5
number=[i for i in range(10)]
#print(number)
L=[]
for i in permutations(number,N):
    L.append(i)

def hit_and_blow():
    print("0-9の数字を一つずつ使ったhit_and_blowです, 数字は3桁です")
    print("入力は???の形にしてください")
    s=random.randint(0,len(L))
    ans=L[s]
    #print(L[s])
    while True:
        solver()
        cor = input()
        hit,blow=checker(cor,ans)
        print(hit, 'hit',blow, "blow")
        if blow==N:
            print("正解です")
            sys.exit()
#hit_and_blow()

#def solver():
def solver():
    print("入力は? hit ? blowの形にしてください")
    trycount=0
    while True:
        if trycount==0:
            next = "".join(map(str, [i for i in range(N)]))
            print(next)
            A=L
            trycount += 1
            continue
        T=input().split()
        Hit=int(T[0])
        Blow=int(T[2])
        kouho=[]
        for cor in A:
            s,t=checker_net(cor,next)
            #print(s,t,cor)
            if Hit==s and Blow==t:
                kouho.append(cor)
        #print(kouho)
        if len(kouho)==1:
            print(kouho[0])
            #sys.exit()
        minimax=10**10
        for cor in kouho:
            state = [[0 for i in range(N+1)] for i in range(N+1)]
            for n in kouho:
                gijians="".join(map(str,n))
                s, t = checker_net(cor, gijians)
                state[s][t]+=1
            maxvalue=0
            for s in range(N+1):
                maxvalue=max(maxvalue, max(state[s]))
            if minimax>maxvalue:
                minimax=maxvalue
                next="".join(map(str,cor))
        #print(next, maxvalue, kouho,A)
        trycount+=1
        A=deepcopy(kouho)
        print(next)

def checker(cor,ans):
    ans=str(ans)
    blow = 0
    hit = 0
    for i in range(N):
        if int(ans[i]) == cor[i]:
            blow += 1
    for i in range(N):
        hit += ans.count(str(cor[i]))
    return hit, blow

def checker_net(cor,ans):
    ans=str(ans)
    blow = 0
    hit = 0
    for i in range(N):
        if int(ans[i]) == cor[i]:
            hit += 1
    for i in range(N):
        blow += ans.count(str(cor[i]))
    blow-=hit
    return hit, blow


def prob():
    prob=[0]*15
    for i in range(100):
        s = random.randint(0, len(L)-1)
        ans ="".join(map(str, L[s]))
        trycount = 0
        while True:
            if trycount==0:
                next = "".join(map(str, [i for i in range(N)]))
                #print(next)
                A=L
                trycount += 1
                nextans=[i for i in range(N)]
            else:
                Hit=hit
                Blow=blow
                kouho=[]
                for cor in A:
                    s,t=checker(cor,next)
                    if Hit==s and Blow==t:
                        kouho.append(cor)
                minimax=10**10
                for cor in kouho:
                    state = [[0 for i in range(N+1)] for i in range(N+1)]
                    for n in kouho:
                        gijians="".join(map(str,n))
                        s, t = checker(cor, gijians)
                        state[s][t]+=1
                    maxvalue=0
                    for s in range(N+1):
                        maxvalue=max(maxvalue, max(state[s]))
                    if minimax>maxvalue:
                        minimax=maxvalue
                        next="".join(map(str,cor))
                        nextans=cor
                trycount+=1
                A=deepcopy(kouho)
                #print(next)
            hit,blow=checker(nextans,ans)
            #print(hit, 'hit',blow, "blow")
            if blow==N:
                #print(trycount,ans,"正解です")
                #print(trycount)
                prob[trycount]+=1
                break
                #sys.exit()
    print(prob)
    return