def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error! Division by Zero is not allowed."
    return a/b

while True:
    print("\n---Calculator---")
    print("\n1.Add    2.Sub    3.Multiply    4.Divide    5.Exit")

    choice=input("Enter your choice:")
    
    if choice=="5":
        print("Thank you for using Calculator")   
        break

    if choice not in ["1","2","3","4"]:
        print("Invalid Input! Please try again.")
        continue

    try:
        n1 = float(input("Enter a first number:"))
        n2 = float(input("Enter a second number:"))
    except ValueError:
        print("Please enrer valid numbers!")
        continue
    
    if choice=="1":
        print("Result:",add(n1,n2))

    elif choice=="2":
        print("Result:",sub(n1,n2)) 
    
    elif choice=="3":
        print("Result:",multiply(n1,n2)) 
    
    elif choice=="4":
        print("Result:",divide(n1,n2)) 

    



                           
                           
                           
                    