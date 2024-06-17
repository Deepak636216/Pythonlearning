
def CREDIT(customer_list, account_number, deposit_amount):
    for customer in customer_list:
        if customer[1] == account_number:
            customer[2] += deposit_amount
            print(f"Deposited {deposit_amount} into account {account_number}.")
            print(f"Updated balance: {customer[2]}")
            return
    print("Account not found!")

# Function to perform withdraw operation
def DEBIT(customer_list, account_number, debit_amount):
    for customer in customer_list:
        if customer[1] == account_number:
            if customer[2] >= debit_amount:
                customer[2] -= debit_amount
                print(f"Withdrew {debit_amount} from account {account_number}.")
                print(f"Updated balance: {customer[2]}")
            else:
                print("Insufficient balance!")
            return
    print("Account not found!")
