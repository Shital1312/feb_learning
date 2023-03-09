first_condited = input("Enter condited name : ")
secount_condited = input("Enter condited name : ")
f_count = 0
s_count = 0
voter_Id = [101, 102, 103, 104, 105, 106]
no_of_voters = len(voter_Id)
voted = []
while True:
	if voter_Id == []:
		print("Voting is over")
		if f_count > s_count:
			print(f"{first_condited} is won with {f_count} votes.")
		elif s_count > f_count:
			print(f"{secount_condited} is won with {s_count} votes")
		elif s_count == f_count:
			print("Tied!!!!!!!")
		break
	else:
		voter = int(input("Enter your voter id."))

		if voter in voted:
			print("You are already voted.")
		else:
			if voter in voter_Id:
				print(f"1.{first_condited}\n 2.{secount_condited}")
				choice = int(input("Enter your choice."))
				if choice > 2:
					print("Please select valid candited.")
					choice = int(input("Enter your choice."))
				if choice == 1:
					f_count += 1
					print(f"you voted {first_condited}")
				elif choice == 2:
					s_count += 1
					print(f"you vated {secount_condited}")
				voter_Id.remove(voter)
				voted.append(voter)
			else:
				print("You are not allowed to vote.")
