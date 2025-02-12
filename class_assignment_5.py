# x = []
# while True:
#     temp = int(input("Do you want to add 1 to add any number to exit"))
#     if temp == 1:
#         celcius = int(input("Enter the temperature in celcius"))
#         if celcius < 20:
#             faren = (celcius*9/5) + 32
#             x.append(faren)
#     else:
#         break
# print(x)


# question no 2

lst1 =[[1, 2], [3, 4], [5, 6]]

result = []

for x in lst1:
    for y in x:
        result.append(y)
print(result)
res = set(result)
print(res)


# question no 3

# lst1 =[1, 2, 3, 4, 5, 6, 7]
# lst2 = [1, 2, 11, 12, 14, 15, 16]

# set1= set(lst1)
# set2 = set(lst2)

# res = set1.intersection(set2)

# result = list(res)
# print(result)


# question no 4

# transaction = (12345, 500.75, "2024-12-01")

# Sno, Amount, Timestamp = transaction

# print(Sno)

# question no 5
# nums = [1,2,3,1,2,5,7,8,8]
# # set1 = set(nums)
# # result = nums.difference(set1)
# # print(result)
# result = []
# for x in range(9):
#     if x != nums:
#         nums[x] = result
#     nums +=1
# print(result)




# question no 6

# set1 = {1, 2, 3, 4}
# set2 = {2}

# set3= set1.symmetric_difference(set2)
# print(set3)


# question no. 2

# list1 = [[1,2],[4,5]]