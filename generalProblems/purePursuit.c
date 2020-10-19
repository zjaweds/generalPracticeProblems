#include<stdio.h>
#include<math.h>

float dist(float,float,float,float);  	//FUNCTION FOR DISTANCE CALCULATION 

int main(){
	int t;
	float d,c,s,XF[13],YF[13]; 	// d,c,s FOR DISTANCE COSINE AND SINE RESPECTIVELY
								//XF[13],YF[13] ARRAYS TO STORE COORDINATES OF THE PURSUIER
	float XB[]={80,90,99,108,116,125,133,141,151,160,169,179,180};
								//ARRAY STORING X COORDINATE OF THE TARGET
	float YB[]={0,-2,-5,-9,-15,-18,-23,-29,-28,-25,-21,-20,-17};
								//ARRAY STORING Y COORDINATE OF THE TARGET
	XF[0]=0;	 				//INITIAL X COORDINATE OF FIGHTER
	YF[0]=50; 					//INITIAL X COORDINATE OF FIGHTER
	for(t=0;t<13;t++){ 	 		//IN WORST CASE LOOP WILL RUN 13 TIMES
		d=dist(XF[t],YF[t],XB[t],YB[t]); 	//CALLING DIST FUNCTION FOR DISTANCE
		if(d<=10){				//WHEN TARGET MEETS
			printf("\nTarget met at %dth minute at a distance %f.",(t-1),d);
								//t-1 BECAUSE FIGHTER HAS ALREADY REACHED THE TARGET  
			break; 				//TERMINATING THE PURSUIT
		}
		else{
			c=(XB[t]-XF[t])/d; 		//COSINE CALCULATION
			s=(YB[t]-YF[t])/d; 		//COSINE CALCULATION
			XF[t+1]=XF[t]+20*c; 	//NEW X COORDINATE OF THE FIGHTER
			YF[t+1]=YF[t]+20*s;		//NEW Y COORDINATE OF THE FIGHTER
	    }
		}
		if(t>11) 				//AS AT T=12 PURSUIT IS ASSUMED TO BE ENDED
			printf("\n!Target Escaped!");
	return 0;
}

float dist(float F,float f,float B,float b){ //DEFINITION OF THE dist() FUNCTION
	float d;
	d=sqrt((F-B)*(F-B)+(f-b)*(f-b));
	return d;
}