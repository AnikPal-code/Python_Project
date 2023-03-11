# My name is Anik Pal my stream is AIML

text = input()
letters = []

text = text.lower()
letters.append(input("Enter the first number: ").lower())
letters.append(input("Enter the second number: ").lower())
letters.append(input("Enter the third number: ").lower())

print("\n")
print("LETTER REPETITIONS")
letter_repetition1 = text.count(letters[0])
letter_repetition2 = text.count(letters[1])
letter_repetition3 = text.count(letters[2])

print(f"We have found the '{letters[0]}' repeated {letter_repetition1} no. of times")
print(f"We have found the '{letters[1]}' repeated {letter_repetition2} no. of times")
print(f"We have found the '{letters[2]}' repeated {letter_repetition3} no. of times")

print("\n")
print("NO OF WORDS")

words = text.split()
print(f"No of words in the text is {len(words)}")

print("\n")
print("PRINT FIRST AND LAST WORD")
print(f"The first word of the text is '{text[0]}' and the last of the text is '{text[-1]}'")

print("\n")
print("INVERTED TEXT")
words.reverse()
inverted_text = ' '.join(words)
print(inverted_text)

print("\n")
print("LOOKING FOR THE WORD 'PYTHON' IN TEXT")
is_python = 'python' in text
dt = {True: 'is', False: 'is not'}
print(f"The word 'python' {dt[is_python]} present")
print("\n")
