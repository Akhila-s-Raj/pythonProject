str=input("Enter a string")
dict={}
for i in str:
    if i in dict:
        dict[i]=dict[i]+1
        
    else:
        dict[i]=1

for m,n in dict.items():
    print(m,n)


