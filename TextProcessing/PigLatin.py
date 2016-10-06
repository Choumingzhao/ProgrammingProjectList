# -*- encoding:utf-8 -*-
import re


def pigLatin(word):
    if word.isalpha() is False:
        raise TypeError
    lower = word.lower()
    # When word is not started with vowel letter
    if all([not lower.startswith(i) for i in 'aeiou']):
        head = re.match(r'[bcdfghjklmnpqrstvwxyz]+', lower).group()
        result = lower.replace(head, '')+head+'ay'
    else:
        result = word+"way"
    if word[0].isupper():
        return result.capitalize()
    else:
        return result

if __name__ == "__main__":
    word = "Hello"
    print(pigLatin(word))
