from unittest import TestCase

from f4py.Maybe import nothing, just


class TestMaybe(TestCase):
    def setUp(self):
        self.empty = nothing()
        self.filled = just(5)

    def test_is_present(self):
        self.assertTrue(self.filled.is_present())
        self.assertFalse(self.empty.is_present())

    def test_is_nothing(self):
        self.assertFalse(self.filled.is_nothing())
        self.assertTrue(self.empty.is_nothing())

    def test_map_empty(self):
        mapper = lambda x: x + 1
        resultFilled = self.filled.map(mapper)
        resultEmpty = self.empty.map(mapper)
        self.assertTrue(resultFilled.is_present())
        self.assertFalse(resultEmpty.is_present())
        self.assertEqual(resultFilled.get(), 6)

    def test_map_filled(self):
        pass

    def test_map_filled_to_empty(self):
        pass

    def test_flat_map(self):
        self.fail()

    def test_filter(self):
        self.fail()

    def test_or_else(self):
        self.fail()

    def test_flat_or_else(self):
        self.fail()

    def test_or_else_compute(self):
        self.fail()

    def test_get(self):
        self.fail()

    def test_of(self):
        self.fail()
