def get_book_contents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def sort_on_count(dict):
    return dict["count"]

def count_charakters(file_contents):
    charakter_count = {}
    for c in "".join(file_contents.lower().split()):
        if c in charakter_count:
            charakter_count[c] += 1
        else:
            charakter_count[c] = 1
    
    lst_count = []
    for key in charakter_count:
        lst_count.append({"name": key, "count": charakter_count[key]})
    
    lst_count.sort(reverse=True, key=sort_on_count)
    
    return lst_count
        
        
def main():
    path_to_file = "books/frankenstein.txt"
    print(f"--- Begin report of {path_to_file} ---")
    contents = get_book_contents(path_to_file)
    
    wordcount = count_words(contents)
    print(f"{wordcount}  words found in the document")
    print()
    
    for line in count_charakters(contents):
        print(f"The '{line['name']}' character was found {line['count']} times")
        
    
main()