def Test(arr):
    
    factor = []
    factor_2 = []
    for i in range(0, len(arr)-1):
      factor.append(arr[i+1] - arr[i])
      factor_2.append(arr[i+1] / arr[i])
    
    if all(x == factor[0] for x in factor):
       return "Arithmetic"
    elif all(x == factor_2[0] for x in factor_2):
       return "Geometric"
    return -1

def ArithGeo(arr):
     return Test(arr)
# keep this function call here 
print(ArithGeo([15, 10, 5]))