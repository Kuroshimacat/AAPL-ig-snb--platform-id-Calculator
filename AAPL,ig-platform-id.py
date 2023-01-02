import re
data = input("Please input raw data: ")
data1 = data.split("x")
data2 = re.findall(r'.{2}', data1[1])
print("Your AAPL,ig(snb)-platform-id is: "+data2[3]+data2[2]+data2[1]+data2[0])