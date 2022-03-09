""" wordle cheat script for wordlers having a bad day"""

if __name__ == '__main__':

    known_letters = input("Known Letters - Enter your known letters (no spaces. example: frw) or leave blank if none: ")
    skip_letters = input("Skip Letters - Enter letters you know are not in word (no spaces. example: vnb): ")
    known_letter = input("You get 1 green letter hint, enter a letter you know the position of, leave blank if none: ")
    known_position: int = input("What position is the letter (1-5), leave blank if none: ")

    if known_position:
        try:
            known_position = int(known_position)
        except ValueError:
            print("Known position must be an integer, try again")
            exit

    with open('words.txt', "r") as words:
        possible_words = []

        if not known_letters and not skip_letters:
            raise ValueError("You must enter at least one known letter or one skip letter")

        my_letters = list(known_letters)
        exclude_letters = list(skip_letters)
        # you get one green hint

        word_list = words.read().split('\n')

        for word in word_list:
            word_as_list = list(word)
            # the word contains letters that were already used, ignore it
            if any(x in exclude_letters for x in word_as_list):
                continue

            if all(ml in word_as_list for ml in my_letters):
                if known_letter and known_letter != "":
                    if not known_position:
                        known_position = 1
                    if known_letter == word[(known_position-1)]:
                        possible_words.append(word)
                else:
                    possible_words.append(word)

        for pw in possible_words:
            print(pw)














# See PyCharm help at https://www.jetbrains.com/help/pycharm/
