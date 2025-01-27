# Fibonacci sequence: 1 1 2 3 5 8 13 21, ...
#----
def fibonacci(number_of_elements):
    list = [1, 1]
    if(number_of_elements <= 1): return number_of_elements
    else:
        for i in range(1,number_of_elements):
            list.append(list[i-1]+list[i])
        return list

print(fibonacci(8))