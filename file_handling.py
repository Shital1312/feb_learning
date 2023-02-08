'''Create new file using x, also you can create file with "w"'''
# f = open("My-file.txt", "w") you can use this syntax and create new txt file in python.
# f = open("My-file.txt", "x")# you can create new txt file in python.
f = open("My-file.txt", "w")
f.write("Hello\n")  # use this sentence for write some data for your txt. file.
l = ["This is a new file.\n", "This is a txt file.\n", "We are create this file for practice."]
f.writelines(l)  # use this sentence for write group of line in your txt file you can add list/set/tuple.
f.close()
# f = open("My-file.txt", "r")
# print(f.read()) # use this sentence for read text in txt. file in your terminal
f.close()  # use the close() to change file access modes
# print("Readline ")
# f = open("My-file.txt", "r")
# print(f.readline())  # use readline for read only first line in your txt file
# print(f.readline())  # if you again print readline then you can show next line. you put any index with readline then you
# can show value for 0 to n index.
# print(f.readlines()) # use readlines for read all lines in your terminal.
# f.close()
f = open("My-file.txt", "a")
update_data = f.write("\nYou can use 'a' and update your data in your txt file.")
f.close()
'''Handle read and write both at a one time.'''
f = open("My-file.txt", "r+")
print(f.read())
f.write("\nThank you")
print(f.readlines())
print(f.name)
f.close()
