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
            for i in range(number_of_dices):
                curr_val
        else:
            return






