def evenstr(x):
    p=[]
    count=0
    for i in x:
        if(len(i)%2==0):
            p.append(i)
            count=count+1
    if(count>0):
        print(f'The number of even string is {count} and string :{p}')
    else:
        print("No even string available!")

x=[]
for i in range(5):
    y=input(f"Enter string:")
    x.append(y)    
evenstr(x)    
