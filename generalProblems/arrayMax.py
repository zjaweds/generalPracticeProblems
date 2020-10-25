arr=[]
print("Enter the number of elements")
n=int(input())
for i in range(n):
    print("Enter "+str(i+1)+"th of element")
    arr.append(int(input()))
print("Maximum number: "+str(max(arr)))
