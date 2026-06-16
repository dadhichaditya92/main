student = [10, 20, 347, 654, 786 ,856, 346, 764, 879, 978, 654, 341]
sum = 0
for score in student:
    sum = sum+score

print("sum of the score is", sum)
max_score = 0
for maximum in student:
    if maximum > max_score:
        max_score = maximum

print (max_score)
