# *** The Boolening ***

# is_raining = False
# is_cold = True

# print(type(is_raining))
# print(type(is_cold))


# ********** NOT *****************

# is_raining = False
# is_cold = True

# print(type(is_raining)) 
# print(type(is_cold))

# just_the_word_true = "True"
# print(type(just_the_word_true))


# *** 🧠 The Logical Operators 🧠
# - not
# - or
# - and

# is_raining = False
# is_cold = True

# print(is_raining)
# print(not is_raining)

# ********** OR ***********************
# is_raining = False
# is_cold = True

# is_warm = False
# is_dry = True

# print(is_raining or is_warm)
# print(is_raining or is_cold)
# print(is_cold or is_dry)

# ********** AND ***********************

# is_raining = False
# is_cold = True

# is_warm = False
# is_dry = True

# print(is_raining and is_warm)
# print(is_raining and is_cold)
# print(is_cold and is_dry)


# **** ⚖️ The Comparison Operators ⚖️

# ********** == ***********
# print(5 == 3)
# print(5 == "five")
# print(5 == "5")
# print(5 == 2+3)
# print(5 == 5.0)
# print("five" == f"{'fi'}{'ve'}")

# ********** != ***********
# print(5 != 3)
# print(5 != "five")
# print(5 != "5")
# print(5 != 2+3)
# print(5 !=5.0)
# print("five" != f"{'fi'}{'ve'}")

# ********** < or > ***********

# print(3 < 3)
# print(4 < 3)
# print(3 < 3.0)
# print(3 < 99)
# print(3 < 2+2)
# print(3 < 4.0)

# print(3 > 3)
# print(4 > 3)
# print(3 > 3.0)
# print(3 > 99)
# print(3 > 2+2)
# print(3 > 4.0)

# ********** 💁 if 💁***********
# is_raining = True
# user_name = "Art"

# if is_raining:
#     print(f"Hey {user_name}, it's raining!") 
#     print("Better take an umbrella!")

# ********** 🤷‍♀️ else 🤷‍♀️ ***********
# is_raining = True
# user_name = "Art"

# if is_raining:
#     print(f"Hey {user_name}, it's raining!") 
#     print("Better take an umbrella!")
# else:
#     print(f"Hey {user_name}, it's sunny!") 
#     print("Better wear sunscreen!")


# ********** 🙃 elif 🙃 ***********
# temperature = float(input("What temperature is it?: "))
# user_name = input("What is your name?: ")

# if temperature<15:
#     print(f"Hey {user_name}, it's cold!") 
#     print("Better take a coat!")
# elif temperature>20:
#     print(f"Hey {user_name}, it's hot!") 
#     print("Better take a water bottle!")
# else:
#     print("Its April 25th. Not too hot, not too cold. All you need is a light jacket!")


# ********** 🤔 Truthiness And Falsiness 🤔 ***********
# user_name = input("What is your name?: ")

# if not user_name:
#     user_name = input("Wait... you just hit enter without typing anything. Really, what is your name?: ")