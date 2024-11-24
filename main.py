def word_count(file_contents):
    words = file_contents.split()
    print(f"{len(words)}") 
    return (len(words))


def character_count(file_contents):
    import collections
    lower_characters = file_contents.lower()
    counted_list = collections.Counter(lower_characters)
    # Let's filter for only alphabetic characters
    letter_counts = {char: count for char, count in counted_list.items() if char.isalpha()}
    print(letter_counts)

def main():
    with open("/root/workspace/github.com/LevinRB/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        #word_count(file_contents)
        character_count(file_contents)
if __name__ == '__main__':
    main()
    print(" ~~ Begin report of books/frankenstein.txt~~,")
        