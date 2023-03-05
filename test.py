import sqlite3
#Connect the sqlite to the database
conn = sqlite3.connect("database.db")
#Creating the table of Employee
c=conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS Employee(
    ID int,
    FirstName text,
    LastName text,
    City text,
    State text
)
""")
d1={"ID":10330,"FirstName":"John","LastName":"John","City":"NY","State":"NY"}
d2={"ID":10449,"FirstName":"Sarah","LastName":"Lebat","City":"Melbourne","State":"Bourke"}
d3={"ID":11012,"FirstName":"Jon","LastName":"Dallas","City":"NY","State":"NY"}
d4={"ID":11013,"FirstName":"Gheorge","LastName":"Honey","City":"NY","State":"NY"}
d5={"ID":11014,"FirstName":"Anton","LastName":"Savar","City":"NY","State":"NY"}
liste_01=[d1,d2,d3,d4,d5]

for i in liste_01:
    sql = "INSERT INTO Employee SELECT :ID, :FirstName, :LastName, :City, :State WHERE NOT EXISTS (SELECT 1 FROM Employee WHERE ID = :ID)"
    c.execute(sql,i)

#Creating the table of Payments  
c.execute(""" CREATE TABLE IF NOT EXISTS Payments(
    ID int,
    SalaryDate text,
    Month int,
    Value int
)
""")


p1={"ID":10330,"SalaryDate":"June","Month":6,"Value":128}
p2={"ID":10330,"SalaryDate":"July","Month":7,"Value":158}
p3={"ID":10330,"SalaryDate":"August","Month":8,"Value":133}
p4={"ID":10330,"SalaryDate":"September","Month":9,"Value":120}
p5={"ID":10330,"SalaryDate":"October","Month":10,"Value":188}
p6={"ID":10330,"SalaryDate":"November","Month":11,"Value":160}
p7={"ID":10330,"SalaryDate":"December","Month":12,"Value":105}
p8={"ID":10449,"SalaryDate":"September","Month":9,"Value":150}
p9={"ID":10449,"SalaryDate":"October","Month":10,"Value":158}
p10={"ID":10449,"SalaryDate":"November","Month":11,"Value":160}
p11={"ID":10449,"SalaryDate":"December","Month":12,"Value":180}

liste_02=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]

for i in liste_02:
    sql = "INSERT INTO Payments (ID, SalaryDate, Month, Value) SELECT :ID, :SalaryDate, :Month, :Value WHERE NOT EXISTS (SELECT * FROM Payments WHERE Value = :Value and Month = :Month and SalaryDate = :SalaryDate)"
    c.execute(sql,i)


#Display the total amount earned by each employee
c.execute("SELECT FirstName from Employee WHERE ID=10330")  
name=c.fetchone()
c.execute("SELECT LastName from Employee WHERE ID=10330")
surname=c.fetchone()

c.execute("SELECT SUM(Value) from Payments WHERE ID=10330")
summing=c.fetchall()
print("The amount earned by " + str(name) + " " +str(surname)+" is " + str(summing))


c.execute("SELECT FirstName from Employee WHERE ID=10449")
name=c.fetchone()

c.execute("SELECT LastName from Employee WHERE ID=10449")
surname=c.fetchone()

c.execute("SELECT SUM(Value) from Payments WHERE ID=10449")
summin=c.fetchall()
print("The amount earned by " + str(name) + " " +str(surname)+" is " + str(summin))

c.execute("SELECT * from Employee WHERE FirstName LIKE 'J%' ")
names=c.fetchall()
print("Names that start with J" + str(names))



conn.commit()
conn.close()