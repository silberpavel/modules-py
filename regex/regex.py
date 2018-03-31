# (r/w) files, regex, zip | module 8.5
import re

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    train_time = re.findall(r'\d{3}\s\w+\s\w{1,2}.+(\d{2}\:\d{2}\:\d{2})', text)
    train_number = re.findall(r'(\d{3})\s\w+\s\w{1,2}.+\d{2}\:\d{2}\:\d{2}', text)
    train_direct = re.findall(r'\d{3}\s\w+\s(\w{1,2}\s\w+)', text)
    
with open('output.txt', 'w+', encoding='utf-8') as f:
    z = list(zip(train_time, train_number, train_direct))
    list_len = len(z)
    count = 0

    for lst in z[count]:        
        if count < list_len:
            f.write(f'[{str(z[count][0])}] № {str(z[count][1])} {str(z[count][2])}\n')
##            print(f'[{str(z[count][0])}] № {str(z[count][1])} {str(z[count][2])}\n')
            count += 1
        else:
            break
        
        
        
        
        