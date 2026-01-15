number = 32544447

def digit_root(num):
    def sum_list_numbers(temp_num):
        summa = 0  
        temp_list = list(str(temp_num))
        for i in range(len(temp_list)):
            summa += int(temp_list[i])
        temp_num = summa
        return temp_num

    a = sum_list_numbers(num)
    for i in range(9):
        if (a > 9):
            a = sum_list_numbers(a)
        else:
            break
    return a

print(digit_root(number))
         