import mysql.connector as mys

mycon = mys.connect(
                     host = "localhost",
                     user = "root",
                     password = "admin",
                     database = "hospital"
                     )
mycursor=mycon.cursor()

def all():        
    hs=input("Enter the State:")
    q1="select Number_of_Government_Hospital,Number_of_LocalBody_Hospital,Number_of_Other_Hospital from ayushhospital where State_or_UT='{}'".format(hs)
    mycursor.execute(q1)
    data=mycursor.fetchall()
    for i in data:
        print("The government hospitals are",i[0])
        print("The local hospitals are",i[1])
        print("The other hospitals are",i[2])
    
    
def beds1():
    hs=input("Enter the State:")
    q1="select Number_of_beds_in_Government_Hospital,Number_of_beds_in_LocalBody_Hospital,Number_of_beds_in_Other_Hospital from ayushhospital where State_or_UT='{}'".format(hs)
    mycursor.execute(q1)
    data=mycursor.fetchall()
    for x in data:
        print("The beds in government hospitals are",x[0])
        print("The beds in local hospitals are",x[1])
        print("The beds other hospitals are",x[2])

def gov():
    hs=input("Enter the State:")
    q1="select Number_of_Government_Hospital,Number_of_beds_in_Government_Hospital from ayushhospital where State_or_UT='{}'".format(hs)
    mycursor.execute(q1)
    data=mycursor.fetchall()
    for x in data:
        print("The number of Government Hospitals are",x[0])
        print("The number of beds in Government Hospital are",x[1])

def local1():
    hs=input("Enter the State:")
    q1="select Number_of_LocalBody_Hospital,Number_of_beds_in_LocalBody_Hospital from ayushhospital where State_or_UT='{}'".format(hs)
    mycursor.execute(q1)
    data=mycursor.fetchall()
    for x in data:
        print("The number of Local Hospitals are",x[0])
        print("The number of beds in Local Hospital are",x[1])

def other():
    hs=input("Enter the State:")
    q1="select Number_of_Other_Hospital,Number_of_beds_in_Other_Hospital from ayushhospital where State_or_UT='{}'".format(hs)
    mycursor.execute(q1)
    data=mycursor.fetchall()
    for x in data:
        print("The number of Other Hospitals are",x[0])
        print("The number of beds in Other Hospital are",x[0])
    

    



print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~WELCOME~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
print("1. Search Hospitals in a particular State or Union Territory")
print("2. Search Beds in a particular State or Union Territory")
print("3. Search only Government number of Hospital and Number of Beds in Government Hospital")
print("4. Search only Local number of Hospital and Number of Beds in Local Hospital")
print("5. Search only Other number of Hospital and Number of Beds in Other Hospital")
print("6. Exit")
n=int(input("Enter your choice(num):"))


while n>0:
    if n==1:
        all()
        ch=input("Do you want to continue y/n:")
        if ch=='n':
            n=int(input("Enter your choice:"))
            
            
    if n==2:
        beds1()
        ch=input("Do you want to continue y/n:")
        if ch=='n':
            
            n=int(input("Enter your choice:"))
    if n==3:
        gov()
        ch=input("Do you want to continue y/n:")
        if ch=='n':
            
            n=int(input("Enter your choice:"))
    if n==4:
        local1()
        ch=input("Do you want to continue y/n:")
        if ch=='n':
            
            n=int(input("Enter your choice:"))
    if n==5:
        other()
        ch=input("Do you want to continue y/n:")
        if ch=='n':
            
            n=int(input("Enter your choice:"))
    if n==6:
        break
    
