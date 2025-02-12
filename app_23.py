# import csv
# import pandas as pd
# with open("text.csv", "r") as f:

#     df = pd.read_csv('cleaning_test.csv')
#     df.loc[7,"Duration"]= 45
#     print(df)

# import csv
# import pandas as pd
# with open("text.csv", "r") as f:

#     # df = pd.read_csv('cleaning_test.csv')
#     # for x in df.index:
#     #     if df.loc[x, "Duration"] > 120:
#     #         df.loc[x,"Duration"]= 120
#     # print(df)

#     df = pd.read_csv('cleaning_test.csv')
#     for x in df.index:
#         if df.loc[x, "Duration"] > 120:
#             df.drop(x,inplace= True)
#     # print(df.duplicated())
#     df.drop_duplicates(inplace = True)
#     # print(df)
#     df.to_csv("output", index = False)

#     df.corr() #correlation
#     # remove duplicates

    #Matplotlib, power Bi, snowsight, tableau
import matplotlib.pyplot as plt
 
x = [1,2,3,4,5]
y = [2,3,5,7,11]
 
x1 = [6,7,8,9,10]
y1 = [2,3,5,7,11]
 
plt.plot(x,y, marker='o',linestyle='--',color='b',label='Prime Numbers')
 
plt.plot(x1,y1, marker='o',linestyle='-',color='r',label='Numbers')
 
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Prime numbers Plot')
 
plt.legend()
 
plt.show()