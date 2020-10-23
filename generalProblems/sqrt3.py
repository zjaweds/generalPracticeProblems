#Importing random module which contains the random() function
import random
n=0
#Loop will be executed for 10000 times
#More loops generates more points which leads to accuracy but increases the complexity
for i in range(10000):
 #Generating random numbers between 1 and 2 and assigning it to x as x the sqrt(3) is assumed to lie in 1 to 2
    x=random.random()+1
 #Checking whether point with coordinate x^3 lies between 1 and 2 or not
    if(x*x-3<=0):
#For each point lying in between 1 and 2 we increment n
 #to have count of points lying in that interval
        n=n+1
# Result for the square root we have count of the points in interval 1 and sqrt(3)
# ratio of that count and total points considered will be added in the lowest limit will give the result
result=1+n/10000
print(result)