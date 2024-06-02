import unittest

class TestMain(unittest.TestCase):#they are in classes
    
    def test_location(self):#has to start with test_{functionName}
        a = 'red'
        b = 'red'
        self.assertEqual(a,b)#if 2 values are equal

if __name__ == '__main__':#if we are in the app's main file run the unit test
    unittest.main()




