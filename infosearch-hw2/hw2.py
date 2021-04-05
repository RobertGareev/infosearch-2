import nltk
import os
import re
import pymorphy2

all_files = []
stopwords_rus = nltk.corpus.stopwords.words("russian")

for filename in os.listdir('./resources/files'):
    with open('./resources/files/' + filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            all_files.append(line)


files_count = len(all_files)

print('STEP 1:')
print('[get tokens from files and write them to tokens.txt....]')
search = re.compile(r'[^А-Яа-я]').search
all_tokens = []

for i in range(files_count):
    words = nltk.tokenize.word_tokenize(all_files[i], language="russian")
    # исключаем стоп-слова и слова, не состоящие из русских букв
    for w in words:
        if w not in stopwords_rus and not bool(search(w)):
            all_tokens.append(w)

tokens_file = open('./tokens.txt', 'x', encoding='utf-8')
for token in all_tokens:
    tokens_file.write(token + '\n')
print('tokens written successfully!')


print('STEP 2:')
print('[lemmatize tokens and write them to lemmas.txt...]')
lemmas = {}
morph = pymorphy2.MorphAnalyzer()

tokens_count = len(all_tokens)

for i in range(tokens_count):
    l = morph.normal_forms(all_tokens[i])[0]
    if not bool(lemmas.get(l)):
        lemmas[l] = []
    lemmas[l].append(all_tokens[i])

lemmas_file = open('./lemmas.txt', 'x', encoding='utf-8')
for main_word in lemmas:
    lemmas_file.write(main_word + ' ')
    for res in lemmas[main_word]:
        lemmas_file.write(res + ' ')
    lemmas_file.write('\n')
print('lemmas written successfully!')