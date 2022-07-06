statement  = input('enter any statement for analysis')
char_search = input('which character you want check for duplication: ')
count = 0
for letter in statement:
    if letter.lower() == char_search:
        count += 1

print(f'number duplicate character of {char_search} found are {count}')