import random
inc=1
num=int(input("\nEnter the number whose square root is to be calculated(Integer only):\t"))
# I have not considered any exception handling
print("\nMore iterations means more accuracy\nBut that increases the Complexity:")
iterations=int(input("Enter desired iterations(integer only): "))
for j in range(num):
    n=0
 #Loop will be executed for 10000 times
 #More loops generates more points which leads to accuracy but increases the complexity
    for i in range(iterations):
 # Random number generation between the square root of
 #previous perfect square and the number just one greater
        x=random.random()+inc
 # Checking the condition if that no lies in interval of the root of previous perfect
 # square and the number whose square is to be calculated
        if(x*x-num<=0):
 # For every number lying in that range we take the count by incrementing n
            n=n+1
 # Checks numbers which are perfect squares
            if n%iterations==0:
 # For every perfect square we are incrementing inc to change the lower limit
 # and the range of random numbers
                inc=inc+1
 # For every perfect square it goes out of the current loop
                break
# Result for the square root we have count of the points in interval square root of prvious perfect square
#and sqrt(num) ratio of that count and total points considered will be added
#in the lowest limit will give the result
result=inc+n/iterations
print(result)
print("Square of the calculated square root:",(result*result))