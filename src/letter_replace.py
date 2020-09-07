def replace(initial_text):
    _dict = {'a': '@',
             's': '$',
             'e': '3',
             'b': '8',
             'i': '1',
             'o': '0'
             }

    altered_text = ''
    for letter in initial_text:
        letter_low = letter.lower()
        if _dict.get(letter_low) is None:
            altered_text += letter
        else:
            altered_text += _dict[letter_low]

    return altered_text


def letter_replace(password):
    new_pass = replace(password)
    if new_pass != password and new_pass is not None:
        return new_pass
    else:
        pass
