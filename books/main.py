
def get_num_words(main_text):
    word_count = main_text.split()
    return len(word_count)

def get_frankenstein(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_charas(main_text):
    main_text = main_text.lower()
    counts = {}
    for chara in main_text:
        if chara in counts:
            counts[chara] += 1
        else:
            counts[chara] = 1
    return counts


def sort_on(d):
    return (-d["num"], d["char"])


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        print(ch) # this will print each character before checking if it's alphabetic
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(key=sort_on)
    return sorted_list


def main():
    frankenstein = "Frankenstein.txt"
    text = get_frankenstein(frankenstein)
    total_words = get_num_words(text)
    print(f"{total_words} words were found")
    counts_dict = count_charas(text)
    chars_sorted_list = chars_dict_to_sorted_list(counts_dict)

    print(f"--- Begin report of {frankenstein} ---")
    print()

    print(chars_sorted_list)
    print("This is a test print statement")

    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

main()
