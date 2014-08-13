import json


class Param(object):

    def __init__(self, doc):
        self._doc = doc

    def valid_header(self):
        return self._doc.split('\n', 1)[0].strip() == "scenarios:"

    def args(self):
        for line in self._doc.split('\n')[1:]:
            line = line.strip()
            if line:
                yield json.loads(line)

    def test_cases(self, base_name):
        for c, arg in enumerate(self.args()):
            test_name = 'test_%s_%s' % (base_name, c)

            def cloj(arg):
                def test_f(self):
                    f = getattr(self, base_name)
                    return f(*arg)
                return test_f
            yield test_name, cloj(arg)


def autoscenarios(klass):
    for f_name in dict(vars(klass)):
        f = getattr(klass, f_name)
        if callable(f) and f.__doc__:
            scenarios = Param(f.__doc__)
            if scenarios.valid_header():
                for test_name, test_f in scenarios.test_cases(f.__name__):
                    setattr(klass, test_name, test_f)
    return klass


def pytest_generate_tests(metafunc):
    func_args = metafunc.funcargnames
    f = metafunc.function
    if callable(f) and f.__doc__:
        param = Param(f.__doc__)
        if param.valid_header():
            metafunc.parametrize(func_args, [arg for arg in param.args()])
