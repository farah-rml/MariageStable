from Student import Student

class MariageStable:

    def __init__(self, students_preferences, schools_preferences):

        self.schools_preferences = schools_preferences
        self.n=len(schools_preferences)
        self.students=[]

        for i in range(self.n):
            self.students.append(
                Student(students_preferences[i],i)
            )
        
		#afin de calculer plus simplement les preferences, on crée une liste des classements ordonnés, tel que : schools_rank[e][s] = rang de student s pour l'école e
        self.create_rank(schools_preferences) 
        
        self.rejected ={Student for Student in self.students} #les etudiants sans écoles, donc tous au début
        self.matches=[None]*self.n 
    
    def create_rank(self, schools_preferences):
        self.schools_rank = [
			[0]*self.n
			for _ in range(self.n)
		]
        for e in range(self.n):                       
            for rank, student in enumerate(schools_preferences[e]):
                self.schools_rank[e][student]=rank#les étudiants choisis par les écoles 

    def hasNext(self):
        return len(self.rejected)>0
    
    def reject(self,student):
        student.incrementCursor()
        self.rejected.add(student)
    
    def next(self):
        student = self.rejected.pop()
        preferred_school = student.getPreferredSchool()
        currentChosenStudentIndex = self.matches[preferred_school]

        if student.isBetterThan(currentChosenStudentIndex,self.schools_rank[preferred_school]):
            self.matches[preferred_school]=student.getIndex()
            if currentChosenStudentIndex is not None:
                self.reject(self.students[currentChosenStudentIndex])
            return (student.getIndex(), preferred_school)
        else:
            self.reject(student)
            return (student.getIndex(), None)

    def solve(self, verbose):
        while self.hasNext():
            stepResult = self.next()
            if verbose:
                print(stepResult)
        return self.matches

