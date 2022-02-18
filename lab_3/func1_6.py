def reverso(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence
sentence = input()
print(reverso(sentence))