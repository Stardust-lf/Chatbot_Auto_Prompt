def txt_to_string(filename):
    with open(filename, 'r',encoding='utf-8') as file:
        data = file.read().replace('\n', '')
    return data

def get_char(sentence):
    temp = sentence.split(' ')
    if 'likui' in temp:
        return 'likui'
    elif 'wusong' in temp:
        return 'wusong'
    elif 'luzhishen' in temp:
        return 'luzhishen'