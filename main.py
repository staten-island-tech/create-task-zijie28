import random 



def func():
    times_played = 1
    value_reqirement = []
    current_value = []
    not_included = []
    def logic(value_reqirement, current_value, number_of_dices, times_played, not_included):
        r = False
        while sorted(value_reqirement) != sorted(current_value):
            for i in range(number_of_dices):
                if i in not_included:
                    continue
                numb = random.randint(1, 6)
                try:
                    current_value[i] = numb
                except IndexError:
                    current_value.append(numb)
                if(sorted(value_reqirement) == sorted(current_value)):
                    print(f"Current Values {current_value}")
                    print(f"You did it! Took {times_played} tries")
                    r = True
                    break
            times_played +=1
            
            if r:
                break
            print(f"Current Values {current_value}")
                    
            keeped = input(f'What values would you want to keep? (1 to {number_of_dices} (position) or if mutiple type 
                            out numbers with spaces inbetween or type none) \n')
            if keeped == 'none':
                continue
            else:
                for j in list(map(lambda x: x-1, map(int, keeped.split()))):
                    not_included.append(j)
        return
    

    try:
        number_of_dices = int(input("How many dices would you like to play with? \n"));  
    except ValueError:
        print("Type a number.")
        func();
    else:
        for i in range(number_of_dices):
            num = random.randint(1,6)
            value_reqirement.append(num)
        print(f"Required values to roll are {value_reqirement}")
        if(input("Start? (y,n) \n") == "y"):
            logic(value_reqirement, current_value, number_of_dices, times_played, not_included)

                        
        else:
            return
        
func()




