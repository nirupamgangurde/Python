def frequency_counter(sentence):
    cleaned_sentence = sentence.lower().replace(".","").replace(",", "").replace("?", "").replace("!","")
    words = cleaned_sentence.split()
    word_frequency = {}
    for word in words :
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency
def main():
    sentence = input("Enter Sentence : ")
    frequencies = frequency_counter(sentence)
    print("\nWord\t\tFrequency")
    print("------------------------")
    for word, frequency in frequencies.items():
        print(f"{word.ljust(12)}\t{frequency}")

if __name__ == "__main__":
        main()