import unittest
from exercises_tests import city_country, city_country_population


class CitiesTestCase(unittest.TestCase):
    """Test for 'city_functions.py"""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago Chile')

    def test_city_country_population(self):
        """Does a simple city, country and population work"""
        stockholm_sweden_2000000 = city_country_population(
            'stockholm', 'sweden', 2_000_000)
        self.assertEqual(stockholm_sweden_2000000, 'Stockholm Sweden 2000000')


if __name__ == "__main__":
    unittest.main()
