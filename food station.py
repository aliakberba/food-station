def menu():
    
    print("Our Menu Is : ")

    print("""Fast Food: 
          1.Fries                  Rs.120/-
          2.Zinger Burger          Rs.400/-
          3.Pizza(Large Only)      Rs.1200/-
          4.Club Sandwich          Rs.300/-
          5.Broast                 Rs.400/-
          6.Rolls                  Rs.170
                                               """)
    
    print(""" Deserts:
          7.Shakes                Rs.180/-
          8.Ice-Cream             Rs.150/-
          9.Custard               Rs.220/-  """)
          
 
    print(""" Beverages:
          10.Drinks/Water          Rs.50/- """)
          
def deals():
    print("""Deal A:
          Pizza
          fries
          drink
          
          price = 1400/-  """)
          
    print("""Deal B:
          Zinger Burger
          fries
          drink
          
          price = 600/-  """)
          
    print("""Deal C:
          Zinger Burger
          Broast
          drink
          
          price = 900/-  """)     
                            
          
    print("""Deal D:
          Zinger Burger
          Ice-cream
          pizza
          Broast
          drink
          
          price = 2000/-  """)     
    


def calculation_menu():
    
    total=0
    items=0
    while True:
        i=input("\nPress E/e to exit or press any key to continue your order placment = ")
        if(i!="E" and i!="e"):
        
            item=int(input("enter your item number ="))
            quantity=int(input("How much quantity ? = "))
            
            if(item==1):
                bill=120*quantity
                total=total+bill
                items=items+quantity
                
                
            elif(item==2):
                bill=400*quantity
                total=total+bill
                items=items+quantity
                
            elif(item==3):
                bill=1200*quantity
                total=total+bill
                items=items+quantity
                
            elif(item==4):
                bill=300*quantity
                total=total+bill 
                items=items+quantity
                
            elif(item==5):
                bill=400*quantity
                total=total+bill
                items=items+quantity
                
            elif(item==7):
                bill=180*quantity
                total=total+bill
                items=items+quantity    
            
            elif(item==8):
                bill=150*quantity
                total=total+bill
                items=items+quantity
                
            elif(item==9):
                bill=220*quantity
                total=total+bill
                items=items+quantity  
    
            elif(item==10):
                bill=50*quantity
                total=total+bill
                items=items+quantity
                
            elif(item==6):
                bill=170*quantity
                total=total+bill
                items=items+quantity
         
            
     
        else:
           
            print("your total items is  = " , items)
            
            print("Your total bill is = ",total)
            discount(total)
            
            break
      

def discount(total):
    discount=0
    
    if(total>=1500 and total<=2000):
        discount=total*(10/100)
        total=total-discount

    elif(total>=2001 and total<=3000):
        discount=total*(15/100)
        total=total-discount
        
    elif(total>=3001 and total<=4000):
        discount=total*(20/100)
        total=total-discount

    elif(total>4000):
        discount=total*(25/100)
        total=total-discount
    print("Your total bill after discount = ",total)

   
            
           
            
           
            

def calculation_deals():

    total=0
    items=0
    
    while True:
        i=input("\nPress E/e to exit or press any key to continue your order placement ! = ")
        if(i!="E" and i!="e"):
            
            item=(input("Enter your deal (A/B/C/D) = "))
            quantity=int(input("How much quantity ? = "))
            
            if(item=="A" or item=="a"):
                bill=1400*quantity
                total=total+bill
                items=items+quantity
                print("your total deals is =",items)
                print("Your total bill is = ",bill)
                
            elif(item=="B" or item=="b"):
                bill=600*quantity
                total=total+bill
                items=items+quantity
                print("your total deals is =",items)
                print("Your total bill is = ",bill)
                
            elif(item=="C" or item=="c"):
                bill=900*quantity
                total=total+bill
                items=items+quantity
                print("your total deals is =",items)
                print("Your total bill is = ",bill)
                
            elif(item=="D" or item=="d"):
                bill=2000*quantity
                total=total+bill
                items=items+quantity
                print("your total deals is =",items)
                print("Your total bill is = ",bill)
                
        else:
            print("your total items is  = " , items)
            
            print("Your total bill is = ",total)
            discount(total)
            
            break
      
       
          
            
            
            
            
            





                 ###### Main Code ######

print(" WELCOME TO FOOD STATION ")
print()

print(" Hello Sir ! \n Would you like to : \nA. Dine in \nB. Home Delivery  ")
print("\nPress A for Dine In \nPress B for Home dilevery ")
d=input("Press = ")


if(d=="A" or d=="a"):
    
    reserved=input("Sir ! Enter the number of person to be reserved = ")
    
    print("Here is your", reserved , "persons table ! ")
    print()
    
    print("Do you prefer deals or items to be choosen manually ?  ")
    
    print("Press d for Deals \nPress m for manually")
    
    choice=input("Press = ")
    
    if(choice=="d" or choice=="D"):
        print("Here is our deals ! ")
        deals()
        calculation_deals()
        
    elif(choice=="m" or choice=="M"):
        print("Here is our menu ! ")
        menu()
        calculation_menu()

elif(d=="B" or d=="b"):
    
    print("Do you prefer deals or items to be choosen manually ?  ")
    
    print("Press d for Deals \nPress m for manually")
    
    choice=input("Press = ")
    
    if(choice=="d" or choice=="D"):
        print("Here is our deals ! ")
        deals()
        calculation_deals()
        
    elif(choice=="m" or choice=="M"):
        print("Here is our menu ! ")
        menu()
        calculation_menu()
    
    print()
    print("Please share your information for order dilevery")
    name=input("Enter your Name = ")
    address=input("Enter your Address = ")    
    number=int(input("Enter your contact number = "))
    print()
    print("Your order details are : ")
    print("Name: ",name)
    print("Address: ",address)
    print("Number: " ,number)
    print("Your order will be dilevered in 30 minutes")
    print("Thankyou ! for choosing Food Station")
    print("Enjoy Your Meal ..!!!")

