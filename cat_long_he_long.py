def count_words(text: str):
    '''
    function that calculates the length of words in a text.
    For example:
        str: "Rivki Kanterovich".
        return: {'Rivki': 5, 'Kanterovich': 11}.
    :param text: text of words.
    :return: dictionary of len of word in a text.
    '''
    str_only_word = [''.join(letter for letter in word if letter.isalpha()) for word in text.split(' ')]
    dict_word_len = {word: len(word) for word in str_only_word}
    return dict_word_len


def main():
    text = "You see, wire telegraph is a kind of a very, very long cat. " \
           "You pull his tail in New York and his head is meowing in Los Angeles. " \
           "Do you understand this? " \
           "And radio operates exactly the same way: you send signals here, they receive them there. " \
           "The only difference is that there is no cat."
    print(count_words(text))


if __name__ == '__main__':
    main()
