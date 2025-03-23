from backend import *
from Animal import *




import unittest

class TestStringMethods(unittest.TestCase):
    ZebraMussel = Animal("Zebra Mussel", "Mollusk", "Herbivore", "QC", "LC", "7.5E+14", "Invasive", "Freshwater lakes;Rivers")
    Moose = Animal("Moose", "Mammal", "Herbivore", "BC", "LC", "20000", "Native", "Woodlands")
    fox = Animal("fox", "Mammal", "Carnivore", "BC", "LC", "20000", "Native", "Woodlands")
    animalList = {ZebraMussel, Moose, fox}

    def test_findAnimalByProvince(self):
        result = find_by_province(self.animalList, "BC")
        self.assertEqual(result, [self.Moose,self.fox])

        result_qc = find_by_province(self.animalList, "QC")
        self.assertEqual(result_qc, [self.ZebraMussel])

        result_none = find_by_province(self.animalList, "AB")
        self.assertEqual(result_none, None)

    def test_findAnimalByDiet(self):
        result = search_by_diet(self.animalList, "Herbivore")
        self.assertEqual(result, [self.ZebraMussel,self.Moose])

        result_carnivore = search_by_diet(self.animalList, "Carnivore")
        self.assertEqual(result_carnivore, [self.fox])

    def test_getAnimalDescritpion(self):
        ZebraMussel = Animal("Zebra Mussel", "Mollusk", "Herbivore", "QC", "LC", "7.5E+14", "Invasive", "Freshwater lakes;Rivers")
        Moose = Animal("Moose", "Mammal", "Herbivore", "BC", "LC", "20000", "Native", "Woodlands")
        fox = Animal("fox", "Mammal", "Carnivore", "BC", "LC", "20000", "Native", "Woodlands")
        animalList = {ZebraMussel, Moose, fox}
        result_Moose = get_animal_description(animalList, "Zebra Mussel")
        self.assertEqual(result_Moose, [ZebraMussel])

        result_Fox = get_animal_description(animalList, "fox")
        self.assertEqual(result_Fox, [fox])

    
if __name__ == '__main__':
    unittest.main()