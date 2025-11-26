class SatisfactionCalculator:
    def __init__(self, students_preferences, schools_preferences, matches):
        self.students_preferences = students_preferences
        self.schools_preferences = schools_preferences
        self.matches = matches
        self.n = len(schools_preferences)
        self.students_satisfaction = [0.0] * self.n
        self.schools_satisfaction = [0.0] * self.n
        self.calculate_satisfaction()
    
    def calculate_satisfaction(self):
        for i in range(self.n):
            student_rank = self.getStudentGivenSchool(i)
            self.students_satisfaction[i] = round((1 - (student_rank / (self.n - 1))) * 100, 2)
            
            school_rank = self.getSchoolGivenStudent(i)
            self.schools_satisfaction[i] = round((1 - (school_rank / (self.n - 1))) * 100, 2)
    
    def getStudentGivenSchool(self, student_index):
        school_obtained = self.matches.index(student_index)
        return self.students_preferences[student_index].index(school_obtained)
    
    def getSchoolGivenStudent(self, school_index):
        student_obtained = self.matches[school_index]
        return self.schools_preferences[school_index].index(student_obtained)
    
    def getAverageStudentSatisfaction(self):
        return round(sum(self.students_satisfaction) / self.n, 2)
    
    def getAverageSchoolSatisfaction(self):
        return round(sum(self.schools_satisfaction) / self.n, 2)
    
    def getGlobalSatisfaction(self):
        return round((self.getAverageStudentSatisfaction() + self.getAverageSchoolSatisfaction()) / 2, 2)
    
    def getStudentsSatisfaction(self):
        return self.students_satisfaction
    
    def getSchoolsSatisfaction(self):
        return self.schools_satisfaction