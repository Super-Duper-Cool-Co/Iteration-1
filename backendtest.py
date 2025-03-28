from backend import *
from Animal import *




import unittest

class TestBackend(unittest.TestCase):
    fields, data = load_data()

    def test_save_data(self):
        # Test if the data is saved correctly
        save_data(self.fields, self.data)
        self.assertTrue(fields,["Animal                    ", "Class    ", "Diet       ", "Province", "Endangered Status", "Population", "Native/Invasive", "Habitat"])

    def test_getAnimal(self):
        # Test if the getAnimals function returns the correct data
        Moose = get_animal_description(self.data, "Moose")
        self.assertEqual(Moose.name, "Moose")
    def test_getAnimalProvince(self):
        # Test if the getAnimalProvince function returns the correct data
        BC= find_by_province(self.data, "BC")
        isBc=True
        for animal in BC:
            if animal.province != "BC":
                isBc=False
                break
        self.assertTrue(isBc)

    def test_getAnimalDiet(self):
        # Test if the getAnimalDiet function returns the correct data
        Carnivore = search_by_diet(self.data, "Carnivore")
        isCarnivore=True
        for animal in Carnivore:
            if animal.diet != "Carnivore":
                isCarnivore=False
                break
        self.assertTrue(isCarnivore)

    
if __name__ == '__main__':
    unittest.main()