def reverse_words(sentence):
    words = sentence.split()
    reversed = ' '.join(words[::-1])
    return reversed
print(reverse_words("Hello, my name is Nurdaulet"))