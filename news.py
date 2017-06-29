import chardet
import json


def main_function():
    file_list = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    for file_name in file_list:
        encoding_type = decoding_file(file_name)
        count_dict = open_file(file_name, encoding_type)
        print_sort_words(count_dict)


def decoding_file(file):
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
    return result['encoding']


def open_file(file_name, encoding_type):
    with open(file_name, encoding=encoding_type) as f:
        data = json.load(f)

        list_words = []
        count_dict = {}
      
        for text_news in data['rss']['channel']['items']:
            list_words += (text_news['title']).split()
            list_words += (text_news['description']).split()
        for word in list_words:
            if len(word) < 6:
                 continue
            else:
                if word.lower() not in count_dict:
                    count_dict[word.lower()] = int(list_words.count(word))

        print('В файле {} * {} * обработано:'.format(f.name, (data['rss']['channel']['title'])))
        print('Cлов {} шт. '.format(len(list_words)))
        print('Уникальных слов {} шт. длиной более 5 символов'.format(len(count_dict)))
        print('Новостей {} шт обработанно.'.format(len(data['rss']['channel']['items'])))
    return count_dict


def print_sort_words(count_dict):
    
    reves_count_dict = (dict(reversed((sorted(count_dict.items(), key = lambda item: item[1])))))
    reves_count_dict_sorted = {}
    for key, value in reves_count_dict.items():
        if len(reves_count_dict_sorted) < 10:
            reves_count_dict_sorted[key] = value
    for key,value in  reves_count_dict_sorted.items():
        print('{1} - {0}'.format(key, value))
    print('\n')

main_function()
