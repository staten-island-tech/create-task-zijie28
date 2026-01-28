import random 

def func():
    value_req = 0
    curr_val = 0
    try:
        number_of_dices = int(input("How many dices would you like to play with? \n"));  
    except ValueError:
        print("Type a number.")
        func();
    else:
        for i in range(number_of_dices):
            value_req += random.randint(1, 6)
        print(f"Required value to roll is {value_req}")
        if(input("Start? (y,n) \n") == "y"):
            start = True
            while start:
                
                for i in range(number_of_dices):
                    curr_val += random.randint(1, 6)
                ans = input(f'Current Value is {curr_val}. Would you like to go again? (y,n)')
                if ans == 'n':
                    break;
                elif ans == 'y':
                    pass
                if curr_val > value_req:
                    print(f"You lost, getting {value_req - curr_val} over")
                    break
                else:
                    print(f"You got {value_req - curr_val} close to {value_req}")
            
        else:
            return






