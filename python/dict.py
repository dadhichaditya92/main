customer = {
    "name" : "Aditya Dadhich",
    "Age": 35,
    "Gender": "Male",
    "Address": "A85N921"
}
employee = [
    {"name" :"Akanksha", "age" : 32, "Gender" : "female"},
    {"name" : "aditya", "age" : 35, "Gender" : "male"}
]
for emp in employee:
    print("Employee Details")
    for key in emp:
        value = emp[key]
        print(f"{key}: {value}")
    print()