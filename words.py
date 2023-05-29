def print_upper_words(words, must_start_with):
    for word in words:
        lower_word = word.lower()
        for letter in must_start_with:
            lower_letter = letter.lower()
            if lower_word.startswith(lower_letter):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "every", "Evening"], must_start_with=["H", "e"])