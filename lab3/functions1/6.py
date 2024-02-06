def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words to form the new sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

# Example usage:
user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print("Reversed words:", result)