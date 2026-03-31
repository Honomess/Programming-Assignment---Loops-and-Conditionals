
# 4.1
# Choose a number between 1 and 10 and assign it to the variable secret.
# Choose another number between 1 and 10 and assign it to guess.
# Use if/elif/else to print:
# 'too low' if guess < secret
# 'too high' if guess > secret
# 'just right' if guess == secret

secret = 7
guess = 5

if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')


# 4.2
# Assign True or False to variables small and green.
# Use if/else statements to identify which fruit/vegetable matches:
# cherry, pea, watermelon, pumpkin

small = True
green = False

if small and not green:
    print('cherry')
elif small and green:
    print('pea')
elif not small and green:
    print('watermelon')
else:
    print('pumpkin')


# 6.1
# Use a for loop to print the values of the list [3, 2, 1, 0]


for value in [3, 2, 1, 0]:
    print(value)


# 6.2
# Assign 7 to guess_me and 1 to number.
# Use a while loop to compare number with guess_me:
# - print 'too low' if number < guess_me
# - print 'found it!' if equal and exit loop
# - print 'oops' if number > guess_me and exit loop
# Increment number at the end of each loop


guess_me = 7
number = 1

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    number += 1



# 6.3 
# Assign 5 to guess_me.
# Use a for loop over range(10):
# - print 'too low' if number < guess_me
# - print 'found it!' and break if equal
# - print 'oops' and exit loop if number > guess_me


guess_me = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break