#Dubey's Calculator    by  AtharvDubey12

memory=[]
loopbreaker=1
import subprocess
import sys
import time
import urllib.request

#Check for internet connection

def internetcheck():
    try:
        urllib.request.urlopen("https://www.google.com", timeout= 5)
        return True
    except:
        return False
    

list= ['sympy','tk']
for lib in list:
    try:
        __import__(lib)
    except ImportError:
        print(f"{lib} library is not available! please wait while we install it for you.")
        if internetcheck():
            print(f"An active internet connection has been detected, proceeding to install {lib} library")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(f"{lib} installed!")
        else:
            print("Internet connection not detected! please turn on the internet so that we can install missing libraries.")
            while True:
                if internetcheck():
                    print("internet connection established! proceeding to download missing libraries")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
                    print(f"{lib} installed!")
                    break
                else:
                    end= int(input("enter 900 to end program, any other integer to resume (you'll need internet though!)"))
                    if end==900:
                        loopbreaker=0
                        break
                    else:
                        time.sleep(5)


#Calc code begins from here---

import sympy as sp 
from sympy.plotting import plot
from tkinter import *
root= Tk()
root.geometry('1980x1080')
userlabel= Label(text="""          Basic Arithmetic (TK= '+' for addition and subtraction,  '*' for multiplication and division )\n
                                   Equation Solving (TK= 'eqn' for solving equation systems of upto 3 variables (x,y,z).)\n
                                   Differential Equation solving (TK= 'de' for solving differential equation of 'n'th order and 'm'th degree)\n
                                   Calculus: Integration and Differentiation (TK= 'i' for integration, 'd' for differentiation)\n
                                   Matrix Calculations (upto 3 distinct variables allowed: x,y,z) (TK= mx) (STK= 'det' for determinant,\n
                                                        'inv' for inverse, 'adj' for adjoint, 'ceqn' for retrieving characteristic equation,\n
                                                        'mm' for matrix multiplication, '+' for addition/subtraction of 2 matrices)\n
                                   Graph plotting of y= f(x) (TK= 'g')\n
                                   Unit Conversions (TK='uc') (STK= 'jev' Joule to electron volts, 'evj' Electron volts to Joules,\n
                                   'nd' Newtons to dyne, 'dn' dyne to Newtons, 'd' for degree to Kelvin and Fahrenheit, 'k' for Kelvin to others,\n
                                   'f' for Fahrenheit to others, 'm' for metre to others, 'mm' for millimetres to others, 'hpw' for horsepower to watts.\n
                                   'whp' for watts to horsepower, 'dr' for degree to radians, 'rd' for radians to degrees)\n
                                   Continuity and Differentiability check at a point (TK= 'cdc')\n
                                   Circum radius calculation for any triangle (TK= 'cr')\n
                                   Area Calculations (TK='ac') (STK= 'c' for circle, 'r' for rectangle/square, 't' for traingle,\n
                                   'cy' for cylinder, 'co' for cone, 'e' for ellipse, 's' for sphere, 'hs' for hemisphere, 'cbd' for cuboid.\n
                                   'f' for frustum, 'nsrp' for n sided regular polygon, 'tz' for a trapezium, 'csec' for circle sector, 'cseg' for circle segment.\n
                                   'pg' for parallelogram)\n
                                   Distance between two 3D points (TK= 'd2p')
                                   Hypotenuse Calculation (TK= 'pyt)\n
                                   Collinearity check for three 3D points (TK= 'col')\n
                                   Calculations related to Lines (TK= 'lin') (STK= 'sds' for shortest distance between skew 3D lines,\n
                                   'sdp' for shortest distance between 2D/3D parallel lines, 'pc' for parallel check for 2D/3D lines)\n
                                   Vector Calculations (TK= 'vt') (STK= 'dot' for dot product, 'cross' for cross product, 'vtp' for vector triple product,\n
                                   'stp' for scalar triple product)\n
                                   Capacitance Calculations (TK='cap') (STK= 'pp' for parallel plate, 's1' for sphere, 's2' for sphere with outer shell, 'cy' for cylinder.)\n
                                   TO QUIT (TK= 'quit')""")
userlabel.pack()
root.title("Dubey's Calculator: Task Codes (TK) and Sub Task Codes (STK)")
while loopbreaker==1:




    try:
        taskcode= input("\nenter task code: ")
        if taskcode=="+":
            memstore="+ "
            numcount= int(input("\nenter number of numbers to be added/subtracted: "))
            addresult=0
            for looper in range(numcount):
                num= float(input("enter number with appropriate sign(s): "))
                addresult+=num
                memstore+=str(num) + " "
            memstore+= "= "
            memstore+= str(addresult)
            memory.append(memstore)
            print("\ntotal sum of all the entered number is: ", addresult)
     
        elif taskcode=="tm":
            print("Temporary memory is being accessed.\n")
            if memory==[]:
                print("memory is empty, please perform operations to store data.\n")
            else:
                for looper in memory:
                    print(looper)

        elif taskcode=="*":
            numcount1= int(input("enter number of numbers to be multiplied: "))
            numcount2= int(input("enter number of numbers to be divided: "))
            addresult=1
            for looper in range(numcount1):
                num= float(input("enter number (multiplication): "))
                addresult*=num
            for looper2 in range(numcount2):
                num2= float(input("enter number (division): "))
                if num2==0:
                    print("This input has been ignored, remaining one will be considered for evaluation.")
                else:
                    addresult*=1/num2
            print("product of all the entered number is: ", addresult)
            
    
        elif taskcode=="d":
            independent_variable=input("enter independent variable symbol: ")
            dependent_variable=input("enter dependent variable symbol: ")
            x= sp.symbols('x')
            func= input("enter function of independent variable (e.g: y= f(x), so enter f(x)): ")
            f_x=sp.simplify(func)
            derivative= sp.diff(f_x, x)
            print("derivative is: ", derivative)
          

        elif taskcode=="i":
            x= sp.symbols("x")
            func=input(f"enter function f({x}): ")
            f_x= sp.simplify(func)
            type= input("\nenter 'i' for indefinite integration, 'd' for definite integration: ")
            if type=='i':
                integral= sp.integrate(f_x,x)
                print(f"integration is: {integral} + C")
            elif type=='d':           
                lowlim= input("enter lower limit (e.g: 2**x + 6): ")
                uplim= input("enter upper limit: ")
                lowerlimit=sp.symbols(lowlim)
                upperlimit=sp.symbols(uplim)
                integral= sp.integrate(f_x, (x,lowerlimit,upperlimit))
                print(f"integral is: {integral}\n")
               
            else:
                print("invalid input")
    
        elif taskcode=='mx':
            x= sp.symbols('x')
            y= sp.symbols('y')
            z= sp.symbols('z')
            
            matrixinput= eval(input("enter matrix (e.g: [[1,2,3],[4,5,x],[y,z,8]] a 3x3 matrix) (at max 3 distinct variables allowed): "))
            matrix= sp.Matrix(matrixinput)
            subtaskcode=input("enter sub task code: ")
            if subtaskcode=='m':
                matrixinput2= eval(input("enter matrix 2 (e.g: [[1,2,3],[4,5,x],[y,z,8]] a 3x3 matrix) (at max 3 distinct variables allowed): "))
                matrix2= sp.Matrix(matrixinput2)
                mult= matrix*matrix2
                print("multiplication result is", mult)
               
             
            elif subtaskcode=='inv':
                inverse=matrix.inv()
                print(f"inverse of {matrixinput} is: ", inverse)
         

            elif subtaskcode=='det':
                determinant= matrix.det()
                print(f"the determinant value of {matrixinput} is: ", determinant)
              
            elif subtaskcode=='adj':
                adjoint= matrix.adjugate()
                print(f"the determinant value of {matrixinput} is: ", adjoint)
         
            
            elif subtaskcode=='ceqn':
                v= sp.symbols('v')
                eqndet= (matrix-v*sp.eye(matrix.shape[0])).det()
                print(f"characteristic equation of {matrix} is {eqndet} = 0")
                equation= eqndet
                solution= sp.solve(equation, v)
                print(f"\nsolution of {eqndet} =0 is ", solution)
             
            
            elif subtaskcode=='+':
                matrixinput2= eval(input("enter matrix 2 (e.g: [[1,2,3],[4,5,x],[y,z,8]] a 3x3 matrix) (at max 3 distinct variables allowed): "))
                matrix2= sp.Matrix(matrixinput2)
                matrix3= matrix+matrix2
                print(f"algebraic sum of {matrix} and {matrix2} is: ", matrix3)
            


        elif taskcode=='eqn':
            x= sp.symbols('x')
            y= sp.symbols('y')
            z= sp.symbols('z')
        
            varcount=int(input("enter number of variables/ number of equations (1 or 2 or 3): "))
            if varcount==1:
                equation= input("enter equation in format a*x**n + b*x**n-1.....+ n =0 without '=0': ")
                solution= sp.solve(equation, x)
                print(f"solution of {equation} is: ", solution)
               
            
            elif varcount==2:
                equation= input("enter equation in format a*x**n + b*x**n-1.....+ n =0 without '=0': ")
                equation2= input("enter equation in format a*y**n + b*y**n-1.....+ n =0 without '=0': ")
                solution= sp.solve([equation,equation2], (x,y))
                print("solution is: ", solution)
             
            
            elif varcount==3:
                equation= input("enter equation in format a*x**n + b*x**n-1.....+ n =0 without '=0': ")
                equation2= input("enter equation in format a*y**n + b*y**n-1.....+ n =0 without '=0': ")
                equation3= input("enter equation in format a*z**n + b*z**n-1.....+ n =0 without '=0': ")
                solution= sp.solve([equation,equation2,equation3], (x,y,z))
                print("solution is: ", solution)
        
            
            else:
                print("invalid value for variable count has been input.")
               
            
        elif taskcode=='cap':
            
            subtaskcode= input("enter sub task code: ")
            if subtaskcode=='pp':
                platearea= float(input("plate area (in SI): "))
                dielectric= float(input("dielectric constant (in SI): "))
                distance= float(input('distance between plates (in SI): '))
                capacitance= (platearea*dielectric*8.85418*10**(-12))/distance
                print("capacitance is: ", capacitance)
            
            elif subtaskcode=='s1':
                radius= float(input("enter radius of sphere: "))
                capacitance= 4*3.1415*8.85*(10**-12)*radius
                print(f"capacitance of a spherical capacitor of radius {radius} is: ", capacitance)
      
            
            elif subtaskcode=='s2':
                radius1= float(input("enter radius of inner sphere: "))
                radius2= float(input("enter radius of outer shell: "))
                capacitance= 4*3.1415*8.85*(10**-12)*radius1*radius2/(radius2-radius1)
                print(f"capacitance of a spherical capacitor of radius {radius1} with a outer shell of finite radius {radius2} is: ", capacitance)
       
            
            elif subtaskcode=='cy':
                radius1= float(input("enter radius of inner cylinder: "))
                radius2= float(input("enter radius of outer cylinder shell: "))
                length= float(input("enter length of cylinders: "))
                capacitance= (2*3.1415*8.85*(10**-12)*length)/sp.log(radius2/radius1)
                print("capacitance is: ", capacitance)
              
    
        elif taskcode=='uc':
            
            subtaskcode= input("enter sub task code: ")
            if subtaskcode=='jev':
                joules=  float(input("enter energy in Joules: "))
                ev= 6.242*(10**18)*joules
                print(f"{joules} J = {ev} eV\n")
      
            
            elif subtaskcode=='evj':
                ev=  float(input("enter energy in electron volts: "))
                joules= 1.602*(10**-19)*ev
                print(f"{ev} eV = {joules} J\n")
          

            elif subtaskcode=='nd':
                newton= float(input("enter force in Newtons: "))
                dyne= newton*(10**5)
                print(f"{newton} N = {dyne} dyne\n")
           

            elif subtaskcode=='dn':
                dyne= float(input("enter force in dyne: "))
                newton= dyne*(10**-5)
                print(f"{dyne} dyne = {newton} N\n")
             

            elif subtaskcode=='d':
                degree= float(input("enter temperature in degree celcius: "))
                if degree<-273.15:
                    print("Invalid input: Temperature cannot go lower than absolute zero.\n")
          
                else:
                    print(f"{degree} C = {degree + 273.15} K = {degree*33.8} F\n")
        

            elif subtaskcode=='k':
                kelvin= float(input("enter temperature in Kelvin: "))
                if kelvin<0:
                    print("Invalid input: Temperature cannot go lower than absolute zero.\n")
                 
                else:
                    print(f"{kelvin} K = {kelvin - 273.15} C = {(kelvin - 273.15)*9/5 + 32} F \n")
    
            
            elif subtaskcode=='f':
                fahrenheit= float(input("enter temperature in fahrenheit: "))
                if fahrenheit<-459.67:
                    print("Invalid input: Temperature cannot go lower than absolute zero.\n")
                
                else:
                    print(f"{fahrenheit} F = {(fahrenheit-32)*5/9} C = {(fahrenheit-32)*5/9+273.15} K \n")
            
            
            elif subtaskcode=='m':
                metre= float(input("enter length in metre: "))
                print(f"{metre} m = {metre*100} cm = {metre*1000} mm = {metre*39.37} inches = {int(metre*39.37/12)} feet {((metre*39.37/12)-int((metre*39.37/12)))*12} inches")

            
            elif subtaskcode=='mm':
                milimetre= float(input("enter length in millimetre: "))
                print(f"{milimetre} mm = {milimetre/10} cm = {milimetre*1000} m = {milimetre*39.37/1000} inches = {int(milimetre*39.37/(12*1000))} feet {(milimetre*39.37/(12*1000)-int((milimetre*39.37/(12*1000))))*12} inches")
      

            elif subtaskcode=='hpw':
                horse= float(input("enter power in horsepower HP: "))
                print(f"{horse} HP = {horse *746} W")
           

            elif subtaskcode=='whp':
                watt= float(input("enter power in watts W: "))
                print(f"{watt} W = {watt /746} HP")
    
            
            elif subtaskcode=='dr':
                degree= float(input("enter angle in degrees: "))
                print(f"{degree} degrees in radians is: ", degree*3.1415/180)
            
            elif subtaskcode=='rd':
                rad= float(input("enter angle in radians: "))
                print(f"{rad} radians in degrees is: ", rad*180/3.1415)
            
            else:
                print("enter a valid sub task code.")
  
        elif taskcode=='de':
            
            x= sp.symbols('x')
            y= sp.Function('y')(x)
            equation=eval(input("enter differential equation in format y.diff(x,2) + y -5 =0 (without '=0'): "))
            solution= sp.dsolve(sp.Eq(equation,0))
            print(f"solution of differential equation {equation} is: ", solution)
        
        elif taskcode=='cr':
            brancher= input("will the input be angle (a) or area (ar)? ")
            if brancher == 'a':
                a= float(input("enter side length of a side to which the opposite angle is known: "))
                brancher2= input("will the input for angle be in degrees (d) or radians (r)? ")
                if brancher2 == 'r':
                    angle= float(input(f"enter opposite angle to {a} in radians: "))
                    print("circum radius of the given circle is: ", a/(0.5*sp.sin(angle)))
                elif brancher2 == 'd':
                    angle= float(input(f"enter opposite angle to {a} in degrees: "))
                    print("circum radius of the given circle is: ", a/(0.5*sp.sin(angle*3.1415/180)))
                else:
                    print("enter a valid input.")
            elif brancher == 'ar':
                area= float(input("enter area of triangle: "))
                a= float(input("enter side 1: "))
                b= float(input("enter side 2: "))
                c= float(input("enter side 3: "))
                print("circum radius is: ", a*b*c/(4*area))

    
        elif taskcode=='g':
            x= sp.symbols('x')
            func= input("enter function in terms of x (e.g: floor(sin(x)) + exp(x**2): ")
            function= sp.sympify(func)
            range= eval(input("enter range of input (e.g: [lower limit, upper limit]): "))
            plot(function, (x,range[0],range[1]), title= f"y = {func}", xlabel= "x axis", ylabel= "y axis")
            

        elif taskcode=='cdc':
            point= float(input("enter point at which continuity is being checked (x): "))
            func= input("enter function y= f(x) without 'y=': ")
            x= sp.symbols('x')
            function= sp.sympify(func)
            
            try:
                fx=function.subs(x,point)
            except Exception:
                print(f"{func} at x= {point} is not defined. Function is neither continous nor differentiable at x= {point}.")
            try:
                lhl=sp.limit(function,x,point, dir='-')
            except Exception:
                print(f"Left hand limit for {func} at x= {point} is not defined. Function is neither continous nor differentiable at x= {point}.")
 
            try:
                rhl= sp.limit(function,x,point,dir='+')
            except Exception:
                print(f"Right hand limit for {func} at x= {point} is not defined. Function is neither continous nor differentiable at x= {point}.")

            if fx==lhl and fx==rhl and rhl==lhl:
                print(f"{func} at x= {point}, is continous.")
                
                try:
                    derivative= sp.diff(function, x)
                    try:
                        derivativeatpoint= derivative.subs(x,point)
                    except Exception:
                        print(f"{func} is not differentiable at x= {point}")

                    if derivativeatpoint.is_real:
                        print(f"{func} is differentiable at x= {point}")
                    else:
                        print(f"{func} is non differentiable at x= {point}")
            
                except Exception:
                    print(f"{func} is not differentiable at x= {point}.")
            else:
                print(f"{func} is neither continous nor differentiable at x= {point}")
        
            
        elif taskcode=='ac':
            print("Note: you can get distance between 2 points to get side lengths of polygons if you have point coordinates, using d2p task code.\n")
            subtaskcode=input("enter sub task code:")
            if subtaskcode=='c':
                radius= float(input("enter radius of circle: "))
                print("area of the circle is: ", 3.1415*radius**2)
        
            
            elif subtaskcode=='r':
                length= float(input("enter length: "))
                breadth= float(input("enter breadth: "))
                print("area of rectangle is: ", length*breadth)
            
            
            elif subtaskcode=='t':
                side1= float(input("side length 1: "))
                side2= float(input("side length 2: "))
                side3= float(input("side length 3: "))
                s= (side1+side2+side3)/2
                area= (s*(s-side1)*(s-side2)*(s-side3))**0.5
                print("area of triangle is: ", area)
        
            
            elif subtaskcode=='cy':
                height= float(input("enter height of cylinder: "))
                radius= float(input("enter height of cylinder: "))
                print("curved surface area of a cylinder is: ", 2*3.1415*radius*height)
                print("total surface area of cylinder is: ", 2*3.1415*radius*height + 2*3.1415*(radius**2))
    
            
            elif subtaskcode=='co':
                radius= float(input("enter radius of cone: "))
                brancher= input("decide the input (slant height (sh) / height (h)): ")
                if brancher== 'sh':
                    slant= float(input("enter slant height: "))
                    print("curved surface area of cone is: ", 3.1415*radius*slant)
                    print("total surface area of cone is: ", 3.1415*radius*slant + 3.1415*(radius**2))
            
                elif brancher== 'h':
                    height= float(input("enter height of cone: "))
                    print("curved surface area of cone is: ", 3.1415*radius*((height**2 + radius**2)**0.5))
                    print("total surface area of cone is: ", 3.1415*radius*((height**2 + radius**2)**0.5 + 3.1415*(radius**2)))

                else:
                    print("enter a valid sub task code.")
            
            elif subtaskcode=='e':
                major= float(input("enter semi major axis length: "))
                minor= float(input("enter semi minor axis length: "))
                print("area of the ellipse is: ", 3.1414*major*minor)
            
            elif subtaskcode=='s':
                radius= float(input("enter radius of sphere: "))
                print("surface area of sphere is: ", 4*3.1415*radius**2)
            
            elif subtaskcode=='hs':
                radius= float(input("enter radius of hemisphere: "))
                print("curved surface area of hemisphere is: ", 2*3.1415*radius**2)
                print("total surface area of hemisphere is: ", 3*3.1415*radius**2)
            
            elif subtaskcode=='cbd':
                length= float(input("enter length of cuboid: "))
                breadth= float(input("enter breadth of cuboid: "))
                height= float(input("enter height of cuboid: "))
                print("surface area of cuboid is: ", 2*(length*breadth + breadth*height + length*height))
            
            elif subtaskcode=='f':
                radius1= float(input('enter radius of 1st circular face: '))
                radius2= float(input("enter radius of 2nd circular face: "))
                length= float(input("enter slant height of frustum: "))
                print("curved surface area of frustum is: ", 3.1415*(radius1+radius2)*length)
                print("total surface area of frustum is: ", 3.1415*radius1**2 + 3.1415*radius2**2 + 3.1415*(radius1+radius2)*length)
            
            elif subtaskcode=='nsrp':
                n= float(input("enter number of sides: "))
                brancher= input("will the input be side length (s) or circumcircle radius (r)? ")
                if brancher == 's':
                    s= float(input("enter side length of regular polygon: "))
                    print(f"area of {n} sided regular polygon is: ", 0.25*n*s*s*sp.cot(3.1415/n))
                elif brancher=='r':
                    r= float(input("enter circum circle radius: "))
                    print(f"area of {n} sided regular polygon is: ", 0.5*n*r*r*sp.sin(6.28/n))
                else:
                    print("enter a valid sub task code.")
            
            elif subtaskcode=='tz':
                side1= float(input("enter side length of 1st parallel side: "))
                side2= float(input("enter side length of 2nd parallel side: "))
                h= float(input("enter perpendicular distance between 2 parallel sides: "))
                print("area of trapezium is: ", 0.5*h*(side1+side2))
            
            elif subtaskcode=='csec':
                radius = float(input("enter radius of circle: "))
                brancher= input("will the angle be in degree (d) or radians (r)? ")
                if brancher == 'd':
                    angle= float(input("enter angle in degrees: "))
                    print("area of the circle sector is: ", 3.1415*angle*radius*radius/360)
                elif  brancher == 'r':
                    angle= float(input("enter angle in radians: "))
                    print("area of circle sector is: ", 0.5*angle*radius*radius)
                else:
                    print("enter a valid sub task code.")
            
            elif subtaskcode=='cseg':
                radius = float(input("enter radius of circle: "))
                brancher= input("will the angle be in degree (d) or radians (r)? ")
                if brancher == 'd':
                    angle= float(input("enter angle in degrees: "))
                    print("area of the circle sector is: ", 0.5*radius*radius*(angle*(3.14/180) - sp.sin(angle*(3.14/180))))
                elif  brancher == 'r':
                    angle= float(input("enter angle in radians: "))
                    print("area of circle sector is: ", 0.5*radius*radius*(angle - sp.sin(angle)))
            
            elif subtaskcode=='pg':
                base= float(input("enter base length: "))
                height= float(input("enter height: "))
                print("area of parallelogram is: ", base*height)
            
            else:
                print("enter a valid sub task code")
            


        elif taskcode=='d2p':
            x1= float(input("enter x1: "))
            y1= float(input("enter y1: "))
            z1= float(input("enter z1: "))
            x2= float(input("enter x2: "))
            y2= float(input("enter y2: "))
            z2= float(input("enter z2: "))
            print("distance between the two points is: ", (((x1-x2)**2) + ((y1-y2)**2) + ((z1-z2)**2))**0.5)
            loopbreaker= int(input("1 to repeat, any other to end: "))
        
        elif taskcode=='pyt':
            side1= float(input("enter smallest side: "))
            side2= float(input("enter smaller side: "))
            print("hypotenuse is: ", (side1**2 + side2**2)**0.5)

        elif taskcode=='col':
            x1= float(input("enter x1: "))
            y1= float(input("enter y1: "))
            z1= float(input("enter z1: "))
            x2= float(input("enter x2: "))
            y2= float(input("enter y2: "))
            z2= float(input("enter z2: "))
            x3= float(input("enter x3: "))
            y3= float(input("enter y3: "))
            z3= float(input("enter z3: "))
            temp= ((x2-x1)*((y3-y1)-(y2-y1))-(y2-y1)*((x3-x1)-(x2-x1))+(z2-z1)*((x3-x1)*(y2-y1)-(x2-x1)*(y3-y1)))
            if temp == 0:
                print("\nGiven 3 points are collinear.")

            else:
                print("\nGiven 3 points are not collinear.")
        
        elif taskcode=='lin':

            if subtaskcode=='sds':
                x1= float(input("enter x coordinate of any point on the line 1: "))
                y1= float(input("enter the corresponding y coordinate of the point on the line 1: "))
                z1= float(input("enter the corresponding z coordinate of the point on the line 1: "))
                a1= float(input("enter direction ratio (n*cos a) of line 1: "))
                b1= float(input("enter direction ratio (n*cos b) of line 1: "))
                c1= float(input("enter direction ratio (n*cos c) of line 1: "))
                x2= float(input("enter x coordinate of any point on the line 2: "))
                y2= float(input("enter the corresponding y coordinate of the point on the line 2: "))
                z2= float(input("enter the corresponding z coordinate of the point on the line 2: "))
                a2= float(input("enter direction ratio (n*cos a) of line 2: "))
                b2= float(input("enter direction ratio (n*cos b) of line 2: "))
                c2= float(input("enter direction ratio (n*cos c) of line 2: "))
                distance= ((x2-x1)*(b1*c2-c1*b2) + (y2-y1)*(c1*a2-a1*c2) + (z2-z1)*(a1*b2-b1*a2))/((b1*c2-c1*b2)**2 + (c1*a2-a1*c2)**2 + (a1*b2-b1*a2)**2)**0.5
                if distance<0:
                    print("the shortest distance between the 2 given skew lines is: ", -distance) 
                else:
                    print("the shortest distance between the 2 given skew lines is: ", distance)

            elif subtaskcode=='sdp':
                dimension= input("are the lines 2D (2D) or 3D (3D) ?")
                if dimension=='2D' or '2d':
                    A= float(input("enter A in the equation of the line 1 of format Ax + By + C1= 0: "))
                    B= float(input("enter B in the equation of the line 1 of format Ax + By + C1= 0: "))
                    C1= float(input("enter C1 in the equation of the line 1 of format Ax + By + C1= 0: "))
                    C2= float(input("enter C1 in the equation of the line 2 of format Ax + By + C2= 0: "))
                    distance= (C2-C1)/(A**2 + B**2)**0.5
                    if distance <0:
                        print("distance between two parallel lines is: ", -distance)
                    else:
                        print("distance between two parallel lines is: ", distance)
                
                elif dimension== '3D' or '3d':
                    x1= float(input("enter x coordinate of any point on the line 1: "))
                    y1= float(input("enter y coordinate of any point on the line 1: "))
                    z1= float(input("enter z coordinate of any point on the line 1: "))
                    x2= float(input("enter x coordinate of any point on the line 2: "))
                    y2= float(input("enter y coordinate of any point on the line 2: "))
                    z2= float(input("enter z coordinate of any point on the line 2: "))
                    bx= float(input("x componentt of direction vector: "))
                    by= float(input("y componentt of direction vector: "))
                    bz= float(input("z componentt of direction vector: "))
                    distance= ((x2-x1)*bx + (y2-y1)*by + (z2-z1)*bz)/(bx**2 + by**2 + bz**2)**0.5
                    if distance<0:
                        print("distance between 2 lines is: ", -distance)
                    else:
                        print("distance between 2 lines is: ", distance)
                
                else:
                    print("calculator only supports 1D, 2D and 3D calculations.")


            elif subtaskcode=='pc':
                dimension= input("are the lines 2D (2D) or 3D (3D) ?")
                if dimension=='2D' or '2d':
                    m1= float(input("enter coefficient of x when the line is of the format y= mx + c where m and c are constants, of line 1: "))
                    c1= float(input("enter c when the line is of the format y= mx + c where m and c are constants, of line 1: "))
                    m2= float(input("enter coefficient of x when the line is of the format y= mx + c where m and c are constants, of line 2: "))
                    c2= float(input("enter c when the line is of the format y= mx + c where m and c are constants, of line 2: "))
                    if m1==m2 and c1 != c2:
                        print("two given lines are parallel, they have no real intersection points.")
                    elif m1==m2 and c1== c2:
                        print("two given lines are coincident, they have infinitely many intersection points.")
                    else:
                        print("two given lines are neither parallel, nor coincident, hence they will intersect at one unique real point.")
                
                elif dimension=='3D' or '3d':
                    vect1= sp.Matrix(eval(input("enter direction vector of line 1 (e.g: [1,2,3]): ")))
                    vect2= sp.Matrix(eval(input("enter direction vector of line 2 (e.g: [1,2,3]): ")))
                    cross= vect1.cross(vect2)
                    dot= vect1.dot(vect2)
                    if cross== 0:
                        print("lines are parallel.")
                    elif dot==0:
                        print("lines are perpendicular.")
                    else:
                        print("lines are neither parallel, nor perpendicular. ")
                
                else:
                    print("calculator only supports 1D, 2D and 3D calculations.")

        elif taskcode=='vt':
                from sympy.vector import CoordSys3D
                from sympy.vector.vector import cross
                
                x= sp.symbols('x')
                y= sp.symbols('y')
                z= sp.symbols('z')
                print("Note that at maximum, 3 distinct variables are allowed. Also remember that operations will occur in this way: Vector n (operation) Vector n+1\n")
                subtaskcode= input("enter sub task code: ")
                if subtaskcode=='dot':
                
                    vect1= sp.Matrix(eval(input("enter vector 1 (e.g. [1,2,x]: ")))
                    vect2= sp.Matrix(eval(input("enter vector 2 (e.g. [y,z,x]: ")))
                    dot= vect1.dot(vect2)
                    print(f"{vect1} . {vect2} = ", dot)

                elif subtaskcode=='cross':
                    vect1= sp.Matrix(eval(input("enter vector 1 (e.g. [1,2,x])")))
                    vect2= sp.Matrix(eval(input("enter vector 2 (e.g. [y,z,x]: ")))
                    cross= vect1.cross(vect2)
                    print(f"{vect1} x {vect2} = ", cross)
                
                elif subtaskcode== 'vtp':
                    N= CoordSys3D('N')
                    vect1= eval(input("enter vector 1 (e.g. [1,2,x])"))
                    vect2= eval(input("enter vector 2 (e.g. [y,z,x]: "))
                    vect3= eval(input("enter vector 3 (e.g. [1,2,0])"))
                    vector1= vect1[0]*N.i + vect1[1]*N.j + vect1[2]*N.k
                    vector2= vect2[0]*N.i + vect2[1]*N.j + vect2[2]*N.k
                    vector3= vect3[0]*N.i + vect3[1]*N.j + vect3[2]*N.k
                    cross1= cross(vector1, vector2)
                    final= cross(cross1, vector3)
                    print("vector triple product is: ", final)
                
                elif subtaskcode=='stp':
                    N= CoordSys3D('N')
                    vect1= eval(input("enter vector 1 (e.g. [1,2,x])"))
                    vect2= eval(input("enter vector 2 (e.g. [y,z,x]: "))
                    vect3= eval(input("enter vector 3 (e.g. [1,2,0])"))
                    vector1= vect1[0]*N.i + vect1[1]*N.j + vect1[2]*N.k
                    vector2= vect2[0]*N.i + vect2[1]*N.j + vect2[2]*N.k
                    vector3= vect3[0]*N.i + vect3[1]*N.j + vect3[2]*N.k
                    cross1= cross(vector1, vector2)
                    final= vector3.dot(cross1)
                    print("scalar triple product is: ", final)

                    

        elif taskcode=='quit':
            loopbreaker=0             


    except Exception:
        print("invalid input: ", Exception)

root.mainloop()

