# main.py
import Bank
import Transaction
# Create a list of customer details
customer_list = Bank.create_customer_list()

while True:
    print("\nChoose Transaction:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        account_number = input("Enter account number: ")
        deposit_amount = float(input("Enter deposit amount: "))
        Transaction.CREDIT(customer_list, account_number, deposit_amount)
    elif choice == 2:
        account_number = input("Enter account number: ")
        debit_amount = float(input("Enter debit amount: "))
        Transaction.DEBIT(customer_list, account_number, debit_amount)
    elif choice == 3:
        break
    else:
        print("Invalid choice!")

# Print the final list of customer details
print("\nFinal Customer Details:")
for customer in customer_list:
    print(f"Name: {customer[0]}, Account Number: {customer[1]}, Balance: {customer[2]}")
