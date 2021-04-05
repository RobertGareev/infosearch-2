import json
import math
import nltk

result = {}

with open('./resources/invertedIndex.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        data = json.loads(line)
        if data.get('word') not in result.keys() and data.get('count') != 0:
            # tf
            tf = {}
            for n in data.get('inverted_array'):
                with open('./resources/files/' + str(n) + '.txt', 'r', encoding='utf-8') as f:
                    lns = f.readlines()
                    entrances = 0
                    words = 0
                    for l in lns:
                        entrances += l.count(data.get('word'))
                        words += len(nltk.tokenize.word_tokenize(l, language="russian"))
                    tf[n] = entrances / words
            # idf
            idf = math.log(100 / data.get('count'))
            #tf_idf
            tf_idf = {}
            if idf != 0:
                for n in tf.keys():
                    tf_idf[n] = tf.get(n) * idf
            res_word = {}
            res_word['idf'] = idf
            res_word['tf_idf'] = tf_idf
            result[data.get('word')] = res_word
            print('done for the word "' + data.get('word') + '"')

# result in JSON format
result_file = open('tf_idf.txt', 'x')
for item in result.items():
    result_file.write(str(item) + '\n')
