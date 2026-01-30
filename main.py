import random 



def func():
    times_played = 1
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
            r = False
            while sorted(value_req) != sorted(curr_val):
                for i in range(number_of_dices):
                    if i in not_included:
                        continue
                    numb = random.randint(1, 6)
                    try:
                        curr_val[i] = numb
                    except IndexError:
                        curr_val.append(numb)
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
                        
        else:
            return
        
func()




