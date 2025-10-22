# TODO: YOUR FUNCTIONS DEFINITIONS GO HERE

# Part 1
def combine_marks(names, test1_marks, test2_marks):
    student_data = []
    for i in range(len(names)):
        student_data.append((names[i], test1_marks[i], test2_marks[i]))
    return student_data

# Part 2
def get_summary(character):
    return f"{character['name']} is a level {character['level']} {character['race']} {character['class']} with {character['hp']} HP."

# Part 3
def is_vowel(char):
    vowels = 'aeiou'
    return char.lower() in vowels

# Part 4
def count_vowels_iter(text):
    count = 0
    for char in text:
        if is_vowel(char):
            count += 1
    return count

def main():
    # This main() function is here in case you want to test your functions with sample data

    # Part 1
    names = ['Lucie Manette', 'Charles Darnay', 'Sydney Carton']
    test1_marks = [34.0, 75.5, 58.0]
    test2_marks = [47.5, 82.0, 63.5]

    student_data = combine_marks(names, test1_marks, test2_marks)
    print(student_data)

    # Part 2
    character = {
        'name': 'Grimbor',
        'race': 'Dwarf',
        'class': 'Warrior',
        'hp': 58,
        'level': 9,
    }
    summary = get_summary(character)
    print(summary)

    # Part 3
    print(f'{is_vowel("t")=}')   # prints False
    print(f'{is_vowel("o")=}')   # prints True
    print(f'{is_vowel("u")=}')   # prints True

    # Part 4
    print(f'{count_vowels_iter("this is a sentence")=}')   # prints 6
    print(f'{count_vowels_iter("loud")=}')                 # prints 2
    print(f'{count_vowels_iter("rebel")=}')                # prints 2

if __name__ == "__main__":
    main()