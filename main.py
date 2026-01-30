import random 

times_played = 1
def util(number_of_dices, curr_val, value_req, not_included):
    global times_played
    r = False
    while sorted(value_req) != sorted(curr_val):
        for i in range(number_of_dices):
            if i in not_included:
                continue
            numb = random.randint(1, 6)
            curr_val[i] = numb
            if(sorted(value_req) == sorted(curr_val)):
                print(f"Current Values {curr_val}")
                print(f"You did it! Took {times_played} tries")
                r = True
                break
        times_played +=1
        
        if r:
            break
        print(f"Current Values {curr_val}")
        keeped = input(f"What values would you want to keep? (1 to {number_of_dices} or if mutiple type out numbers with spaces inbetween or type none) \n")
        if keeped == 'none':
            continue
        else:
            for j in list(map(lambda x: x-1, map(int, list(keeped)))):
                    not_included.append(j)

def func():
    global times_played
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
            for i in range(number_of_dices):
                numb = random.randint(1, 6)
                curr_val.append(numb)

            print(f"Current Values {curr_val}")
            if(sorted(value_req) == sorted(curr_val)):
                print(f"You did it! Took {times_played} tries")
                return
            keeped = input(f"What values would you want to keep? (1 to {number_of_dices} or if mutiple type out numbers with spaces inbetween or type none) \n")
                
            if keeped == 'none':
                util(number_of_dices, curr_val, value_req, not_included)
            else:
                for j in list(map(lambda x: x-1, list(map(int, keeped.split())))):
                    not_included.append(j)
                util(number_of_dices, curr_val, value_req, not_included)
                        
        else:
            return
        
func()




