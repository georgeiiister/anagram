import random
from functools import reduce

def words() -> tuple:
    return ('hello',
            'world',
            'town',
            'city',
            'address',
            'kitty')


def create_anagram():
    err_words = tuple()

    for i, word in enumerate(tuple(i.upper() for i in words())):

        new_word = ''
        for j in word:
            while True:
                _ = random.choice(word)
                if not new_word or _ not in new_word or word.count(_) >= new_word.count(_) + 1:
                    break
            new_word += _

        if input(f'>> {new_word} <<\n You this known words? '
                 f'If "yes", type it on the keypad >>> ').upper() != word:
            err_words += (word,)

    print(f'do you this known words: {len(words()) - len(err_words)} from {len(words())} '
          f'error_word: {str(err_words) if len(err_words) > 0 else 0}'
          )


def create_anagram_plus():
    err_words = tuple()

    for i, word in enumerate(tuple(i.upper() for i in words())):

        new_word = ''
        old_word = word
        while old_word:
            position = random.choice(range(len(old_word)))
            new_word += old_word[position]

            letters_list = list(old_word)
            del letters_list[position]
            old_word = ''.join(letters_list)

        if input(f'>> {new_word} <<\n You this known words? '
                 f'If "yes", type it on the keypad >>> ').upper() != word:
            err_words += (word,)

    print(f'do you this known words: {len(words()) - len(err_words)} from {len(words())} '
          f'error_word: {str(err_words) if len(err_words) > 0 else 0}'
          )

def check_anagram(word=None):
    return reduce(lambda i,j:i==j[::-1],[input('input word for check on anagram >> ') if not word else word]*2)

def main():
    create_anagram_plus()



if __name__ == '__main__':
   main()
