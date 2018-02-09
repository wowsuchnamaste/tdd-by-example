"""An example implementation of xUnit from TDD by example by Kent Beck."""


class TestException(Exception):
    """Raise when tests raise an exception."""


class TestCase:
    def __init__(self, name):
        self.name = name
        self.log = None
        self.result = None

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
        result.test_started()
        try:
            self.set_up()
        except (TestException, Exception):
            result.test_setup_failed()
            result.test_failed()
        else:
            try:
                method = getattr(self, self.name)
                method()
            except (TestException, Exception):
                result.test_failed()

        finally:
            self.tear_down()


class TestResult:
    def __init__(self):
        self.run_count = 0
        self.error_count = 0
        self.setup_fail_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self):
        return '%s run, %s failed' % (self.run_count, self.error_count)

    def test_failed(self):
        self.error_count += 1

    def test_setup_failed(self):
        self.setup_fail_count += 1


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)
