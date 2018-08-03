def reverse_words(text):

    text = text[::-1].split()
    new_list = []

    while len(text) > 0:
        new_list.append(text.pop())

    return " ".join(new_list)

# def reverse_words(text):
#     return ' '.join(s[::-1] for s in text.split(' '))


print reverse_words('The quick brown fox jumps over the lazy dog.')
