
# Multiply the values in your lists (A and B using for loop and prit out rhe result)
list_A = [9,8,6,4,1,7,6]
list_B = [5,8,7,9,2,4,0]
result = []

for i in range(len(list_A)):
    temp_result = list_A[i] * list_B[i]
    result.append(temp_result)
print(result)
