# Prepare valid user name and password dictionary. (You can chage items.)
valid_users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}


def check_username_and_password(user_name, password):
    """This function checks if provided user name and password is correct."""
    if valid_users.get(user_name):
        if valid_users[user_name] == password:
            print("User name and password is correct")
            return True
        else:
            print("Wrong password")
            return False
    else:
        print("Wrong user name")
        return False


# ---Part1----
# Get user name and password
valid = False
max_try = 3
try_count = 0
valid = False
while not valid:
    try_count += 1
    try:
        print("-----------------")
        user_name = input("Please enter your user name:")
        password = input("Please enter your password:")
        valid = check_username_and_password(user_name, password)
    except:
        print("You have did not provide a correct username and password")

    if (try_count == max_try):
        break
    elif (not valid):
        print("You have {0} tries left".format(max_try - try_count))

if valid:
    print("You have logged in !")
else:
    print("You did not provide correct input.")
