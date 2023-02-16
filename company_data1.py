import json


def salary_credit():
	f = open('company_data.json', mode='r')
	data_dict = json.load(f)
	# print(data_dict['Employees'])# you can print all employee data this way.
	for key in data_dict['Employees']:
		# print(key)# you can print employee id this way.
		# print(data_dict['Employees'][key])# you can get all employess key's value this way.
		if data_dict['Employees'][key]['Bank_Name'] == "Bank of Maharashtra":
			print("Process Salary.")
			print(f"Salary {data_dict['Employees'][key]['salary']} is processing {data_dict['Employees'][key]['Account_Number']}")
	f.close()


salary_credit()
