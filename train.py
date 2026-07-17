print("RAILWAY TICKET RESERVARION")
name=input("enter the name: ")
age=int(input("enter the age: "))
gender=input("enter the gender(male/female): ")
train=input("enter the train name: ")
source=input("enter the source name: ")
destination =input("enter the detination: ")

ticket_price=500
if age < 5:
    fare=0
    print("\nchild below 5 years -free ticket")
elif age >=60:
    fare =ticket_price *0.5
    print("\nolder person - 50% Discount")
else:
    print(ticket_price)


print("passenger name: ",name)
print("age: ",age)
print("gender ",gender)
print("tarin name ",age)
print("from ",source)
print("to :",destination)
print("ticket fare :rs.",fare)
print("reservation status :CONFIRMED")
