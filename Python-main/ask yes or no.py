from urllib import response


def ask_yes_no(question):
    response = None
    while response not in("y","n"):
        response = input(question).lower()
        return response
    answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
    print("Thanks for entering:", answer)
