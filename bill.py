import mysql.connector

mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'hoteldb')
mycursor = mydb.cursor() 
total=0
item=[]
l =[]
while(True):
    print("select an option:")
    print("1 tea--10")
    print("2 coffee--15")
    print("3 burger--30")
    print("4 pizza--50")
    print("5 shawarma--90")
    print("6 generate bill")
    print("7 view all transaction")
    print("8 view transaction in particular day")
    print("9 view transaction summary for a period")
    print("10 break")


    choice=int(input("enter the choice"))

    if(choice==1):
       print("tea selected")
       quantity=(int(input("enter the quantity")))
       total=10*quantity
       l.append(total)
       item.append("tea x"+str(quantity))
       print("quantity= ",quantity)
       print("total" ,total)
       

    elif(choice==2):
        print("coffeee selected")
        quantity=(int(input("enter the quantity")))
        total=15*quantity
        l.append(total)
        item.append("coffee x"+str(quantity))
        print("quantity= ",quantity)
        print("total" ,total)


    elif(choice==3):
        print("burger selected")
        quantity=(int(input("enter the quantity")))
        total=30*quantity
        l.append(total)
        item.append("burger x"+str(quantity))
        print("quantity= ",quantity)
        print("total" ,total)


    elif(choice==4):
        print("pizza selected")
        quantity=(int(input("enter the quantity")))
        total=50*quantity
        l.append(total)
        item.append("pizza x"+str(quantity))
        print("quantity= ",quantity)
        print("total" ,total) 

    elif(choice==5):
        print("shawarma selected")
        quantity=(int(input("enter the quantity")))
        total=90*quantity
        l.append(total)
        item.append("shawarma x"+str(quantity))
        print("quantity= ",quantity)
        print("total" ,total) 


    elif(choice==6):
         name = input('Enter the name : ')
         phone = input('Enter the phone number : ')
        #dates = input('Enter the date in the form of yyyy-mm-d : ')
         l1 = []
         l1.extend(l)
         count = 0
         for i in l1:
           count = count + i
           l.remove(i)
         amount = count
         # #print(f'Total amount {count} ')
         sql = "INSERT INTO `bills`(`name`, `Phone`, `amount`, `date`) VALUES (%s,%s,%s,now())"
         data = (name,phone,amount)
         mycursor.execute(sql,data)
         mydb.commit()
         print('Thank you Welcome to next time ')

    elif(choice==7):
        print("display the transactions")
        date = input("enter the date (yyyy-mm-d:")
        sql= "SELECT * FROM `bills` WHERE date ='"+date+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

    elif(choice==8):
        print("display the transaction summary of a date")
        date = input("enter the date (yyyy-mm-d:")
        sql = "SELECT SUM(`amount`), `date` FROM `bills` WHERE date = '"+date+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

    elif(choice==9):
        print("display the transaction summary for a period")
        date1 = input("enter the date (yyyy-mm-d:")
        date2 = input("enter the date (yyyy-mm-d:")
        sql = "SELECT SUM(`amount`) FROM `bills` WHERE date BETWEEN '"+date1+"' AND '"+date2+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

    elif(choice==10):
      break
    
