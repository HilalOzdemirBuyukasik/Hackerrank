
"""
The Minion Game - Python Implementation

This script solves the 'Minion Game' problem where two players, Kevin and Stuart,
compete by forming substrings from a given uppercase string.

Game Rules:
- Kevin scores points for substrings starting with vowels (A, E, I, O, U).
- Stuart scores points for substrings starting with consonants.
- Each substring's score equals the number of times it appears in the original string, calculated efficiently as (len(string) - current index).

Instead of generating all substrings (which is inefficient), this solution
uses an optimized O(n) approach by calculating the number of substrings that
start at each index.

Example:
Input: BANANA
Output: Stuart 12

Usage:
- Run the script and input an uppercase string.
- Output will be the winner's name and score, or 'Draw' if tied.

"""

def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif stuart_score > kevin_score:
        print('Stuart', stuart_score)
    else:
        print('Draw')


if __name__ == '__main__':
    s = 'BANANA'
    #s = input('Enter a word (in uppercase): ')
    minion_game(s)