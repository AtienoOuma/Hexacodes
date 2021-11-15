stay="she begged her saying\"baby please stay\" and she just looked at him with a firece look and left"
print(stay)
name="Atieno Ouma"
print(name.capitalize())

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics").split())

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
print(len(verse))
print(verse.find("and"))
print(verse.count("you"))
print(verse.rfind("you"))
print(verse.find("you"))
# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
bio="this is me talking about myself and my likes in life"
print("myself" in bio)

VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']
print('GE' in VINIX)
print(sorted(VINIX,reverse=True))
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
hello="\n".join(VINIX)
print(hello)
play=(45,43,33,45,22,1,7,8)
print(type(play))

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
