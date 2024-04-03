def txt_to_string(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
    return data
