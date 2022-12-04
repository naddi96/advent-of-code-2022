from utility.api import get_input




def part_1(input):
    mapp={"A":"rock","B":"paper","C":"sci", "X":"rock","Y":"paper","Z":"sci"}
    cost={"rock":1,"sci":3,"paper":2}
    count=0
    for a,b in input:

        count+=cost[mapp[b]]

        if mapp[a]==mapp[b]:
            count+=3
            continue
        if mapp[a]=="rock" and mapp[b]=="paper":
            count+=6
            continue
        if mapp[a]=="paper" and mapp[b]=="sci":
            count+=6
            continue
        if mapp[a]=="sci" and mapp[b]=="rock":
            count+=6
            continue
    print(count)
    return count

def part_2(input):
    to_win={"A":"paper","B":"sci","C":"rock"}
    to_lose={"A":"sci","B":"rock","C":"paper"}
    cost={"rock":1,"sci":3,"paper":2}
    mapp={"A":"rock","B":"paper","C":"sci", "X":"rock","Y":"paper","Z":"sci"}
    count=0
    for a,b in input:
        if b=="X":
            count+=cost[to_lose[a]]
        if b=="Y":
            count+=cost[mapp[a]]+3
        if b=="Z":
            count+=cost[to_win[a]]+6
    print(count)
    return count
        
def parse_input(input):
    input=input.split("\n")
    input=[k.split(" ") for k in input]
    input=input[:-1]
    
    return input
if __name__=="__main__":
    input=get_input(year=2022, day=2 )
    input=parse_input(input)
    part_1(input)
    part_2(input)
