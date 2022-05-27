# This program calculates the moment of inertia of any object given its x,y,z coordinates and the axis.
# Author                  : Aneesh Jain
# Last updated            : May 24, 2022
# Last updated            : May 25, 2022
# Last updated            : May 26, 2022
# Origin is assumed for the calculation as x=y=z=0


from scipy import integrate
import sympy as smp
import matplotlib.pyplot as plt
import math
import numpy as np

def area(x,y,sh,response):
    if (sh==1):        
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

def convertunits(unitsin,unitsout):
    if (sh==1 or sh==2):
        if (unitsin==1):
            if (unitsout==1):
                return 1
            elif (unitsout==2):
                out=pow(pow(10,-1),4)
                return out
            elif (unitsout==3):
                out=pow(pow(10,-3),4)
                return out
            elif (unitsout==4):
                out=pow((1/25.4),4)
                return out

        elif (unitsin==2):
            if (unitsout==1):
                return pow(10,4)
            elif (unitsout==2):
                return 1
            elif (unitsout==3):
                out=pow(pow(10,-2),4)
                return out
            elif (unitsout==4):
                out=pow((1/2.54),4)
                return out

        elif (unitsin==3):
            if (unitsout==1):
                return pow(1000,4)
            elif (unitsout==2):
                return pow(100,4)
            elif (unitsout==3):
                return 1
            elif (unitsout==4):
                out=pow((100/2.54),4)
                return out

        elif (unitsin==4):
            if (unitsout==1):
                return pow(25.4,4)
            elif (unitsout==2):
                return pow(2.54,4)
            elif (unitsout==3):
                return pow(2.54/100,4)
            elif (unitsout==4):
                out=pow((100/2.54),4)
                return out




def rectangle2D(x,y,offx,offy,sh,response,unitsin,unitsout):    
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
    Ixx=(bxx*resxx+(pow(offy,2))*area(x,y,sh,response))*convertunits(unitsin,unitsout)
    Iyy=(dyy*resyy+(pow(offx,2))*area(x,y,sh,response))*convertunits(unitsin,unitsout)
    Izz=Ixx+Iyy
    return Ixx, Iyy, Izz

choice=1
print("\n\n")
print("---------------------START OF THE PROGRAM--------------------")
print("-------------------------------------------------------------")
if (choice==1):
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
    print("Enter the input units:")
    print("1) Millimeters")
    print("2) Centimeters")
    print("3) Meters")
    print("4) Inches")
    unitsin=int(input("Enter your choice: "))
    print("-------------------------------------------------------------")
    print("Enter the output units:")
    print("1) Millimeters")
    print("2) Centimeters")
    print("3) Meters")
    print("4) Inches")
    unitsout=int(input("Enter your choice: "))
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
            xcoord=np.zeros(4)
            ycoord=np.zeros(4)
            print("Enter coordinates below:")
            for i in range(0,4):
                xcoord[i]=float(input("\nEnter X" + str(i+1) + ":"))
                ycoord[i]=float(input("Enter Y" + str(i+1) + ":"))
            print("-------------------------------------------------------------")

            if (offset==2):
                Ixx,Iyy,Izz= rectangle2D(xcoord,ycoord,0,0,sh,response,unitsin,unitsout)
                print(Ixx,Iyy,Izz)
                print("More calculations?")
                print("1) Yes")
                print("2) No")
                choice=int(input("Enter your choice: "))
            elif (offset==1):
                offsetx=float(input("Offset X by: "))
                offsety=float(input("Offset Y by: "))
                Ixx,Iyy,Izz= rectangle2D(xcoord,ycoord,offsetx,offsety,sh,response,unitsin,unitsout)
                print(Ixx,Iyy,Izz)
                print("More calculations?")
                print("1) Yes")
                print("2) No")
                choice=int(input("Enter your choice: "))

            
        elif (response==2):
            print("Enter dimensions: ")
            length=float(input("Enter length of the rectangle: "))
            width=float(input("Enter width of the rectangle: "))
            xdim=np.zeros(4)
            ydim=np.zeros(4)
            xdim[1]=float(length/2)
            xdim[2]=float(length/2)
            xdim[0]=-(float(length/2))
            xdim[3]=-(float(length/2))
            ydim[1]=-(float(width/2))
            ydim[2]=(float(width/2))
            ydim[0]=-(float(width/2))
            ydim[3]=(float(width/2))
            if (offset==2):
                Ixx,Iyy,Izz= rectangle2D(xdim,ydim,0,0,sh,response,unitsin,unitsout)
                print(Ixx,Iyy,Izz)
                print("More calculations?")
                print("1) Yes")
                print("2) No")
                choice=int(input("Enter your choice: "))
            elif (offset==1):
                offsetx=float(input("Offset X by: "))
                offsety=float(input("Offset Y by: "))
                Ixx,Iyy,Izz= rectangle2D(xdim,ydim,offsetx,offsety,sh,response,unitsin,unitsout)
                print(Ixx,Iyy,Izz)
                print("More calculations?")
                print("1) Yes")
                print("2) No")
    choice=int(input("Enter your choice: "))


    # elif (sh==2):

        
        
        



        
        












