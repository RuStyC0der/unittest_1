
class MoreThanRange(ValueError):
    pass

class LessThanRange(ValueError):
    pass


class MathForTests:

    minRange = 1.582
    maxRange = 63.062

    @classmethod
    def rangeCheck(cls, x):
        if x > cls.maxRange:
            raise MoreThanRange
        elif x < cls.minRange:
            raise LessThanRange
        else:
            return True

    @staticmethod
    def output(result):
        # print("you result is: ", result)
        return result

    def testMethod1(self, x):
        self.rangeCheck(x)
        y = (x ** 4) * 2.868 + (x ** 3) * 3.429 - (x ** 2) * 4.987 + x * 1.18
        return self.output(y)

    def testMethod2(self, x):
        self.rangeCheck(x)
        y = (x ** 3) * 3.791 - (x ** 2) * 3.656 + x * 2.61
        return self.output(y)

    def testMethod3(self, x):
        self.rangeCheck(x)
        y = (x ** 2) * 2.152 + x * 4.38
        return self.output(y)

    def testMethod4(self, x):
        self.rangeCheck(x)
        y = x * 9.825
        return self.output(y)




if __name__ == '__main__':
    a = MathForTests()
    minRange = 1.582
    maxRange = 63.062
    print(a.testMethod1(2))
    print(a.testMethod2(2))
    print(a.testMethod3(2))
    print(a.testMethod4(2))
    print(a.testMethod1(maxRange - minRange))
    print(a.testMethod1(minRange-1))