import math
        
def solution(n):
    check={int(n)}
    steps=0
    while True:
        newcheck=set()
        for num in check:
            if num==1:
                return steps
            elif num%2==0:
                newcheck.add(num//2)
            else:
                newcheck.add(num-1)
                newcheck.add(num+1)
        steps+=1
        check=set(newcheck)
        
        