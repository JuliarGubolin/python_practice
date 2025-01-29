def FirstFactorial(num):
    fat = num
    while num != 1:
        fat = fat * (num-1)
        num = num-1
    return fat

# keep this function call here 
print(FirstFactorial(4))