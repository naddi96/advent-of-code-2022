from utility.api import get_input


def part_1(moves,stacks):
    for move in moves:
        for i in range (move[0]):
            el= stacks[move[1]].pop(0)
            stacks[move[2]].insert(0,el)
    out=""
    for k in range(1,len(stacks)+1):
            out=out+stacks[k][0]
    print(out)
    return out




def part_2(moves,stacks):
    for move in moves:
        tmp=[]
        for i in range (move[0]):
            el= stacks[move[1]].pop(0)
            tmp.append(el)
        stacks[move[2]]= tmp+stacks[move[2]]
    out=""
    for k in range(1,len(stacks)+1):
        out=out+stacks[k][0]
    print(out)
    return out


def parse_input(input):
    input=input.split("\n")[:-1]
    stacks={}
    k=0
    for line in input:
        if line[1]=="1":
            k=k+2
            break
        k=k+1
        i=1
        count=1
        while i< len(line):
            if line[i]!=" ":
                stacks[count]=  stacks.get(count,[])+ [line[i]]
            count+=1
            i=i+4
    moves=[]
    for line in input[k:]:
        l=line.split(" ")
        moves.append( [int(l[1]) , int(l[3]), int(l[5])] )
    return (moves,stacks)
    
if __name__=="__main__":
    input=get_input(year=2022, day=5)
    moves,stacks=parse_input(input)
    part_1(moves,stacks)
    moves,stacks=parse_input(input)
    part_2(moves,stacks)

