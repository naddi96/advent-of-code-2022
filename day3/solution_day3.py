import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from utility.api import get_input


def getvalue(c):
    if c>="a" and c<="z":
        return ord(c)-9#6
    if c>="A" and c<="Z":
        return ord(c)-38


def part_1(input):
    summ=0
    for el in input:
        sett=set()
        for char in el[:len(el)//2]:
            sett.add(char)
        for char in el[len(el)//2:]:
            if char in sett:
                 summ+=getvalue(char)
                 break
            
    print(summ)
    return summ

def part_2(input):
    
    sett1=[set(),set(),set()]
    c=0
    summ=0
    for el in input:
        if c<3:
            for char in el:
                sett1[c].add(char)
            c=c+1
        if c==3:
            c=0
            el1=list(sett1[0].intersection(sett1[1]).intersection(sett1[2]))
            sett1=[set(),set(),set()]
            summ+=getvalue(el1[0])

    print(summ)
    return summ



def parse_input(input):
    #print([input])
    input=input.split("\n")
    input=input[:-1]
    return input

if __name__=="__main__":
    input=get_input(year=2022, day=3 )
    input=parse_input(input)
    part_1(input)
    part_2(input)
    
