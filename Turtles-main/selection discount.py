'''For example, let’s ask the user about their choice of cinema or theater.
You have to pay 10 dollars to watch movies and 5 dollars for theater.
We think that students get 50% discount.
If the student is discounted;
If he is not a student,
let’s write a document that calculates the non-discounted amount and prints it.'''


selection = input("Press (1) for Cinema, (2) for Theater : ")
student = input("Are you student(Y/N) : ")
price = 0
#non-discounted fee calculation
if selection == '1':
    price = 10 #cinema
elif selection == '2':
    price = 5 #theatre
#student discount
if student =='Y' or student =='y':
    price=price / 2  #%50
print(" The fee you have to pay :{}".format(price))
