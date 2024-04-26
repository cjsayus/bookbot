def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word = get_num_words(text)
    chars_dict = letter_occ(text)
    d_list = split_dict(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_word} words found in the document")
    print()
    for item in d_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item["char"]} character was found {item["num"]} times")
    
    print("--- End report ---")

    



def sort_on(x):
    return x["num"]

def split_dict(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)

def letter_occ(text):
    stats = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in stats:
            stats[char] += 1
        else:
            stats[char] = 1
    return stats







main()    

