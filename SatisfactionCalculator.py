class SatisfactionCalculator:
    def __init__(self,students_preferences,schools_preferences,matches):

        self.students_preferences = students_preferences
        self.schools_preferences = schools_preferences

        self.matches = matches

        self.n=len(schools_preferences)

        self.percentage_loss = 100//self.n 

        self.students_satisfaction = [100]*self.n
        self.schools_satisfaction = [100]*self.n

        self.calculate_satisfaction()
    
    def calculate_satisfaction(self):
        for i in range(self.n):
            self.students_satisfaction[i] -= self.getStudentGivenSchool(i)*self.percentage_loss
            self.schools_satisfaction[i] -= self.getSchoolGivenStudent(i)*self.percentage_loss
    
    def getStudentGivenSchool(self,student_index):
        return self.students_preferences[student_index].index(self.matches.index(student_index))
    
    def getSchoolGivenStudent(self,school_index):
        return self.schools_preferences[school_index].index(self.matches[school_index])

    def getAverageStudentSatisfaction(self):
        return sum(self.students_satisfaction)/self.n
    
    def getAverageSchoolSatisfaction(self):
        return sum(self.schools_satisfaction)/self.n
    
    def getGlobalSatisfaction(self):
        return (self.getAverageStudentSatisfaction()+self.getAverageSchoolSatisfaction())/2
    
    def getStudentsSatisfaction(self):
        return self.students_satisfaction
    
    def getSchoolsSatisfaction(self):
        return self.schools_satisfaction