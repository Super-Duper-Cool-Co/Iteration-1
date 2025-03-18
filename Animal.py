class Animal:
    def __init__(self, name,type, diet, province, endangerStatus, population, invasiveStatus, habitat ):
        self.name=name.strip()
        self.type=type.strip()
        self.diet=diet.strip()
        self.province=province.strip()
        self.endagerStatus=endangerStatus.strip()
        self.population=population
        self.invasiveStatus=invasiveStatus.strip()
        self.habitat=habitat.strip()

    def toString(self):
        print( f"Name: {self.name}, Type: {self.type}, Diet: {self.diet}, Province: {self.province}, Endanger Status: {self.endagerStatus}, Population: {self.population}, Invasive Status: {self.invasiveStatus}, Habitat: {self.habitat}")