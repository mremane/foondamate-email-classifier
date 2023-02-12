import unittest
from classifier import Classifier

class TestClassifier(unittest.TestCase):

    def setUp(self):
        self._classifier = Classifier('model.pkl')
        
    def test_none(self):
        self.assertRaises(TypeError, self._classifier.classify)
    
    def test_null(self):
        self.assertRaises(ValueError, self._classifier.classify, '') # call with empty string
        
    def test_classify_one(self):
        self.assertEqual(self._classifier.classify('Can I share your email'), 'Student wants to know if can share.', 'Classification is wrong.')
    
    def test_classify_two(self):
        self.assertEqual(self._classifier.classify('May we share your email'), 'Student wants to know if can share.', 'Classification is wrong.')
        
    def test_classify_three(self):
        self.assertEqual(self._classifier.classify('I have shared your email'), 'Student has shared.', 'Classification is wrong.')

    if __name__ == '__main__':
        unittest.main()