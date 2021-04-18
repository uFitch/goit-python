# Clear and normalize text (remove non-alphanumeric symbols and make it casefold)
# Find frequency for each word
# Find text dictionary
# Find top 3 keywords

import re


test_text = ""Matches if the current position in the string is preceded by a match for ... that ends at the current position. This is called a positive lookbehind assertion. (?<=abc)def will find a match in 'abcdef', since the lookbehind will back up 3 characters and check if the contained pattern matches. The contained pattern must only match strings of some fixed length, meaning that abc or a|b are allowed, but a* and a{3,4} are not. Note that patterns which start with positive lookbehind assertions will not match at the beginning of the string being searched; you will most likely want to use the search() function rather than the match() function:""



def clear_text(text):

    clean_text = re.sub(r'[^\w\s]', '', text)

    return clean_text


def normalize_text(clean_text):

    return clean_text.casefold()


def find_text_dictionary(clean_normalized_text):

    text_dictionary = frozenset(clean_normalized_text.split())

    return text_dictionary


def find_words_frequency(clean_normalized_text, text_dictionary):

    words_frequency = {}
    words_quantity = len(clean_normalized_text.split())

    for word in text_dictionary:

        frequency = clean_normalized_text.count(word) / words_quantity * 100
        words_frequency[word] = round(frequency, 2)

    return words_frequency


def sort_by_value(item):
    
    return item[1]


def sort_words_frequency(words_frequency):

    words_frequency_items = list(words_frequency.items())
    words_frequency_items.sort(key=sort_by_value, reverse=True)

    print(words_frequency_items)
