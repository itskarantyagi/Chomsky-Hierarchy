#funtion below is to check for type-0
def type0(p,lhs):
    #n=p*2
    for n in range(len(lhs)):
        if((lhs[n]=="A")or(lhs[n]=="B")or(lhs[n]=="S")):
            return 0
    return 9

#function below is to check for type-1
def type1(p,lhs,rhs,l,r):
    j=0
    k=0
    for q in range(len(lhs)):
        if(lhs[q]=="S"):
            j=j+1

    for t in range(len(rhs)):
        if(rhs[t]=="S"):
            k=k+1

    if((j==0)and(k!=0)):
        return 0
    
    if((lhs=="S")and(rhs=="l")):  #this will be applicable only for the first production
        return 1
    if(l<=r):
        return 1
        
        
def type2(l):
    if(l==1):
        return 2
    else:
        return 1

def type3_LL(p,rhs,lhs):
    #m=(p*2)+1
    m=1
    counter=0
    for m in range(len(rhs)):
        if((rhs[m]=="A")or(rhs[m]=="B")or(rhs[m]=="S")):
            counter=counter+1
    if(counter==0):
        return 3
    else:
        return 2
            

def type3_RL(p,rhs):
    #b=(p*2)+1
    b=1
    counter1=0
    for b in range(len(rhs)):
        if((rhs[b]=="A")or(rhs[b]=="B")or(rhs[b]=="S")):
            counter1=counter1+1
            
    if((counter1==1)and((rhs[len(rhs)]!="A")or(rhs[len(rhs)]!="B")or(rhs[len(rhs)]!="S"))):
        return 3
    else:
        return 2

s=int (input("Enter the Number of production functions : "))  #input number of production functions
symb=input("Enter start symbol: ")
pfunc=[]
type=4
i=0

#flag="false"
for i in range(s):
    pfunc.append(input("Enter LHS of "+str(i)+"th/st production function : "))
    pfunc.append(input("Enter RHS of "+str(i)+"th/st production function : "))
    l_len=len(pfunc[i])
    r_len=len(pfunc[i+1])
    min=type0(i,pfunc[i])
    if(min==0):
        min=type1(i,pfunc[i],pfunc[i+1],l_len,r_len)
    if(min==1):
        min=type2(l_len)
    if(min==2):
        if((pfunc[i+1][0]=="A")or(pfunc[i+1][0]=="B")or(pfunc[i+1][0]=="S")):
            min=type3_LL(i,pfunc[i+1],pfunc[i])
        elif((pfunc[i+1][0]=="a")or(pfunc[i+1][0]=="b")or(pfunc[i+1][0]=="l")):
            min=type3_RL(i,pfunc[i+1])
    continue
if((min==0)or(min==1)or(min==2)or(min==3)):
    print("Type is :"+str(min))
else:
    print("No type")


