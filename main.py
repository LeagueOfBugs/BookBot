def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    aplhabet_char = get_alphabet_chars(chars_dict)
    sorted_dict = dict(sort_dict(aplhabet_char))
    book_report = generate_report(sorted_dict, book_path, num_words)
    return book_report


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_alphabet_chars(dict):
    return {k: v for k,v in dict.items() if k.isalpha()}


def sort_dict(dict):
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)

def generate_report(dict, dict_path, total_words):
    print(f'--- Begin Report of {dict_path}---')
    print(f'{total_words} words found in the document')
    for word, count in dict.items():
        print(f"The '{word}' character was found {count}")
    print('--- End Report ---')


main()