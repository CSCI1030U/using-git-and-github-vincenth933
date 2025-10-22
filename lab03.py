def main():
    # part 1

    pets = ['Spot', 'Boots', 'Mrs. Fluffington', 'Lenny', 'Bowser', 'Gina']
    count = 0
    pet_name_lengths = []

# TODO: YOUR CODE TO COUNT THE NUMBER OF PETS AND THE LENGTH OF PET NAMES GOES HERE
    for i in pets:
        count += 1
        pet_name_lengths.append(len(i))

    print(f'There are {count} pets in the list.')
    print(f'The word lengths of each word are {pet_name_lengths}.')

    # part 2

    words = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
    word_vowel_ratios = []

    # TODO: YOUR CODE TO COUNT THE NUMBER OF VOWELS AND CONSONANTS IN EACH WORD TO CALCULATE THE RATIOS
    for word in words:
        vowls = 0
        consonants = 0
        for letter in word:
            if letter in 'aeiou':
                vowls += 1
            else:
                consonants += 1
                if consonants == 0:
                    consonants = 1
        word_vowel_ratios.append(vowls / consonants)
    print(f'The vowel to consonant ratios for each word are {word_vowel_ratios}.')
if __name__ == "__main__":
    main()