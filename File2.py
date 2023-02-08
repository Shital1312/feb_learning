import os

print(os.path.isfile("My-file.txt"))
'''isfile() ek method hai file hai ya nahi hai us path pai vo check karke aapko ek return boolen value deta hai. 
but for that first think is import os then os.path.isfile(filename) ye syntax use kar skte hai.'''
f = open('My-file.txt', 'r', encoding='utf-8')
if f:
    print("File open suceesfully")
print(f.name)  # you can print file name in your terminal
print(
    f.encoding)  # you can print file encoding value in your terminal If you didn't g.ive encodig value then it's print default value
print(f.mode)  # you can print file mode in your terminal
print(f.closed)  # you can print your file is closed or not with boolean value in your terminal
print(f.readable())  # you can print your file mode is readable or not with boolean value in your terminal
print(f.writable())  # you can print your file mode is writable or not with boolean value in your terminal
print(type(f))
# print(type(f))
