a = open('PZ10/10.2/text18-6.txt', 'r')
s = open('PZ10/10.2/new_text.txt', 'w')
c = 0
d = a.read()
for i in d:
    if i == ' ':
        c += 1
print(d, c, sep = '\n')
text = d.replace('»','!').replace('«','!').replace('.','!').replace(',','!').replace('?','!')
s.write(text)
a.close
s.close

    
