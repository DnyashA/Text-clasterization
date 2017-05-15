import re

input_file = open("SEO.txt", 'r')
input_file_list = [line.split(r'[^\w\s]+|[\d]+') for line in input_file.readlines()]
input_file_strings = []
for i in range(len(input_file_list)):
    input_file_strings.append(''.join(map(str, input_file_list.__getitem__(i))))
for i in input_file_strings:
    for d in '1234567890':
        i = i.replace(d, '')
    print(i.strip(), "\n")
