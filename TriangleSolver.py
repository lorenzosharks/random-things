"""
Honors Geometry 
Triangle Solver Skeleton (v.3.0) 1.26.2024
"""

######  TOOLS ###### 
## IMPORT LIBRARIES/MODULES ##
# math module to use python's trig functions
import math
## FUNCTIONS ##
# python's trig functions use radian measure instead of degree measure,
# the following four functions just make trig work in degrees.

def cos(degreeAngle):
    """
    Calculates the cosine of an angle in degrees
    parameters: angle in degrees (float)
    return: cosine of the angle (float)
    """     
    ratio = math.cos(math.radians(degreeAngle))
    return ratio

def sin(degreeAngle):
    """
    Calculates the sine of an angle in degrees
    parameters: angle in degrees (float)
    return: sine of the angle (float)
    """ 
    ratio = math.sin(math.radians(degreeAngle))
    return ratio

def inverseCos(ratio):
    """
    Calculates the degree angle measure given a ratio using cosine
    parameters: ratio (float)
    return: angle in degrees (float)
    """ 
    angle = math.degrees(math.acos(ratio))
    return angle
    
def inverseSin(ratio):
    """
    Calculates the degree angle measure given a ratio using sine
    parameters: ratio (float)
    return: angle in degrees (float)
    """     
    angle = math.degrees(math.asin(ratio))
    return angle    

def SSS(a,b,c):
    """
    Calculates all angles in valid SSS scenarios
    parameters: a = side, b = side, c = side    
    return: list with the six triangle parts    
    """ 
    # use law of Cosines to find angle A    
    A = inverseCos((a*a - b*b - c*c)/(-1*2*b*c))
    # use law of Cosines to find angle B    
    B = inverseCos((b*b - a*a - c*c)/(-1*2*a*c))
    # use sum of triangle angles is 180 to find C    
    C = 180 - A - B    
    # return all six pieces of triangle information as a list
    return [a,b,c,A,B,C]

def ASA(A,c,B):
    """
    Calculates missing angles and sides in valid ASA scenarios
    parameters: A = angle, c = side, B = Angle 
    return: list with the six triangle parts
    """    
    # use sum of triangle angles is 180 to find C
    C = 180 - A - B
    # use Law of Sines to find b
    b = c * sin(B)/sin(C)
    # use Law of Sines to find a
    a = c * sin(A)/sin(C)    
    # return all six pieces of triangle information as a list
    return [a,b,c,A,B,C]
    
def AAS(A,B,a):
    """
    Calculates missing angles and sides in valid AAS scenarios
    parameters: A = angle, B = angle, a = Side 
    return: list with the six triangle parts
    """    
    C = 180 - A - B
    
    x = ASA(B,a,C) 
    """
    Because the result of ASA is a list,
    x would be a list.
    """
    return [a,x[0],x[1],A,B,C] 
    """
    Since x is a list from the above comment,
    you can call x[0] (the first element) and
    x[1] (the second element) from x.
    """
    """
    Why AAS works
    If we look back to the result of the ASA function,
    we can see that the first and second element
    of the result is the 2 other sides of the
    triangle. However, in the function AAS, we only need
    to calculate the degree of the missing angle, which
    is already done. Therefore, we only need to solve for
    the 2 other sides but instead of solving for them again,
    we can grab the value of the 2 sides by calling them
    from the ASA function which already solves for them.
    This means we save a lot of space as well as have a
    organized code.
    """
    
def SAS(a,C,b):
    """
    Calculates missing angles and sides in valid SAS scenarios
    parameters: a = side, B = angle, c = Side 
    return: list with the six triangle parts
    """        
    c=((a**2)+(b**2)-(2*a*b*cos(C)))**0.5
    Z=SSS(a,b,c)
    return [a,b,c,Z[3],Z[4],C]

def SSA(a,b,A):
    """
    Calculates missing angles and sides in valid SSA scenarios
    parameters: a = side, b = side, A = Angle 
    return: If it indeed is a SSA case, it will say it is not possible
    """
    w=-2*b*(cos(A))
    c=(-w+((w**2)-(4*((b**2)-(a**2))))**0.5)/2
    Y=SSS(a,b,c)
    return[a,b,c,A,Y[4],Y[5]]
   
def welcome():
    """
    Prints welcome message and a menu of options 
    parameters: none
    return: none    
    """     
    print("""
This program solves triangles!
Based on specific information provided by the user about a triangle,
this program reports all sides & angles for the triangle or reports why the triangle cannot be solved.
Note: for the SSA scenario, the program reports when two triangles are possible but does not solve both triangles.

Consider a triangle ABC with sides and angles denoted in the typical way.
What triangle information do you have?    
 (1) SSS
 (2) SAS
 (3) ASA
 (4) AAS
 (5) SSA
 """) 

def userChoice(): 
    """
    Gets a valid choice from the user from a list of triangle scenarios
    parameters: none    
    return: a response from the list of numerical choices (str)   
    """     
    validChoice = False 
    while validChoice == False:
        userInput = input("Select an option 1 through 5: ")    
        if userInput == "1" or userInput == "2" or userInput == "3" or userInput == "4" or userInput == "5":
            validChoice = True
        else: 
            print("Please enter a number 1 through 5! Try again.")
    return userInput

def getInput(sideAngle,ABC):
    """
    Asks the user for a specific side or angle
    parameters: sideAngle = "side" or "angle", ABC = the specific side/angle
    return: a user input (float) for the measure of the side or angle.
    """     
    print() #Adds blank line to match difftool
    return(float(input("enter " + sideAngle + " " + ABC + ": ")))
        
def solveTriangle(userInput): 
    """
    Based on user's choice, returns a message with triangle information OR an error message
    parameters: userChoice (str)   
    return: all sides and angles (list) or error message (str)
    """  
    if userInput == "1":
        print("You chose SSS")  
        a = getInput("side","a")
        b = getInput("side","b")
        c = getInput("side","c")
        if a <=0 or b<=0 or c<= 0:
            triangleInfo = "No triangle: one or more given sides are 0 or negative."            
        elif a + b <= c or a + c <= b or b + c <= a:
            triangleInfo = "No triangle: triangle inequality is not satisfied."
        else:
            triangleInfo = SSS(a,b,c)        
    elif userInput == "2":
        print("You chose SAS")  
        a = getInput("side","a")
        C = getInput("angle","C")
        b = getInput("side","b")        
        if a <= 0 or b <= 0:
            triangleInfo = "No triangle: one or more given sides are 0 or negative."                
        elif C <= 0:
            triangleInfo = "No triangle: one or more given angles are too small or too big"
        else:
            triangleInfo = SAS(a,C,b)
    elif userInput == "3":
        print("You chose ASA")  
        A = getInput("angle","A")
        c = getInput("side","c")
        B = getInput("angle","B")
        if c <= 0:
            triangleInfo = "No triangle: one or more given sides are 0 or negative."                
        elif A <= 0 or B <= 0 or A + B >=180:
            triangleInfo = "No triangle: one or more given angles are too small or too big."
        else:
            triangleInfo = ASA(A,c,B)  
    elif userInput == "4":
        print("You chose AAS")  
        A = getInput("angle","A")
        B = getInput("angle","B")
        a = getInput("side","a")        
        if a <= 0:
            triangleInfo = "No triangle: one or more given sides are 0 or negative."                
        elif A <= 0 or B <= 0 or A + B >=180:
            triangleInfo = "No triangle: one or more given angles are too small or too big."
        else:
            triangleInfo = AAS(A,B,a)          
    elif userInput == "5":
        print("You chose SSA")  
        a = getInput("side","a")
        b = getInput("side","b")
        A = getInput("angle","A")
        if a<=0 or b<=0:
            triangleInfo="No triangle: one or more given sides are 0 or negative."
        elif A>=180 or A<=0:
            triangleInfo="No triangle: one or more given angles are too small or too big."
        elif A<90:
            if sin(A)>(a/b):
                triangleInfo="No triangle: leg a is shorter than the altitude from C."
            elif a<b:
                triangleInfo="Ambiguous case: two triangles can be formed with this information."
            elif a>b:
                triangleInfo=SSA(a,b,A)
        elif A>=90:
            if a<=b:
                triangleInfo="No triangle: leg a is too short with that non-acute angle A."
            elif a>b:
                triangleInfo=SSA(a,b,A)
    return triangleInfo


def results(summary) :
    print("")
    print("Results for your triangle ABC:") #blank line to match difftool
    if type(summary) == list:
        print("Sides:  a = " + str(round(summary[0],2)) + ", b = " + str(round(summary[1],2)) + ", c = " + str(round(summary[2],2)))
        print("Angles: A = " + str(round(summary[3],2)) + ", B = " + str(round(summary[4],2)) + ", C = " + str(round(summary[5],2)))
    else:
        print(summary)
        
     

######  MAIN PROGRAM ###### 

# Program summary & a menu of options (triangle cases)
welcome()

## INPUTS ##
#Get a triangle case from the user
selectedChoice = userChoice()

## CALCULATIONS ##
# get the triangle information based on user choice & then save triangle outcome (values or error) as variable
triangleSummary = solveTriangle(selectedChoice)

## OUTPUTS ##
# print the results to the console in an easy-to-read format
results(triangleSummary)  