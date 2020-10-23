

#Implementation in Python
import random #importing random module for creating random orders
cost=[1,2,3,4,5] #Declaration and initialisation of a list to store the cost
polP=[1,2,3,4,5]
polQ=[1,2,3,4,5]
j=0 #For accessing the indices of lists created above
for P,Q in [(125, 150),(125, 250),(150, 250),(175, 250),(175, 300)]: #P and Q will get values from a tuple at a time
    s=115 #Stock at start of day for a given policy
    d=1 #Day number
    oo=0 #Outstanding orders
    c=0 # Instantaneous Cost summed up
 #print("Policy P: "+str(P)+" Q: "+str(Q))
    for d in range(180):
        if(oo==1): # If there are outstanding orders
            s=s+Q # Existing stock and Outstanding order sums up to make new stock
            dem=random.random()*99 #Demand for a day
            s=s-dem
            c=c+(0.75*s) # Calculation of carrying cost
            d=d+1 #Incrementing day
            if(s<=P): # Reorder point reached or not
                oo=1
                c=c+75 #Reorder cost
                for i in range(2):
                    dem=random.random()*99 #Two Days running at previous stock
                    if(s>=dem): # Stock and demand comparison
                        s=s-dem
                        c=c+(s*0.75) #Crrying cost
                        d=d+1
                    else:
                        c=c+(dem-s)*18 #Loss due to lack of stock
                        s=0
                        d=d+1
            else:
                oo=0
                dem=random.random()*99
                if(s>=dem):
                    s=s-dem
                    c=c+(s*0.75)
                else:
                    c=c+(dem-s)*18
                    s=0
        else:
                dem=random.random()*99
                s=s-dem
                c=c+(0.75*s)
                d=d+1
                if(s<=P):
                    oo=1
                    c=c+75
                    for i in range(2):
                        dem=random.random()*99
                        if(s>=dem):
                            s=s-dem
                            c=c+(s*0.75)
                            d=d+1
                        else:
                            c=c+(dem-s)*18
                            s=0
                            d=d+1
                else:
                    oo=0
                    dem=random.random()*99
                    if(s>=dem):
                        s=s-dem
                        c=c+(s*0.75)
                    else:
                        c=c+(dem-s)*18
                        s=0
    cost[j]=c #Storing calculated cost for a policy
    polP[j]=P #Storing P for a policy
    polQ[j]=Q #Storing Q for a policy
    j+=1


print("Minimum cost "+str(min(cost))+" for Policy: P="+str(polP[cost.index(min(cost))])+" Q="+str(polQ[cost.index(min(cost))]))