from backend import *
from Animal import *




import unittest

class TestStringMethods(unittest.TestCase):
    ZebraMussel = Animal("Zebra Mussel", "Mollusk", "Herbivore", "QC", "LC", 7.5E+14, "Invasive", "Freshwater lakes;Rivers")
    Moose = Animal("Moose", "Mammal", "Herbivore", "BC", "LC", 20000, "Native", "Woodlands")
    animalList = {ZebraMussel, Moose}

    def test_findAnimalByProvince(self):
        ZebraMussel = Animal("Zebra Mussel", "Mollusk", "Herbivore", "QC", "LC", 7.5E+14, "Invasive", "Freshwater lakes;Rivers")
        Moose = Animal("Moose", "Mammal", "Herbivore", "BC", "LC", 20000, "Native", "Woodlands")
        animalList = {ZebraMussel, Moose}
        result = find_by_province(animalList, "BC")  # Corrected to pass the province
        self.assertEqual(result, [Moose]) # Corrected to check for a list containing moose.

        result_qc= find_by_province(animalList, "QC")
        self.assertEqual(result_qc, [ZebraMussel])

        result_none = find_by_province(animalList, "AB")
        self.assertEqual(result_none, [])

    def test_findAnimalByDiet(self):
        result = search_by_diet(self.animalList, "Herbivore")
        self.assertEqual(result, [self.ZebraMussel, self.Moose])

        result_carnivore = search_by_diet(self.animalList, "Carnivore")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()