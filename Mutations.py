
#This code takes a string input from the user, changes the character at a specified index, and then prints the modified string.

def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    new_string = ''.join(string_list)

    return new_string


s = input('please write a string: ')
i, c = input('please provide index and character: ')
s_new = mutate_string(s, int(i), c)
print(s_new)