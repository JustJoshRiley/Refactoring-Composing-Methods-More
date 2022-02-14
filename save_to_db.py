# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")

def user_age(birth_year):
    return 2022 - birth_year

user_input = input('Please enter your username: ')
save_into_db(user_input)

user_input = int(input('Please enter your birth year: '))
print("You are",user_age(user_input), "years old.")