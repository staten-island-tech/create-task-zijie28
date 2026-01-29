import random 


def util(number_of_dices, curr_val, value_req, not_included, times_played):
    for i in range(number_of_dices):
        if i in not_included:
            continue
        numb = random.randint(1, 6)
        print(i)
        curr_val[i] = numb
        times_played +=1
        if(value_req == curr_val):
            print(f"You did it! Took {times_played} tries")
            break

        print(f"Current Values {curr_val}")
        keeped = list(input(f"What values would you want to keep? (1 to {number_of_dices}) "))
        if keeped[0] == "none":
            continue
        else:
            not_included.append(list(map(lambda x: x-1, map(int, keeped))))

def func():
    value_req = []
    curr_val = []
    not_included = []
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
            times_played = 0
            while start:

                for i in range(number_of_dices):
                    numb = random.randint(1, 6)
                    curr_val.append(numb)
                print(f"Current Values {curr_val}")
                if(value_req == curr_val):
                    print(f"You did it! Took {times_played} tries")
                    break
                keeped = list(input("What values would you want to keep?"))
                if keeped[0] == 'none':
                    pass
                else:
                    not_included.append(list(map(lambda x: x-1, map(int, keeped))))
                util(number_of_dices, curr_val, value_req, not_included, times_played)

                
                    
        else:
            return
        
func()




