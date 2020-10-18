# Importing random module which contains the random() function
import random
# Importing math module which contains the sqrt() function
import math
n=0;
# Loop will be executed for 10000 times
# More loops generates more points which leads to accuracy but increases the complexity
for i in range(10000):
 # Generating random numbers between 0 and 1 and assigning it to x
    x=random.random()
 # Generating random numbers between 0 and 1 and assigning it to y
    y=random.random()
 # Checking whether point with coordinate (x, y) lies within the quadrant or not
    if y<= math.sqrt(1-x*x):
 # For each point inside quadrant we increment n
 #to have count of points lying inside the quadrant 
        n=n+1;
# Result = 4* Total point inside quadrant /total points inside the square
#Total points inside the quadrant are also inside the square
# Therefore total points inside the square are total points generated i.e number of iterations
result=4*n/10000;
print(result)