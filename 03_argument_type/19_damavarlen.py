def profile(**data):
    if "name" in data:
        print("Name is :: ",data["name"])
        
profile(name="Raj",city="pune")
profile(name = "raj")