from multiprocessing.sharedctypes import Value


Tryagain = True
while Tryagain:
    try:
        value = int(input("enter the value:  "))
    except ValueError:
        print("you must try whole no. :  ")
        
        try:
            doOver = input("try again(y/n)")
        except:
            print("ok")
            Tryagain = False
        else:
            if (str.upper(doOver) == "N"):
                TryAgain = False
    except KeyboardInterrupt:
                print("You pressed Ctrl+C!")
                print("See you next time!")
                TryAgain = False
    else:
                print(value)
                TryAgain = False
        