class Student:
    def __init__(self, preferences, index):
        self.preferences=preferences
        self.index=index
        self.cursor=0

    def incrementCursor(self):
        self.cursor+=1

    def getIndex(self):
        return self.index

    def getCursor(self):
        return self.cursor
    
    def getPreferences(self):
        return self.preferences
    
    def getPreferredSchool(self):
        return self.preferences[self.cursor]
    
    # which student is preferred by the given school's rank?
    def isBetterThan(self,student2,school_rank):
        if student2==None:
            return True
        return school_rank[self.index]<school_rank[student2]
    