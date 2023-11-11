f=open("TestCasesMaths.txt","r")
read=f.read().split('\n\n')
for i in range(len(read)):
    read[i]=read[i].split('\n')
for i in range(len(read)):
    for j in range(len(read[i])):
        read[i][j]=read[i][j].split(' ')
for i in range(len(read)):
    for j in range(len(read[i])):
        for k in range(len(read[i][j])):
            read[i][j][k]=float(read[i][j][k])
f.close()               
def rounder(list):
    for i in range(len(list)):
        list[i]=round(list[i])
    return(list) 
def Soultion_of_matrix(matrix):
    def rearrange_matrix(matrix):
        def czbne(l):
            count=0
            for i in l:
                if i==0:
                    count+=1
                elif i!=0:
                    break  
            return count
        while True:
            swap=0
            for i in range(len(matrix)-1):
                if czbne(matrix[i])>czbne(matrix[i+1]):
                    matrix[i],matrix[i+1]=matrix[i+1],matrix[i]
                    swap+=1
                elif czbne(matrix[i])==czbne(matrix[i+1]):
                    continue 
            if swap==0:
                break
        return(matrix)     
    a=rearrange_matrix(matrix)
    for i in range(len(a)):
        for j in range(len(a[i])):  
            if round(a[i][j],8)!=0:
                a[i]=[k/a[i][j] for k in a[i]]
                for k in range(i+1,len(a)):
                    if a[k][j]!=0:
                        a[k]=[a[k][l]-a[i][l]*a[k][j] for l in range(len(a[k]))]
                break
            else:
                a[i][j]=0

    a=rearrange_matrix(a)      
    for i in range(len(a)-1,0,-1):
        for j in range(len(a[i])):
            if a[i][j]!=0:
                for k in range(i-1,-1,-1):
                    if a[k][j]!=0:
                        a[k]=[a[k][l]-a[i][l]*a[k][j] for l in range(len(a[k]))]
                break       
    free_varb=[]
    for i in range(len(a)):
        count=0
        for j in range(len(a[i])):
            if a[i][j]!=0:
                if count==0:
                    count+=1
                    continue
                else:
                    count+=1
                    free_varb.append(j+1)
    free_varbs=list(set(free_varb))   
    free_varbs.sort()             
    eqn=dict().fromkeys(free_varbs)
    for keys in eqn:
        eqn[keys]=[0]*(len(a[0]))
    for keys in eqn:
        eqn[keys][int(keys)-1]=float(1)
        
    for i in range(len(a)):
        c=0
        for j in range(len(a[i])):
            if a[i][j]!=0:
                if c==0:
                    c+=1
                    pp=j
                    continue
                else:
                    eqn[j+1][pp]=(-1*a[i][j])  
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==0:
                a[i][j]=0.0

    s=""
    sss=""
    for i in range(len(a)):
        sss+=f"{a[i]} \n "
    for b,x in enumerate(eqn):
        if b==len(eqn)-1:
            s+=(f"x{x} {eqn[x]}")
        else:    
            s+=(f"x{x} {eqn[x]} + ")
    if s=="":    
        mm=[0.0]*len(a[0])
        s+=f"{mm}"
        return(s,sss)
    else:      
        return(s,sss)    
        
ss=""
f2=open("OutputMaths.txt","w")
for i in read:
    f2.write(f"The Row Reduced Echlon form of given Matrix is \n {Soultion_of_matrix(i)[1]} \n The Solution of Matrix is \n {Soultion_of_matrix(i)[0]} \n\n")
    print(Soultion_of_matrix(i)[0])
    print("**********************************************************************************************************\n")
    f2.write("**********************************************************************************************************\n")
