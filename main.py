def main():
    with open("/home/kilregna/workspace/github.com/Kilregna/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    number = len(words)
    print (f"{number} words found in the document")
    return file_contents

def stringcount(text):
    characters = {}
    lowered_text = text.lower()
    for char in lowered_text:
            if char.isalpha():
                if char not in characters:
                    characters[char] = 1
                else: 
                    characters[char] += 1
    return(characters)

def convert_dict_to_list(characters):
    char_list = []
    for char, count in characters.items():
        char = {"char": char, "count": count}
        char_list.append(char)
    return char_list

def sort_on(dict):
    return dict["count"]

file_contents = main()
print(stringcount(file_contents))
characters = stringcount(file_contents)
char_list = convert_dict_to_list(characters)
char_list.sort(reverse=True, key=sort_on)
for item in char_list:
    print(f"The '{item['char']}' character was found {item['count']} times.")