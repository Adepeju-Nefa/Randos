
import sys
import random
import string


def yoda_transform(sentence):

    if not sentence:
        return "You didn't give yoda a sentence young padawn...."
    else:
        sentence = sentence.lower()
        for text in string.punctuation.replace("'", ''):
            sentence = sentence.replace(text, '')
        words = sentence.split()
        random.shuffle(words)
        new_sent = ' '.join(words)

        print('Yoda has touched your sentence, enjoy!!!')
        return new_sent.capitalize()


def check_again():
    response = input("Would you like to transform another sentence youngling? Y/N:" )
    response = response.lower()

    if response == 'y':
        new_sentence = input("Your sentence, provide to yoda here: ")
        print(yoda_transform(new_sentence))
        check_again()

    elif response == 'n':
        print('That is all for now padawan, I shall go to rest.')
        sys.exit()
    else:
       print('I do not understand your request young padawan, I shall go to rest now...')
    return


if __name__ == '__main__':
    input_sentence = input("Your sentence, provide to yoda here: ")
    print(yoda_transform(input_sentence))
    check_again()


