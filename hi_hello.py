def words_length(sentence: str) -> [int]:
    '''
    function that calculates the length of words in a sentence.
    For example:
        str: "Rivki Kanterovich".
        return: [5, 11].
    :param sentence: sentence of words.
    :return: list of len of word in a sentence.
    '''
    str_only_word = [word for word in sentence.split(' ')]
    list_word_len = [len(word) for word in str_only_word]
    return list_word_len


def main():
    sentence = "Toto, I've a feeling we're not in Kansas anymore"
    print(words_length(sentence))


if __name__ == '__main__':
    main()
