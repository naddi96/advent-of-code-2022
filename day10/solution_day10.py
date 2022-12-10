from utility.api import get_input


def part_1(input):
    cicle=0
    register=1
    cicles=[220,180,140,100,60,20]
    summ=0
    time={'addx':2,"noop":1}
    for do in input:


        for i in range(time[do[0]]):
            cicle+=1

            if cicle==cicles[-1]:
                summ+= (cicles[-1]*register)
                cicles.pop()
            if i==1:
                register+=do[1]

            if cicles==[]:
                print(summ)
                return summ





def part_2(input):
    display=[[" " for _ in range(40)] for _ in range(6) ]
    cicle=0
    sprite=1
    time={'addx':2,"noop":1}
    column=0
    for do in input:
        for i in range(time[do[0]]):
            row=cicle%40
            if sprite+1>=row and  sprite-1<=row:
                display[column][row]="█"

            if i==1:
                sprite+=do[1]

            cicle+=1
            if cicle%40==0:
                column+=1
    l=""
    for d in display:
        l=l+"".join(d)+"\n"
    print(l)
    return l

def parse_input(input):
    input=input.split("\n")[:-1]
    
    li=[]
    
    for el in input:
        el=el.split(" ")
        if el[0]=="noop":
            li.append((el[0],0))
        else:
            li.append((el[0],int(el[1])))
    
    return li
    

if __name__=="__main__":
    input=get_input(year=2022, day=10)
    print([input])
    input=parse_input(input)

    
    k=part_1(input)
    k=part_2(input)

