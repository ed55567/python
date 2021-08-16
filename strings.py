first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]

temp_password = last_name[2:6]

# Concatenating Strings

first_name = "Julie"
last_name = "Blevins"


def account_generator(first_name, last_name):
    account_name = first_name[:4] + last_name[:5]
    return account_name


new_account = account_generator(first_name, last_name)

print(new_account)


# More and More String Slicing
first_name = "Reiko"
last_name = "Matsuki"


def password_generator(first_name, last_name):
    temp_password = first_name[len(first_name)-3:] + \
        last_name[len(last_name)-3:]
    return temp_password


temp_password = password_generator(first_name, last_name)

print(temp_password)


first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R"

fixed_first_name = "R" + first_name[1:]


# Strings are Immutable

first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R"

fixed_first_name = "R" + first_name[1:]

print(fixed_first_name)


def get_length(word):
    counter = 0
    for letter in word:
        counter += 1
    return counter


def letter_check(word, letter):
    for character in word:
        if character == letter:
            return True
    return False


def contains(big_string, little_string):
    return little_string in big_string


def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name


def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
