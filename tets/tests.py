from testing_1.src.math_class import *
import unittest


class equivalenceClassTests(unittest.TestCase):

    minRange = 1.582
    maxRange = 63.062

    testObject = MathForTests()

    def test_moreThanRangeTM1(self):
        self.assertRaises(MoreThanRange, self.testObject.testMethod1, self.maxRange*10)


    def test_lessThanRangeTM1(self):
        self.assertRaises(LessThanRange, self.testObject.testMethod1, self.minRange/10)


    def test_inRangeTM1(self):
        self.assertEqual(41752645.70449739, self.testObject.testMethod1(self.maxRange - self.minRange))

    def test_moreThanRangeTM2(self):
        self.assertRaises(MoreThanRange, self.testObject.testMethod2, self.maxRange*10)


    def test_lessThanRangeTM2(self):
        self.assertRaises(LessThanRange, self.testObject.testMethod2, self.minRange/10)


    def test_inRangeTM2(self):
        self.assertEqual(867299.8678830718, self.testObject.testMethod2(self.maxRange - self.minRange))

    def test_moreThanRangeTM3(self):
        self.assertRaises(MoreThanRange, self.testObject.testMethod3, self.maxRange*10)


    def test_lessThanRangeTM3(self):
        self.assertRaises(LessThanRange, self.testObject.testMethod3, self.minRange/10)


    def test_inRangeTM3(self):
        self.assertEqual(8403.391340799999, self.testObject.testMethod3(self.maxRange - self.minRange))

    def test_moreThanRangeTM4(self):
        self.assertRaises(MoreThanRange, self.testObject.testMethod4, self.maxRange*10)


    def test_lessThanRangeTM4(self):
        self.assertRaises(LessThanRange, self.testObject.testMethod4, self.minRange/10)


    def test_inRangeTM4(self):
        self.assertEqual(604.0409999999999, self.testObject.testMethod4(self.maxRange - self.minRange))



class BoundaryValueClassTests(unittest.TestCase):

    minRange = 1.582
    maxRange = 63.062

    testObject = MathForTests()

    def test_moreThanRangeTM1(self):
        self.assertRaises(MoreThanRange, self.testObject.testMethod1, self.maxRange + 0.001)

    def test_lessThanRangeTM1(self):
        self.assertRaises(LessThanRange, self.testObject.testMethod1, self.minRange - 0.001)

    def test_inMinRangeTM1(self):
        self.assertEqual(20.926230675936768, self.testObject.testMethod1(self.minRange))

    def test_inMaxRangeTM1(self):
        self.assertEqual(46197791.381305054, self.testObject.testMethod1(self.maxRange))

    def test_moreThanRangeTM2(self):
        self.assertRaises(MoreThanRange, self.testObject.testMethod2, self.maxRange + 0.001)

    def test_lessThanRangeTM2(self):
        self.assertRaises(LessThanRange, self.testObject.testMethod2, self.minRange - 0.001)

    def test_inMinRangeTM2(self):
        self.assertEqual(9.988802870087998, self.testObject.testMethod2(self.minRange))

    def test_inMaxRangeTM2(self):
        self.assertEqual(936354.9303139934, self.testObject.testMethod2(self.maxRange))

    def test_moreThanRangeTM3(self):
        self.assertRaises(MoreThanRange, self.testObject.testMethod3, self.maxRange + 0.001)

    def test_lessThanRangeTM3(self):
        self.assertRaises(LessThanRange, self.testObject.testMethod3, self.minRange - 0.001)

    def test_inMinRangeTM3(self):
        self.assertEqual(12.315022048000001, self.testObject.testMethod3(self.minRange))

    def test_inMaxRangeTM3(self):
        self.assertEqual(8834.319256288, self.testObject.testMethod3(self.maxRange))

    def test_moreThanRangeTM4(self):
        self.assertRaises(MoreThanRange, self.testObject.testMethod4, self.maxRange + 0.001)

    def test_lessThanRangeTM4(self):
        self.assertRaises(LessThanRange, self.testObject.testMethod4, self.minRange - 0.001)

    def test_inMinRangeTM4(self):
        self.assertEqual(15.543149999999999, self.testObject.testMethod4(self.minRange))

    def test_inMaxRangeTM4(self):
        self.assertEqual(619.5841499999999, self.testObject.testMethod4(self.maxRange))



if __name__ == '__main__':
    unittest.main()
