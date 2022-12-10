from utility.api import get_input




class tree_node:

    def __init__(self,size,name,father,is_folder) -> None:
        self.sons=[]
        self.size=size
        self.name=name
        self.father=father
        self.is_folder=is_folder

    def __str__(self):
        return f"{self.name} ... {self.size} sons: {[k.name for k in self.sons ]}"





def is_visible(i,j,input):
    
    el=input[i][j]
    visible =True
    
    for k in range(i+1,len(input)):
        if el<= input[k][j]:
            visible=False
    
    if visible:
        return visible


    visible =True
    for k in range(0,i):
        if el<= input[k][j]:
            visible=False
    
    if visible:
        return visible
    visible=True
    for k in range(j+1,len(input[0])):
        if el<= input[i][k]:
            visible=False

    if visible:
        return visible

    visible=True
    for k in range(0,j):
        if el<= input[i][k]:
            visible=False

    return visible


def part_1(input):
    num_visible= len(input)*2 + (len(input[0])-2)*2
    for i in range(1,len(input)-1):
        for j in range(1,len(input)-1):
            if is_visible(i,j,input):
                num_visible+=1
    print(num_visible)
    return num_visible
    

def compute_score(i,j,input):
    up=0
    el=input[i][j]
    for k in range(i+1, len(input)):
        if el <= input[k][j]:
            up+=1
            break
        up+=1

    down=0
    for k in reversed(range(0, i)):
        if el <= input[k][j]:
            down+=1
            break
        down+=1

    right=0
    for k in range(j+1, len(input[0])):
        if el <= input[i][k]:
            right+=1
            break
        right+=1
    
    left=0
    for k in reversed(range(0, j)):
        if el <= input[i][k]:
            left+=1
            break
        left+=1

    return left*down*up*right

    


def part_2(input):
    maxx=float("-inf")
    
    for i in range(1,len(input)-1):
        for j in range(1,len(input)-1):
            maxx=max(maxx,compute_score(i,j,input))
    print(maxx)
    return maxx




def parse_input(input):
    input=input.split("\n")[:-1]
    li=[]
    for el in input:
        k=[]
        for char in el:
            k.append( int(char))
        li.append(k)
    return li




    
if __name__=="__main__":
    input=get_input(year=2022, day=8)
    input=parse_input(input)

    part_1(input)
    part_2(input)
