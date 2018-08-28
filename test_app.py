import unittest

from questions import questions
from app import *


        

class TestQuestions(unittest.TestCase):
    '''
    Function that finds the question from the dictionary
    '''
    def test_ask_question(self):
        self.assertEqual(ask_question(1), "What is the common name for this tree?")
        self.assertEqual(ask_question(2), "What is the common name for this tree?")
        
        
    

#http://flask.pocoo.org/docs/0.12/testing/#accessing-and-modifying-sessions

if __name__ == '__main__':
    unittest.main()