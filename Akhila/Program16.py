n=int(input("Enter the Number of Elements : "))
print("Enter the elements")
list=[]
for i in range(0,n):
    ele=int(input())
    if(ele>100):
        ele="over"
        list.append("over")
    else:
        list.append(ele)
print(list)
