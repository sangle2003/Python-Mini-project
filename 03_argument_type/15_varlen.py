def max(*num):
    max_value=num[0]
    for i in num:
        if i>max_value:
            max_value=i
        print(max_value)
        
max(1,2,9,0,8,6,4,5,7)
max(100,2666,777,88,45,34,56)