

from utility.api import get_input


def part_1(li):
    maxx=float("-inf")
    current=0
    for el in li:
        if el=="":
            current=0
            continue
            
        current+=int(el)
        maxx=max(current,maxx)
    return maxx

def part_2(li):
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

def parse_input(raw_text):
    #print([raw_text])
    return raw_text.split("\n")[:-1]

if __name__=="__main__":
    input=get_input(year=2022, day=1)
    input=parse_input(input)
    k=part_1(input)
    k=part_2(input)
    print(k)

