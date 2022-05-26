# This program calculates the moment of inertia of any object given its x,y,z coordinates and the axis.
# Author                  : Aneesh Jain
# Last updated            : May 24, 2022
# Last updated            : May 25, 2022
# Origin is assumed for the calculation as x=y=z=0


from scipy import integrate
import sympy as smp
import matplotlib.pyplot as plt
import math
import numpy as np

def area(x,y,sh,response):
    if (sh==1):
        if (response==1):
            # Upper and lower limits of x integral
             xlower=x[0]
             xupper=x[1]
            # Upper and lower limits of y integral
             ylower=y[1]
             yupper=y[2]
            #  Function for calculating area
             farea=lambda yarea, xarea: 1
             areares,err=integrate.dblquad(farea,xlower,xupper,lambda yarea:ylower,lambda yarea:yupper)
             return areares

             


def rectangle2D(x,y,offsetx,offsety):

    # Length of the sides
    bxx=math.sqrt(pow(x[1]-x[0],2) + pow(y[1]-y[0],2))
    dyy=math.sqrt(pow(x[2]-x[1],2) + pow(y[2]-y[1],2))
    # Limits of integration    
    dxx=abs(y[2]-y[1])
    byy=abs(x[0]-x[1])
    # Moment of inertia function
    fxx = lambda yint: yint**2
    fyy = lambda xint: xint**2
    # Computing the integral for moment of inertia
    resxx, errxx = integrate.quad(fxx,-dxx/2,dxx/2)
    resyy, erryy = integrate.quad(fyy,-byy/2,byy/2)
    # Hence, moment of inertia is
    Ixx=bxx*resxx+(pow(offsety,2))*area(x,y,sh,response)
    Iyy=dyy*resyy+(pow(offsetx,2))*area(x,y,sh,response)
    Izz=Ixx+Iyy
    return Ixx, Iyy, Izz


print("\n\n")
print("---------------------START OF THE PROGRAM--------------------")
print("-------------------------------------------------------------")
print("What shape?:")
print("1) Rectangle")
print("2) Circle\n")
sh = int(input("Enter: "))
print("-------------------------------------------------------------")
print("Offset required?:")
print("1) Yes")
print("2) No\n")
offset=int(input("Yes or No? Select the option number: "))
print("-------------------------------------------------------------")

# print(response)
if (sh==1):
    print("Enter an option:")
    print("1) Enter coordinates")
    print("2) Enter dimensions\n")
    response=int(input("Enter your response here: "))
    print("-------------------------------------------------------------")
    # print(shape)
    if (response==1):
        x=np.zeros(4)
        y=np.zeros(4)
        print("Enter coordinates below:")
        for i in range(0,4):
            x[i]=float(input("\nEnter X" + str(i+1) + ":"))
            y[i]=float(input("Enter Y" + str(i+1) + ":"))
        print("-------------------------------------------------------------")

        if (offset==2):
            Ixx,Iyy,Izz= rectangle2D(x,y,0,0)
            print(Ixx,Iyy,Izz)
        elif (offset==1):
            offsetx=float(input("Offset X by: "))
            offsety=float(input("Offset Y by: "))
            Ixx,Iyy,Izz= rectangle2D(x,y,offsetx,offsety)
            print(Ixx,Iyy,Izz)

        
    elif (response==2):
        print("Enter dimensions: ")
        length=float(input("Enter length of the rectangle: "))
        width=float(input("Enter width of the rectangle: "))



        
        












