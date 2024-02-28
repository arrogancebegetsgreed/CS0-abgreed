#Basic Calculator using Functions and Auto Unit Testing
#Caine Mayhew CS0-abgreed
import math


def Calc():
    a = float(input("Enter a number"))
    b = float(input("Enter a number"))
     
    def Sum():
         return a+b
        
    print("The sum of your entered numbers is:", Sum())
    
    def Product():
        return a*b
    print("The product of your entered numbers is:", Product())
    
    def Quotient():
        return a/b
    print("The quotient of your entered numbers is", Quotient())
    
    def Difference():
        return a-b
    print("The difference of your entered numbers is:", Difference())
    
    def Remainder():
        return a % b
    print("The remainder of your entered numbers when divided is:", Remainder())
    
    def Power():
        return a**b
    print("The value of your first number to the power of your second number is:", Power())
    
    def Root():
        return math.sqrt(a)
    print("The square root of your first number is:", Root())

print(Calc())
