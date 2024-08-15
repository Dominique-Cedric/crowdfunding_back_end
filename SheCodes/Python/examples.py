# def jellybean_check(user_guess: int):
#     correct_answer = 9001
#     return user_guess == correct_answer
# print(jellybean_check(9001))


# print(jellybean_check(9001))

def jellybean_check(user_guess: int):
    correct_answer = 9001
    if user_guess == correct_answer:
        print("Correct! You wins ome jellybeans! :)")
    elif user_guess < 0:
        print("That's a dumb guess")
    else:
        print("Sorry, try again")

user_input = int(input("Guess how many beans in the jar: "))
jellybean_check(user_input)
