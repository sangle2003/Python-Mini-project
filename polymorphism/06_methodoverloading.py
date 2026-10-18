class Demo:
    def add(self,*nums):
        return sum(nums)
    
d = Demo()
print(d.add(1,2,3,4))
print(d.add(10,20,30))
print(d. add(10, 20, 10, 10, 10, 10, 10, 10, 10))