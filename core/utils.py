def txt_to_string(filename):
    with open(filename, 'r',encoding='utf-8') as file:
        data = file.read().replace('\n', '')
    return data
