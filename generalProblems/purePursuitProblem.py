import math
def dist(F,f,B,b): #definition of the dist() function
    d=math.sqrt((F-B)*(F-B)+(f-b)*(f-b))
    return d
 #function for distance calculation
XF=[0,1,2,3,4,5,6,7,8,9,10,11,12]
YF=[50,1,2,3,4,5,6,7,8,9,10,11,12]
#XF[13],YF[13] arrays storing coordinates of the pursuer
XB=[80,90,99,108,116,125,133,141,151,160,169,179,180]
#array storing x coordinate of the target
YB=[0,-2,-5,-9,-15,-18,-23,-29,-28,-25,-21,-20,-17]
#array storing y coordinate of the target
XF[0]=0 #initial X coordinate of fighter
YF[0]=50 #initial Y coordinate of fighter
for t in range(12): #in worst case loop will run 13 times
    d=dist(XF[t],YF[t],XB[t],YB[t])
    if(d<=10): #when target meets
        print("\nTarget met at "+ str(t-1)+" minute at a distance of "+str(d)+" kms.");#t-1 because at this time fighter has already reached the target.
        break; #terminating the pursuit
    else:
        c=(XB[t]-XF[t])/d; #cosine calculation
        s=(YB[t]-YF[t])/d; #sine calculation
        XF[t+1]=XF[t]+20*c; #new X coordinate of the fighter
        YF[t+1]=YF[t]+20*s; #new Y coordinate of the fighter
if(t>11):
    print("\n!Target Escaped!") #//as at t=12 pursuit is assumed to be ended
