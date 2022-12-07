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





def parse_input(input):
    root=tree_node(size=0,name="/",father=None,is_folder=True)
    input=input.split("\n")[1:-1]
    for line in input:
        line=line.split(" ")
        if line[0]== "$" and line[1]=="ls":
            continue

        if line[0]== "$" and line[1]=="cd" and  line[2]=="..":
            root=root.father
            continue
        
        if line[0]== "$" and line[1]=="cd":
            for son in root.sons:
                if son.name==line[2]:
                    root=son
                    break
            continue
        
        if line[0]=="dir":
            son=tree_node(size=0,name=line[1],father=root,is_folder=True) 
            root.sons.append(son)
            
            continue

        son=tree_node(size=int(line[0]),name=line[1],father=root,is_folder=False) 
        root.sons.append(son)
    while root.father!=  None:
        root=root.father
    return root


def compute_dim_folders(root):
    if root.sons==[]:
        return root.size
    tot=0
    for son in root.sons:
        tot+=compute_dim_folders(son)
    root.size=tot
    return tot


def part_1(root):
    out=[0]
    def count_fold(root):
        if root.size <= 100000 and root.is_folder:
            out[0]+=root.size
        if root.sons==[]:
            return
        for son in root.sons:
            count_fold(son)        
        return
    compute_dim_folders(root)
    count_fold(root)
    print(out[0])
    return out[0]

    
    
def part_2(root):
    space_occupied=compute_dim_folders(root)
    li=[]
    
    def get_folders_dim(root):
        if root.is_folder:
            li.append(root.size)
       
       
        if root.sons==[]:
            return
        for son in root.sons:
            get_folders_dim(son)        
        return

    
    get_folders_dim(root)
    li.sort()
    
    total_sapce=70000000
    free_space=  total_sapce-space_occupied
    for dim in li:
        if  free_space+dim>= 30000000:
            print(dim)
            return dim

    
if __name__=="__main__":
    input=get_input(year=2022, day=7)
    print([input])
    root=parse_input(input)
    part_1(root)
    root=parse_input(input)
    part_2(root)