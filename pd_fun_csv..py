import pandas as pd

# print(pd.__version__)  # 1.5.3 check the which pandas version are you using.

# file = pd.read_csv("list_phone.csv",nrows=3)
# file = pd.read_csv("list_phone.csv", usecols=['Final_price'])# you can see particular coloum
file = pd.read_csv("list_phone.csv")
# print(file.index)  # RangeIndex(start=0, stop=20, step=1)
# print(file.columns)  # Index(['ID', 'PRODUCT_NAME', 'QUN', 'PRICE', 'Final_price'], dtype='object') // you can see all headers name
# f = file.sort_index(axis=0, ascending= False) # print reverse data
# print(f)
# f = file.replace(to_replace="Redmi_pro", value="Redmi_Note10") // you can replace value use this function
# print(f)
count = file['Final_price'][0:20]
# print(count)
sum1 = 0
for i in count:
	sum1 += i
# print(sum1)
# qun = file['QUN'][0:20]
# qun1 = 0
# for q in qun:
# 	qun1 = q+qun1
# print(f"Total item is : ", qun1)

dis = (sum1 * 12)/100
dis = round(dis)
total_price = sum1 - dis
# print(f"Total bill is : ", round(dis))
# df = pd.DataFrame({f"Total Price ": {sum1}, "Total discount ": {qun1}, "Final bill is ": {total_price}})
df = pd.DataFrame({'Total price': [sum1], 'Discount ': [dis], 'Final_Price':[total_price]})
df.to_csv("list_phone.csv", mode='a', index=False)
df_updated = pd.read_csv("list_phone.csv")
df_updated.to_csv("Update_Phone_list.csv", index=False)
