import operator

operatorlookup = { '+': operator.add, '-': operator.sub,
                   '*': operator.mul, '/': operator.truediv
}

def calc(num1=4, num2=5.7):
    print("Hello User Start Calculating")
    num1 = float(input("Input First Number:"))
    sig = input("Enter what you want to do")
    num2 = float(input("Input Second Number:"))
            
    if sig=='+' or sig=='-' or sig=='*' or sig=='/':
        #Checking For maybe addition or other
        op = operatorlookup.get(sig) 
        ans = op(num1, num2) 
        
    #If the user types something else
    else: 
        ans = "WRONG OPERATOR"
    print( str(num1) + str(sig) + str(num2) + " is " + str(ans))
        
while True:
    calc()



