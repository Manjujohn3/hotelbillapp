import mysql.connector

mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'hoteldb')
mycursor = mydb.cursor() 
total=0
item=[]
while(True):
    print("select an option:")
    print("1 tea--10")
    print("2 coffee--15")
    print("3 burger--30")
    print("4 pizza--50")
    print("5 shawarma--90")
    print("6 generate bill")
    print("7 exit")

    choice=int(input("enter the choice"))

    if(choice==1):
       print("tea selected")
       quantity=(int(input("enter the quantity")))
       total+=10*quantity
       item.append("tea x"+str(quantity))
       #print("quantity= ",quantity)
       #print("total" ,total)
       

    elif(choice==2):
        print("coffeee selected")
        quantity=(int(input("enter the quantity")))
        total+=15*quantity
        item.append("coffee x"+str(quantity))
        #print("quantity= ",quantity)
        #print("total" ,total)


    elif(choice==3):
        print("burger selected")
    elif(choice==4):
        print("pizza selected")
    elif(choice==5):
        print("shawarma selected")
    elif(choice==6):
        print("generate bill")
    elif(choice==7):
        break
    
