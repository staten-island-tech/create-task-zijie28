import random 

def func():
    value_req = []
    curr_val = []
    try:
        number_of_dices = int(input("How many dices would you like to play with? \n"));  
    except ValueError:
        print("Type a number.")
        func();
    else:
        for i in range(number_of_dices):
            num = random.randint(1,6)
            value_req.append(num)
        print(f"Required values to roll are {value_req}")
        if(input("Start? (y,n) \n") == "y"):
            start = True
            while start:
                for i in range(number_of_dices):
                    numb = random.randint(1, 6)
                    curr_val = numb
                    
        else:
            return






