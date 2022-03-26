def load_words():
    with open('allwords.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def get_six_letter_words(words):
    six_letter_words = []
    for word in words:
        if len(word) == 6 and not word.endswith('s'):
            six_letter_words.append(word)

    return six_letter_words


def add_to_file(words):
    with open('six-letter-words.txt', 'w') as f:
        for word in words:
            f.write("  \'%s\',\n" % word)


if __name__ == '__main__':
    english_words = load_words()
    six_letter_words = get_six_letter_words(english_words)
    add_to_file(six_letter_words)