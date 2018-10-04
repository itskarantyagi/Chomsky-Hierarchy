#funtion below is to check for type-0
def type0(lhs):
    for n in range(len(lhs)):
        if((lhs[n]=="A")or(lhs[n]=="B")or(lhs[n]=="S")):
            return 0
    return 9

#function below is to check for type-1
def type1(SL,lhs,rhs,l,r):                              #return SL and type
    Sleft  = False
    SRight = False
    lRight = False
    
    if(l>r):
        return SL, 0
    print (1)
    for q in range(len(lhs)):
        if(lhs[q]=="S"):
            Sleft = True
    print (2)
    for t in range(len(rhs)):
        if(rhs[t]=="l"):
            lRight = True
        if(rhs[t]=="S"):
            SRight = True
    print (3)
    if (Sleft and lRight):
        return True, 1
    print (4)
    if (Sleft == False and SRight== True and SL == True):
        return SL, 0
    print (5)
    if (Sleft == True and SRight== True):
        return SL, 1
    return SL, 1

def type2(l):
    if(l==1):
        return 2
    else:
        return 1

def type3_LL(rhs,lhs):
    counter=0
    for m in range(1,len(rhs)):
        if((rhs[m]=="A")or(rhs[m]=="B")or(rhs[m]=="S")):
            return False,2
    return True,3
            

def type3_RL(rhs):
    counter1=0
    for b in range(1,len(rhs)):
        if((rhs[b]=="A")or(rhs[b]=="B")or(rhs[b]=="S")):
            counter1=counter1+1
    if(counter1==0):
        return False, 3
    if((counter1==1)and((rhs[len(rhs)]!="A")or(rhs[len(rhs)]!="B")or(rhs[len(rhs)]!="S"))):
        return True,3
    else:
        return False,2

s=int (input("Enter the Number of production functions : "))  #input number of production functions
symb=input("Enter start symbol: ")
pfunc=[]
type=4
i=0
SL = False
LL= False
RL = True
#flag="false"
for i in range(s):
    pfunc.append(input("Enter LHS of "+str(i)+"th/st production function : "))
    pfunc.append(input("Enter RHS of "+str(i)+"th/st production function : "))
    l_len=len(pfunc[2*i])
    r_len=len(pfunc[2*i+1])
    min=type0(pfunc[2*i])
    if(min==9):
        break
    if(min==0):
        SL, min= type1(SL,pfunc[2*i],pfunc[2*i+1],l_len,r_len)
    if(min==1):
        min=type2(l_len)
    if(min==2):
        if(((pfunc[i*2+1][0]=="A")or(pfunc[i*2+1][0]=="B")or(pfunc[i*2+1][0]=="S"))and RL==False):
            LL ,min=type3_LL(pfunc[i*2+1],pfunc[i*2])
        elif(((pfunc[i*2+1][0]=="a")or(pfunc[i*2+1][0]=="b")or(pfunc[i*2+1][0]=="l"))and LL==False):
            RL ,min=type3_RL(pfunc[i*2+1])
    print ("min = " + str(min))
if((min==0)or(min==1)or(min==2)or(min==3)):
    print("Type is :"+str(min))
else:
    print("No type")
