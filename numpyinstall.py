import numpy as np



# a=np.array([1,2,3,4])
# print(a)

# # converting list into array


# x=[1,2,3,4,5]
# y=np.array(x)

# print(type(y))
# l=[]
# for i in range(4):
#   int_1=int(input("Enter the Value:"))
#   l.append(int_1)

# print(np.array(l))

ar2=np.array([[1,2,3,4],[5,6,7,8]])

print(ar2)
print(ar2.ndim)

ar10=np.array([1,2,3,4],ndmin=10)


print(ar10.ndim)