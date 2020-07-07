def delete_punctuations(text: str):
    from unicodedata import category
    incomplate = ''.join(n for n in text if not category(n).startswith('P'))
    text_without_punct = ''.join(n for n in incomplate if not category(n).startswith('S'))
    return text_without_punct


text_data = ['Test!!!! hello. esim. test2...',
             '100% ola!! #HashTag',
             'testText???!!?']

for i in range(len(text_data)):
    text_data[i] = delete_punctuations(text_data[i])
print(text_data)
