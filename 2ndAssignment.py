Eng_num_obtained = 60
Math_num_obtained = 75
Islamiyat_num_obtained = 80
Total_obtained_num = Eng_num_obtained+Math_num_obtained+Islamiyat_num_obtained
Total_num =300
percentage_num = (Total_obtained_num/Total_num)*100
print("Total marks are " ,Total_num)
print("You Obtained",Total_obtained_num)
print("Your percentage is",percentage_num )
if percentage_num >80:
    print("grade = A+")
elif percentage_num>70 and  percentage_num< 80:
    print("grade = A")
elif percentage_num>60 and  percentage_num< 70:
    print("grade = B+")
elif percentage_num>50 and  percentage_num< 60:
    print("grade = B")
elif percentage_num>40 and  percentage_num< 50:
    print("grade = C")
elif percentage_num>33 and  percentage_num< 40:
    print("grade = D")
else:
    print("Sorry try again next time")
    



