
def create_customer_list():
    customer_list = []
    N = int(input("Enter the number of customers: "))
    
    for _ in range(N):
        name = input("Enter customer name: ")
        account_number = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))
        customer = [name, account_number, balance]
        customer_list.append(customer)
    
    return customer_list
