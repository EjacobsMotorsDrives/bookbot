

def report(book_result,path_book,bookSTR):
    word_count= get_num_words(bookSTR)


    print(f"============ BOOKBOT ============\nAnalyzing book found at {path_book}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
    chars_list = [{'char': key, 'count': value} for key, value in book_result.items() if key.isalpha()]
    def sort_on(entry):
        return entry['count']
    chars_list.sort(reverse=True, key=sort_on)

    for char_entry in chars_list:
        print(f"{char_entry['char']}: {char_entry['count']}")

def get_num_words(book):
    return len(book.split())


def count_characters(text):
    
    chars_dict = {}
    for char in text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict
