def isvalid(string):
    if not(8<= len(string) <=20):
            return False

    if not any( char.islower() for char in string ):
            return False

    if not any( char.isupper() for char in string ):
            return False
   
    is_prev=False
    count=0
    for char in string:
        if char.isdigit():
            if is_prev:
                return False
            count+=1
            is_prev=True
        else:
            is_prev=False
    if count!=2:
        return False
   
    return True
def validity(lst):
    for string in lst:
        if isvalid(string):
            print(f"{string} is valid")
        else:
            print(f"{string} not valid")
   
def main():
    lst=input("Enter the passwords: ").split()
    (validity(lst))
main()
