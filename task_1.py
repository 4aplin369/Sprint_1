time = '1h 45m,360s,25m,30m 120s,2h 60s'
list = time.replace(' ', ',').split(',')
sum = 0
for l in list:
    if 'h' in l:
        sum += int(l.replace('h', ''))*60
    if 'm' in l:
        sum += int(l.replace('m', ''))
    if 's' in l:
        sum += int(l.replace('s', ''))//60
print("Сумма в минутах:", sum)
