import os
import sys
import unittest


class TestPrediction(unittest.TestCase):

    def test_valid_image_input(self):
        test_image_path = 'tests/data/valid_test_image.jpg'
        expected_gender = 'Male'
        expected_age = 25
        result = predict(test_image_path)
        self.assertEqual(result['gender'], expected_gender)
        self.assertEqual(result['age'], expected_age)

    def test_invalid_image_input(self):
        test_image_path = 'tests/data/invalid_test_file.txt'
        with self.assertRaises(ValueError):
            predict(test_image_path)

    def test_edge_cases(self):
        young_image_path = 'tests/data/young_test_image.jpg'
        old_image_path = 'tests/data/old_test_image.jpg'
        young_result = predict(young_image_path)
        old_result = predict(old_image_path)
        self.assertTrue(0 <= young_result['age'] <= 10)
        self.assertTrue(70 <= old_result['age'] <= 100)

if __name__ == '__main__':
    unittest.main()
