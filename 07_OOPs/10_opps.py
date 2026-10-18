class courses:
    def __init__(self,courseid,coursename,duration):
        self.courseid = courseid
        self.coursename = coursename
        self.duration = duration
        
s1 = courses(1,"datascience",6)
print("courseid :: ",s1.courseid, "course name :: ",s1.coursename, "duration :: ",s1.duration)
        