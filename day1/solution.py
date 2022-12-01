import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from utility.api import get_input


def solution_problem1(li):
    maxx=float("-inf")
    current=0
    for el in li:
        if el=="":
            current=0
            continue
            
        current+=int(el)
        maxx=max(current,maxx)
    return maxx

def solution_problem2(li):
    maxx1=float("-inf")
    maxx2=float("-inf")
    maxx3=float("-inf")
    current=0
    for el in li:
        if el=="":
            current=0
            continue
        current+=int(el)
        if maxx1<current:
            maxx3=maxx2
            maxx2=maxx1
            maxx1=current
            continue

        if maxx2<current:
            maxx3=maxx2
            maxx2=current
            continue
            
        if maxx3<current:
            maxx3=current
            continue
            
         
    return maxx3+maxx1+maxx2


if __name__=="__main__":
    input=get_input(year=2022, day=1)
    input=input.split("\n")
    k=solution_problem1(input)
    k=solution_problem2(input)
    print(k)