# update 2
# update 1
# P2M5 Final Project
# Ezije Nwandu

def get_names():
    elements = []

    while len(elements) < 5:
        name = input("Enter the name of an element: ").lower().strip()

        if name == "":
            continue

        if name in elements:
            print(name, "was already entered")
        else:
            elements.append(name)

    return elements


# open the file
file = open("elements1_20.txt", "r")

elements_list = []

# read file line by line
for line in file:
    elements_list.append(line.strip().lower())

file.close()


print("Welcome Ezije Nwandu, list any 5 of the first 20 elements in the Periodic table")

# get user input
user_list = get_names()

correct = []
incorrect = []

# check answers
for item in user_list:
    if item in elements_list:
        correct.append(item)
    else:
        incorrect.append(item)

# calculate score
score = len(correct) * 20

print()
print(str(score) + " % correct")

# print results
if correct:
    print("Found:", " ".join([word.title() for word in correct]))

if incorrect:
    print("Not Found:", " ".join([word.title() for word in incorrect]))
