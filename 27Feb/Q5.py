class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtain(self):
        total = self.phy + self.chem + self.bio
        return total

    def percentage(self):
        Percentage = (self.totalObtain() / 300) * 100
        return Percentage


a = Student('Mark', 80, 90, 40)
print(a.percentage())
