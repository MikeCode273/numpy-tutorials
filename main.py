import numpy as np

baseball = [[23,100, 200, ],
            [10, 20, 30, ],[40, 90, 50]]

np_baseball = np.array(baseball)
#
# # result = np_baseball/5
#
# print(np_baseball[1, 3])
# # print(type(np_baseball))
# print(np_baseball)

print(np_baseball)
# print(updated)
print("The mean: " f"{np.mean(np_baseball[:, 0])}")
print("The median: " f"{np.median(np_baseball[:, 0])}")
print("The Standard deviation: " f"{np.std(np_baseball[:, 1])}")

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
result = np_baseball * conversion
print(result)