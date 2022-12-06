from utility.api import get_input


def part_1(input):
    sett=set()
    for j,_ in enumerate(input):
        i=0
        sett=set()
        while i<4:
            if input[j+i] not in sett:
                sett.add(input[j+i])
            
            if len(sett)==4:
                
                print(j+i+1)
                return j+i+1
            i+=1
    
def part_2(input):
    sett=set()
    for j,_ in enumerate(input):
        i=0
        sett=set()
        while i<14:
            if input[j+i] not in sett:
                sett.add(input[j+i])
            if len(sett)==14:
                print(j+i+1)
                return j+i+1
            i+=1
    

def parse_input(input):
    return input[:-1]
    
if __name__=="__main__":
    input=get_input(year=2022, day=6)
    input=parse_input(input)
    part_1(input)

    part_2(input)
