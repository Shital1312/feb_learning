import os

first_file = open('bolwer.txt', 'w')
l = ['Malinga\n', 'Zahir khan\n', 'Harbajan singh']
first_file.writelines(l)
first_file.close()
second_file = open("Batsman.txt", 'w')
name = ["Sachin\n", "M.S.Dhoni\n", "Rohit Sharma"]
second_file.writelines(name)
second_file.close()
third_file = open("coach.txt", 'w')
coach_name = ["Yuvraj singh\n", 'Ravindra jadeja\n', 'Pathan']
third_file.writelines(coach_name)
third_file.close()
files = []
mearge_data = ""

while True:
    f_name = input("Enter your file name: ")
    files.append(f_name)
    ans = input("Want to do add another file : ").lower()
    if ans != 'y':
        break

for file in files:
    filename = file+'.txt'
    if os.path.isfile(filename):
        f= open(filename, mode = 'r', encoding='utf-8')
        mearge_data += f.read()+'\n'
        f.close()
print(mearge_data)

with open(input("Enter your final file name") +'.txt', 'x') as f:
    f.write(mearge_data)
    print("Mearging is done , Thanks")


