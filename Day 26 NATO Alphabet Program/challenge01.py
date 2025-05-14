sentence = input("Enter the sentence: ")

letter_count = {word:len(word) for word in sentence.split()}

for word,count in letter_count.items():
    print(f"{word}: {count}")