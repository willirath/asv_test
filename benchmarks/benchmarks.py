# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.


from asv_test import do_something


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        for x in range(1_500):
            self.d[x] = None

    def time_keys(self):
        for key in self.d.keys():
            pass

    def time_values(self):
        for value in self.d.values():
            pass

    def time_range(self):
        d = self.d
        for key in range(1500):
            d[key]


class TimeSomething:
    def time_something():
        do_something()


class MemSuite:
    def mem_list(self):
        return [0] * 1024
