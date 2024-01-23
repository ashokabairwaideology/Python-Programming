# def my_function(fname):
#   print(fname + " tere liye")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")



def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")