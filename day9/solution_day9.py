from utility.api import get_input



'''


t...012..
...H..
......
......
......

......
...H...
HT..t..
......
......

......
.......
..T..HT..
.H.......
......

......
.....
..T..H..
..H...
......


......H.
...H..T.
..T......
......
......



'''

def move_up(head,tail):
    head=list(head)
    tail=list(tail)
     
    if head[0]==tail[0]:
        head[0]+=1
        return tuple(head),tuple(tail)

    head[0]+=1
    
    if head==tail:
        return tuple(head),tuple(tail)

    if abs(head[0] -tail[0])>1:
        tail[0]+=1
        tail[1]=head[1]

    return tuple(head),tuple(tail)
    
    


def move_down(head,tail):
    head=list(head)
    tail=list(tail)
     
    if head[0]==tail[0]:
        head[0]-=1
        return tuple(head),tuple(tail)

    head[0]-=1
    
    if head==tail:
        return tuple(head),tuple(tail)

    if abs(head[0]-tail[0])>1:
        tail[0]-=1
        tail[1]=head[1]

    return tuple(head),tuple(tail)

def move_left(head,tail):
    head=list(head)
    tail=list(tail)
     
    if head[1]==tail[1]:
        head[1]-=1
        return tuple(head),tuple(tail)

    head[1]-=1
    
    if head==tail:
        return tuple(head),tuple(tail)

    if abs(head[1]-tail[1])>1:
        tail[1]-=1
        tail[0]=head[0]

    return tuple(head),tuple(tail)



def move_right(head,tail):
    head=list(head)
    tail=list(tail)
     
    if head[1]==tail[1]:
        head[1]+=1
        return tuple(head),tuple(tail)

    head[1]+=1
    
    if head==tail:
        return tuple(head),tuple(tail)

    if abs(head[1]-tail[1])>1:
        tail[1]+=1
        tail[0]=head[0]

    return tuple(head),tuple(tail)

def part_1(input):
    head=(0,0)
    tail=(0,0)
    sett=set([tail])
    dictt={"U":move_up,"D":move_down,"L":move_left,"R":move_right}
    count=0
    for move in input:
        for _ in range(move[1]):
            head1,tail1=head,tail
            head,tail=  dictt[move[0]](head,tail)
            sett.add(tail)
        count+=1
            
        
    print(len(sett))
    





def move_up(list_tuple):
    head=list(head)
    tail=list(tail)
     
    if head[0]==tail[0]:
        head[0]+=1
        return tuple(head),tuple(tail)

    head[0]+=1
    
    if head==tail:
        return tuple(head),tuple(tail)

    if abs(head[0] -tail[0])>1:
        tail[0]+=1
        tail[1]=head[1]

    return tuple(head),tuple(tail)
    


def move_tail(head,tail):
    head=list(head)
    tail=list(tail)





    if abs(head[1]-tail[1])>1 and abs(head[0]-tail[0])>1:
        if abs(head[1]-(tail[1]+1))==1 and abs(head[0]-(tail[0]+1))==1:
            tail[1]+=1
            tail[0]+=1
        else:
            tail[1]-=1
            tail[0]-=1
        return tuple(tail) 


    if abs(head[1]-tail[1])>1:
        if abs(head[1]-(tail[1]+1))==1:
            tail[1]+=1
        else:
            tail[1]-=1
        
        tail[0]=head[0]
        return tuple(tail) 


    if abs(head[0]-tail[0])>1:
        if abs(head[0]-(tail[0]+1))==1:
            tail[0]+=1
        else:
            tail[0]-=1
        tail[1]=head[1]
        
    return tuple(tail) 
    

        


def part_2(input):
    snake=[(0,0) for i in range(10)]
    
    sett=set([(0,0)])
    m={"U":(1,0),"D":(-1,0),"L":(0,-1),"R":(0,1)}
    for move in input:
        for _ in range(move[1]):
            
            snake[0]=(snake[0][0]+m[move[0]][0],snake[0][1]+m[move[0]][1])

            for i in range(len(snake)-1):
                head=snake[i]
                tail=snake[i+1]
                
                snake[i+1]=  move_tail(head,tail)

            '''
            k=[["." for i in range(60)] for _ in range(60)] 
            
            k[snake[0][0]][snake[0][1]]=f"H"
            
            for j,i in enumerate(snake[1:]):
                k[i[0]][i[1]]=str(j+1)
            for i in reversed(k):
                print("".join(i))
            print(f"----------- moveee {move}")
            '''
                
        
            sett.add(snake[-1])
            
    print(len(sett))



def parse_input(input):
    input=input.split("\n")[:-1]
    li=[]
    for el in input:
        s=el.split(" ")
        li.append([s[0], int(s[1])]) 
    return li

    
if __name__=="__main__":
    input=get_input(year=2022, day=9)
    input=parse_input(input)
    part_2(input)

