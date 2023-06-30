from nltk.corpus import words
# nltk.download('words')
from utils import WORDLE
CLUE = []
POSITION = list('_____')


def check_invalid(word):
    setofwords = set(words.words())
    if len(word) != 5 or not(word in setofwords):
        print(f'{word} is not 5 letters or dictionary word')
        return True
    else:
        return False
    print()


def get_input():
    word = input('Wordle - ')
    return word


def find_clues(word):
    global WORDLE, CLUE, POSITION
    # clue_list =
    CLUE = list(set(CLUE +[x for x in list(word) if x in list(WORDLE)]))

    for i in range(5):
        if word[i] == WORDLE[i]:
            POSITION[i] = word[i]
    print(f"{CLUE} \t\t  {POSITION}")
    if '_' not in POSITION:
        print('Great Job')
        exit(1)

invalid = True
count = 0
while(invalid):
    user_word = get_input()
    invalid = check_invalid(user_word)
    if not invalid and count <5:
        find_clues(user_word)
        count +=1
        invalid = True
    if count >5:
        print(f'Exceeded 5 attempts')

