def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    vow_in_string = ""
    for i in s:
        if i in vowels:
            vow_in_string += i
    result = ""
    for i in s:
        if i in vowels:
            result += vow_in_string[-1]
            vow_in_string = vow_in_string[:-1]
        else:
            result += i
    return result
