#statements:
#condition statement:if , if-else,nested if,elif
#if:used to check statement true or false
num = 9
if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")

    
kusu_SBI_details = {"ATM PIN":'9000'}
pin_ = input("Enter your 4 digit ATM pin:")
if pin_ in kusu_SBI_details['ATM PIN']:
    print("Welcome to SBI ATM")
else:
    print("You have entered incorrect pin")
#nested if:
kusu_SBI_details = {"ATM PIN":'9000'}
pin_ = input("enter your 4 digit Atm pin: ")
if len(pin_) == 4:
    if pin_ in kusu_SBI_details['ATM PIN']:
       print("WELCOME")
    else:
        print("enter valid pin")
else:
        print("enter 4 digit valid pin only.")
#elif:
marks_ = 90
if marks_ >=90:
    print("A+")
elif marks_ >=80:
    print("A")
elif marks_ > 70:
    print("B+")    
else:
    print("failed")


