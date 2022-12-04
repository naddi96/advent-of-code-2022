import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from utility.api import get_input



'''
a0--a1
  b0--b1

   a0--a1
b0---b1

a0------a1
   b0-b1

'''
def overlapp(a,b):
    if a[0]<=b[0] and a[0]<=b[1] and a[1]>=b[0] and a[1]<=b[1]:
        return True

    if a[0]>= b[0] and a[0]<=b[1] and a[1]>=b[0] and a[1]>=b[1]:
        return True
    
    if a[0]<=b[0] and a[1]>=b[1] or a[0]>=b[0] and a[1]<=b[1] or a==b:
        return True
    

    return False

         
def part_2(input):
    count=0
    for  el,b in input:
        if  overlapp(el,b):
            count+=1
    
    print(count)
    return count


def part_1(input):
    count=0
    for  el,b in input:

        if  el[0]<=b[0] and el[1]>=b[1] or el[0]>=b[0] and el[1]<=b[1]:
            count+=1
    print(count)
    return count


if __name__=="__main__":
    input=get_input(year=2022, day=4 )
    input=input.split("\n")[:-1]
    input=[ [ [int(l) for l in  k.split("-")] for k in i.split(",")] for i in input]


    part_1(input)
    part_2(input)