# TODO: YOUR FUNCTIONS DEFINITIONS GO HERE

def main():
    # This main() function is here in case you want to test your functions with sample data

    # part 1
    
    def combine_marks(names, test1_marks, test2_marks):
        student_data = []
        for i in range(len(names)):
            first_name, last_name = names[i].split()
            student_dict = {
                'first_name': first_name,
                'last_name': last_name,
                'test1': test1_marks[i],
                'test2': test2_marks[i]
            }
            student_data.append(student_dict)
        if student_data:
            del student_data[-1]
        return student_data

    names = ['Lucie Manette', 'Charles Darnay', 'Sydney Carton']
    test1_marks = [34.0, 75.5, 58.0]
    test2_marks = [47.5, 82.0, 63.5]

    student_data = combine_marks(names, test1_marks, test2_marks)
    print(student_data)
    

    # part 2

    def get_summary(character):
        return f"{character['name']} (level {character['level']} {character['race']} {character['class']}) - HP: {character['hp']}"

    character = {
        'name': 'Grimbor',
        'race': 'Dwarf',
        'class': 'Warrior',
        'hp': 58,
        'level': 9,
    }
    summary = get_summary(character)
    print(summary)

    # part 3

    def is_vowel1(character):
        return character.lower() in 'aeiou'

    print(f'{is_vowel1("t")=}')   # prints False
    print(f'{is_vowel1("o")=}')   # prints True
    print(f'{is_vowel1("u")=}')   # prints True

    # part 4
    def is_vowel(character):
        return character.lower() in 'aeiou'

    def count_vowels_iter(sentence):
        count = 0
        for char in sentence:
            if is_vowel(char):
                count += 1
        return count

    print(f'{count_vowels_iter("this is a sentence")=}')   # prints 6
    print(f'{count_vowels_iter("loud")=}')                 # prints 2
    print(f'{count_vowels_iter("rebel")=}')                # prints 2


if __name__ == "__main__":
    main()