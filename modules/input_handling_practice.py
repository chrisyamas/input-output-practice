import re


def iterate_file_object_like_list(path):
    my_file = open(path, 'r')
    try:
        for line in my_file:
            print(line)
    finally:
        my_file.close()


def open_read_exclaim_print_and_automatic_close(path):
    with open(path, 'r') as f:
        for line in f:
            line_stripped = line.strip('\n')
            exclaim_line = f"{line_stripped}!!!"
            print(exclaim_line)


def print_word_counts(path):
    word_list = []
    word_freq = {}
    # Read function to assemble word_list - takes file path, returns word_list
    with open(path, 'r') as f:
        for line in f:
            line_stripped = line.strip('\n')
            list_of_words_in_line = line_stripped.split()
            word_list += list_of_words_in_line
    # Iterates through word_list to assemble word_freq dict
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    # Extracts the keys from word_freq into word_keys list, sorts, and iterates
    # to print output
    word_keys = list(word_freq.keys())
    word_keys.sort()
    for word in word_keys:
        freq = word_freq[word]
        print(f"{word} {freq}")
    return


# Break up above function into smaller functions for each action
def componentized_print_word_counts(path_to_file):
    """
    Uses helper functions to parse a text file and then print to the console
    each unique word in the file, followed by a space and then an integer
    representing the number of occurrences of the word throughout the file.

    Param
    -----
    :path_to_file: string of a path to the text file being read

    Return
    ------
    None; rather it prints output to the console.

    Helpers
    -------
    get_word_list()
    get_word_frequency()
    print_word_and_frequency()
    """
    word_list = get_word_list(path_to_file)
    word_freq = get_word_frequency(word_list)
    # Print output of word and frequency:
    print_word_and_frequency(word_freq)
    return


def get_word_list(path):
    """
    Creates a list of all words contained in a text file,
    free of any new lines or whitespace.

    Param
    -----
    :path: string of a path to the text file being read

    Return
    ------
    :word_list: list of each word in file as strings
    """
    word_list = []
    with open(path, 'r') as f:
        for line in f:
            line_stripped = line.strip('\n')
            list_of_words_in_line = line_stripped.split()
            word_list += list_of_words_in_line
    return word_list


def get_word_frequency(words):
    """
    Creates a dictionary with each key being a word in the list and each
    respective value being the number of occurrences of that word in the list.

    Param
    -----
    :words: list of words as individual strings

    Return
    ------
    :word_freq: dictionary with words as keys and their occurrences as values
    """
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq


def print_word_and_frequency(frequency_dict):
    """
    Prints the keys and values of a word frequency dictionary in
    lexicographically sorted order. Each line printed contains a key, followed
    by a space, followed by the respective value.

    Param
    -----
    :frequency_dict: dictionary; key --> word (str), value --> occurrence (int)
    """
    word_keys = list(frequency_dict.keys())
    word_keys.sort()
    for word in word_keys:
        freq = frequency_dict[word]
        print(f"{word} {freq}, but cooler this time.")
    return


def use_python_count_method(path):
    """
    Parses a text file, finds the unique words contained within, and prints to
    the console each unique word, followed by a single space, then followed by
    the number of occurrences of the word in the file
    :param path: a string of a path to access a text file
    :return: None
    """
    word_list = get_word_list(path)
    word_set = set(word_list)
    word_freq = {}
    for word in word_set:
        word_freq[word] = word_list.count(word)
    unique_words = list(word_set)
    unique_words.sort()
    print("Used count method to print these:")
    for unique in unique_words:
        freq = word_freq[unique]
        print(f"{unique} {freq}")
    return


def get_word_count_with_list_comp(path):
    # split text into list
    # use regex in function to remove non-alphabetic characters
    # use function to create word list
    # create word set, list, sort
    # use list comprehension to get tuples of word and count in initial word_list
    # iterate through this list, print accordingly
    text_list = []
    with open(path, 'r') as f:
        for line in f:
            # Split text into list of terms (that were separated by whitespace)
            text_list += line.split()
    # Use regex compile() to only included desired characters
    regex = re.compile("[^a-zA-Z']")
    word_list = [regex.sub('', term) for term in text_list]
    # Remove any empty strings remaining in list
    word_list = [x for x in word_list if len(x) > 0]
    # Create a list of all unique words by converting to set
    # then converting back to a list
    unique_list = list(set(word_list))
    # Create a list holding tuples of (each unique word, its frequency in text)
    words_and_counts = [(x, word_list.count(x)) for x in unique_list]
    words_and_counts.sort(reverse=True, key=lambda i: i[1])
    words_and_counts = {word: word_list.count(word) for word in word_list}
    for word, count in words_and_counts:
        print(word, count)
    return


if __name__ == '__main__':
    file_name = "../samples/sotu_address_2022.txt"
    get_word_count_with_list_comp(file_name)
