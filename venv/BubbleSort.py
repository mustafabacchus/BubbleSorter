def bubble_sort(array):
    switch = True
    while switch:
        for i in range(len(array)-1):
            num1 = array[i]
            num2 = array[i+1]
            if num1 > num2:
                array[i] = num2
                array[i+1] = num1
                switch = True
                break
            else:
                switch = False
    return array


my_list = [7, 4, 7, 10, 3, 5, 6, 7, 9 ,1, 9, 2]
bubble_sort(my_list)
print(my_list)