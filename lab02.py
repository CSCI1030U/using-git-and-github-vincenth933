def main():
    # part 1

    defense = 5
    attack = 8
    hp = 10

    # TODO: YOUR CODE FOR PART 1 GOES HERE
    damage_taken = max(attack - defense, 0 )
    hp -= damage_taken
    print(f"3 damage inflicted, enemy hp is now {hp}.")
    
    # part 2

    lab_mark = 9
    midterm_mark = 40
    final_exam_mark = 135

    # TODO: YOUR CODE FOR PART 2 GOES HERE
    scaled_lab = (lab_mark / 10) * 30
    scaled_midterm = (midterm_mark / 80) * 30
    scaled_final = (final_exam_mark / 180) * 40

    final_grade = scaled_lab + scaled_midterm + scaled_final

    if 0.0 <= final_grade < 50.0:
        letter = "F"
    elif 50.0 <= final_grade < 60.0:
        letter = "D"
    elif 60.0 <= final_grade < 70.0:
        letter = "C"
    elif 70.0 <= final_grade < 80.0:
        letter = "B"
    elif 80.0 <= final_grade <= 100.0:
        letter = "A"
    else:
        letter = "Invalid"

    print(f"This student's final grade is {letter}.")

    # part 3

    long_string = 'the quick brown fox'

    # TODO: YOUR CODE FOR PART 3 GOES HERE
    long_string = 'the quick brown fox'
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0

    for char in long_string:
        if char == ' ':
            continue
        elif char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    ratio = round(vowel_count / consonant_count, 2)
    print (f"The vowel to consonant ratio of '{long_string}' is {vowel_count} / {consonant_count} = {ratio}")
    
if __name__ == "__main__":
    main()