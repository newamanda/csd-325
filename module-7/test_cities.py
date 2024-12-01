#Amanda New
#CSD325-A311
#Module 7.2 Assignment
#Test Cases
#Test Cities

#import unittest and importing city_country function from city_functions.py
import unittest
from city_functions import city_country

#Test case
class CityTestCode(unittest.TestCase):

    #City and country test
    def test_city_country(self):
        testing_city = city_country('London', 'England')
        self.assertEqual(testing_city, 'London, England')

    #Optional population test
    def test_city_population(self):
        testing_city = city_country('London', 'England', population= 9_000_000,)
        self.assertEqual(testing_city, 'London, England - Population: 9000000')

    #Optional language test
    def test_city_language(self):
        testing_city = city_country('London', 'England', 'Population: 9000000', 'Language: English')
        self.assertEqual(testing_city, 'London, England - Population: Population: 9000000, Language: Language: English')

if __name__ == '__main__':
    unittest.main()


    


