# This Python project counts the number of times a given substring appears in a main string, ensuring case-sensitive matching.

string = input('Enter a main string: ').strip()
sub_string = input('Enter a sub_string: ').strip()

def count_substring(string, sub_string):
    count = 0
    start = 0

    while True:
        start = string.find(sub_string, start)
        if start == -1:
            break
        count += 1
        start += 1

    return count

count = count_substring(string, sub_string)
print(f"The substring '{sub_string}' appears {count} times in the main string.")