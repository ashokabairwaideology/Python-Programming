from unicodedata import name


score = []
user = name
choice = None
while choice != "0":
    print('''for list
          0 -- show
          1 -- add
          2 -- delete
          3 -- sort
          4 -- exit''')
    choice = input('enter your choice:')
    
    if choice == "0":
        print('show all list:')
        
        
    elif choice == "1":
        print('add  a list of user:')
        user = eval(input('enter the user name:'))
        score = int(input('enter the score:'))
        
    elif choice == "2":
        print('delete the score:')
        score.remove()
        
    elif choice == "3":
        
        score.sort(reverse=True)
        print('sorted the list:',list)
        
    elif choice == "4":
        print('good bye')
        
    else:
        print('you type invalid key,try again')
        
        
        
    
        
        
        
    
    