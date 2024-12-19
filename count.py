amount = int(input("Please Enter Withdrawal Amount: "))

note_100 = amount//100
note_50 = (amount%100)//50
note_10 = (amount%100%50)//10

print("the amount of 100 Taka is", note_100)
print("the amount of 50 Taka is", note_50)
print("the amount of 10 Taka is", note_10)