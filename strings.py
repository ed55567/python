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


# Formatting Methods

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()

print(poem_author)
print(poem_author_fixed)

# Splitting Strings
line_one = "The sky has given over"

line_one_words = line_one.split()


# Splitting Strings II
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

# Joining Strings
reapers_line_one_words = ["Black", "reapers", "with",
                          "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)

# Joining Strings II
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among',
                      'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)

# strip

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ',
                    'you lay down your arms', '           like flowering mines    ', '\n', '   to conquer me home.    ']


love_maybe_lines_stripped = []

for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)


# replace

toomer_bio = \
    """
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")


def poem_title_card(title, poet):
    poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
    return poem_desc


def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
        publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc


author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(
    publishing_date, author, title, original_work)

print(my_beard_description)


# all

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(':'))

titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
    titles.append(poem[0])
    poets.append(poem[1])
    dates.append(poem[2])

for i in range(0, len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(
        titles[i], poets[i], dates[i]))
