def employee(**details):
    for key,value in details.items():
        print(key ,":",value)
        
employee(name = "pradip",
        age = 22,
        coures = "data science",
        salary = 23000)

print("=====================")

employee(name= "vivek",
         age = 22,
         salary = 20000,
         department = "computer science")

print("========================")

employee(name = "ved",
         age = 22,
         salary = 30000,
         department = "IT")