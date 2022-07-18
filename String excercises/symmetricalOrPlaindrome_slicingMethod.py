string = ("amama")
half = int(len(string) / 2)
if len(string) % 2 == 0:  # even
    first_str = string[:half]
    second_str = string[half:]
else:  # odd
    first_str = string[:half]
    second_str = string[half+1:]

#symmetric 
if first_str == second_str:
    print (string, "string is symmetrical")
else:
    print(string, 'string is not symmertical')

#palindrome
if first_str == second_str[::-1]:
    print (string, 'string is a pallindrome')
else:
    print (string, 'is not a pallindrome')