import  numpy as np

baseball = [23,100, 200, 300, 400, 500,600, 700, 800, 900]

np_baseball = np.array(baseball)

result = np_baseball/5

print(type(np_baseball))
print(result)