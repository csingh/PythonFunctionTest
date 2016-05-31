import inspect
from PurrdyPrinter import *
import traceback

class FunctionTester:
    def __init__(self, function):
        self.function = function
        self.args = inspect.getargspec(function).args
        self.tests = []

    def numArgs(self):
        return len(self.args)

    def addTest(self, expected_val, *args):
        self.tests.append([expected_val, args])

    def __get_test_expected_val__(self, test):
        return test[0]

    def __get_test_args__(self, test):
        return test[1]

    def runTests(self):
        num_tests = len(self.tests)
        num_failed = 0

        PurrdyPrinter.put("underline", "{} - Running {} tests:".format(self.function.__name__, num_tests))

        for test in self.tests:
            expected_val = self.__get_test_expected_val__(test)
            args = self.__get_test_args__(test)

            args_string = ",".join( [str(x) for x in args] )
            func_and_args = "{}({})".format(self.function.__name__, args_string)

            try:
                ans = self.function(*args)

                if ans == expected_val:
                    PurrdyPrinter.put("green", "{} passed.".format(func_and_args))
                else:
                    PurrdyPrinter.put("red", "{} failed.".format(func_and_args))
                    PurrdyPrinter.put("red", "   Expected: {}".format(expected_val))
                    PurrdyPrinter.put("red", "        Got: {}".format(ans))
                    num_failed += 1
            except Exception as ex:
                PurrdyPrinter.put("red", "{} failed.".format(func_and_args))
                PurrdyPrinter.put("red", "   Exception: {}".format(ex))
                PurrdyPrinter.put("pink", "   {}".format(traceback.format_exc()))
                num_failed += 1


        if num_failed == 0:
            PurrdyPrinter.put("blue", "\nAll tests passed!")
        else:
            PurrdyPrinter.put("yellow", "\n{} tests failed. :(".format(num_failed))


    def __str__(self):
        return "FunctionTester: function <{}>, numArgs={}, args={}".format(
            self.function.__name__,
            self.numArgs(),
            self.args
            )

def oneArg(A):
    return (A)

def twoArgs(A,B):
    return (A,B)

if __name__ == '__main__':
    FT1 = FunctionTester(oneArg)
    FT2 = FunctionTester(twoArgs)

    FT1.addTest(1, 1)
    FT1.addTest(True, True)
    FT1.addTest(1, 2)

    FT1.runTests()
