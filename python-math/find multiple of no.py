import numbers

# numbers ={55,56,57,58,59,60}

for numbers in range(100):
    # for numbers in numbers:
        if numbers%4==3:
          if numbers%5==4:
            if numbers%6==5:
               print("answer will be number",format(numbers))