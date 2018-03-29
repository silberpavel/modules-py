# module 8/5 files and regex
import re

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    train_time = re.findall(r'\d{3}\s\w+\s\w{1,2}.+(\d{2}\:\d{2}\:\d{2})', text)
    train_number = re.findall(r'(\d{3})\s\w+\s\w{1,2}.+\d{2}\:\d{2}\:\d{2}', text)
    train_direct = re.findall(r'\d{3}\s\w+\s(\w{1,2}\s\w+)', text)
    
with open('output.txt', 'w+', encoding='utf-8') as f:
    i = 0
    for i in range(len(train_number)):
        f.write(f'[{str(train_time[i])}] № {str(train_number[i])} {str(train_direct[i])}\n')