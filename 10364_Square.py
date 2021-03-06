'''
Created on Aug 11, 2016

@author: Md. Rezwanul Haque
'''
import sys
#from numpypy import *
from queue import Empty
from _ast import Bytes
INF = 1<<31

def solve(N,sides):
    def calc(state, side):
        s = 0
        for i in range(N):
            s += sides[i]
        return s-side*sideL
    
    def can(side,state):
        left = calc(state, side)
        if left == sideL:
            return can(side+1, state)
        elif side == 4:
            return 1
        elif dp[side,state]!=-1:
            return dp[side,state]
        else:
            result = 0
            for i in range(N):
                if not (state & (1<<i)) and left + sides[i] <= sideL:
                    result |= can(side, state | (1<<i))
                dp[side,state] = result
                return result
    
    #N,sides = par
    s = sum(sides)
    if s%4 !=0:
        return 'no'
    sideL = s//4
    dp = Empty((4, 1 << 21), dtype =Bytes)
    dp.fill(-1)
    if can(0, 0):
        return 'yes'
    else:
        return 'no'
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        row = list(map(int,input().split()))
        N = row[0]
        #print(N)
        sides = row[1:]
        #print(sides)
        
        print(solve(N,sides))
            