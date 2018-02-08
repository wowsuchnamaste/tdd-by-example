from xunit_example import *


class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert 'set_up test_method tear_down ' == test.log

    def test_result(self):
        test = WasRun('test_method')
        result = test.run()
        assert '1 run, 0 failed' == result.summary()

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        result = test.run()
        assert '1 run, 1 failed' == result.summary()


if __name__ == '__main__':
    TestCaseTest('test_template_method').run()
    TestCaseTest('test_result').run()
    TestCaseTest('test_failed_result').run()