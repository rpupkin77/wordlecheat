# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('words.txt', "r") as words:
        possible_words = []

        my_letters = ["o", "r", "aa"]
        exclude_letters = ["s", "h", "u", "t", "p",  "w", "n", "c"]
        # you get one green hint
        known_letter = "o"
        position = 3

        word_list = words.read().split('\n')

        for word in word_list:
            word_as_list = list(word)
            # the word contains letters that were already used, ignore it
            if any(x in exclude_letters for x in word_as_list):
                continue

            if all(ml in word_as_list for ml in my_letters):
                if known_letter and known_letter != "":
                    if not(position):
                        position = 1

                    if known_letter == word[(position-1)]:
                        possible_words.append(word)
                else:
                    possible_words.append(word)

        for pw in possible_words:
            print(pw)














# See PyCharm help at https://www.jetbrains.com/help/pycharm/
