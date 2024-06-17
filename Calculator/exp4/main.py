add=""
delete=""
lst=[]
while add!="n":
    add=input("Do you want to add customer details y/n: ")
    if add=="y":
        name=input("Enter the name: ")
        age=int(input("Enter the age: "))
        address=input("Enter the address: ")
        city=input("Enter the city: ")
        val=[name,age,address,city]
        lst.append(val)
print(lst)
while delete!="n":
    delete=input("Do u want to remove a customer details y/n: ")
    if delete=="y":
        name=input("Enter the customer to be removed: ")
        for customer in lst:
            if customer[0]==name:
                lst.remove(customer)
print(lst)  