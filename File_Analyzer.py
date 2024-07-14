import string
from collections import Counter

def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        translator = str.maketrans('','',string.punctuation)
        cleaned_text = text.translate(translator).lower()
        words = cleaned_text.split()
        total_lines = text.count("\n") +1
        total_words = len(words)
        longest_word = max(words, key=len, default='')
        word_count = Counter(words)
        most_common_words = word_count.most_common(5)
        print(f"Total lines: {total_lines}")
        print(f"Total words: {total_words}")
        print(f"Longest word: {longest_word}")
        print("Top 5 most frequent words:")
        for i ,(word,count) in enumerate(most_common_words ,1):
            print(f"{i}.{word}:{count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__=="__main__":
    filename = input("Enter File Name with Extension : ")
    analyze_file(filename)