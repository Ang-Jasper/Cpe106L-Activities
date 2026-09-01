import random
import psycopg2

profit = 0.00


print("Welcome to BETTING ON ADDICTION. Dont wory, no one would know your here....")
suckers_account = input("Before starting, Enter the account where the money would come from(E-walle - account name): ")
print(f"-connection established-")
bet = float(input("Enter the amount you are betting today: "))
profit = profit + bet

while profit > 0:
    print(f"\n PICK YOUR POISON (you know why your here...):")
    print(f"1 - GAMBLE win or lose 10% of current balance")
    print("2 - Cash out")

    choice = input("Your choice: ").strip()

    match choice:
        case "1":
            user_call = input("Choose HEADS or TAILS (any other input will autolose hehe): ").strip()
            coin_result = random.choice(["HEADS", "TAILS"])

            match user_call == coin_result:
                case True:
                    if profit == 0.00:
                        choice == 2
                    else :
                        print("HIT")
                        profit = profit + (profit*0.10)
                    
                case False:
                    if profit == 0.00:
                        choice == 2
                    else :
                        print("MISS, ~ why dont you try again ~")
                    profit = profit - (profit*0.10)
                    

        case "2":
            print(f"\n --CASH OUT--")
            print(f"Total earnings: [{profit:.2f}]")
            print("GAMBLING LOG TERMINATED, ~ don't worry no one would know....")

            break  
        case _:
            print("Invalid Input, try again")

else:
    print("YOUR OUT OF MONEY")
    print("GAMBLING LOG TERMINATED, ~ don't worry no one would know....")
    

                