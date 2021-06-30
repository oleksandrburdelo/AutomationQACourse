vegans = 'Oleksandr', 'Daryna', 'Denys'
meat_and_vegetable_lovers = 'Petro', 'Ganna', 'Serhii'

people = [vegans, meat_and_vegetable_lovers]

for index in people:
    for index2 in index:
        print(index2)

# Interesting solution but you have to create new one list of people who can
# each vegetables. Tuple is not the best data type for this task.
