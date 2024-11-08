num_list = []
max_number = int(input("Enter a number: "))

for i in range(1, max_number + 1): 
    if i % 2 != 0: 
        num_list.append(i)
        
print('ODD numbers between 1 and', max_number, ':', num_list)
