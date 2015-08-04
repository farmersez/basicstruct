import pickle
import unittest

from basicstruct import BasicStruct


class Foo(BasicStruct):
    __slots__ = ('x', 'y')


class MyTestCase(unittest.TestCase):
    def test_attribute_access(self):
        f = Foo(2, 'blah')
        self.assertEqual(f.x, 2)
        self.assertEqual(f.y, 'blah')

    def test_attribute_access_with_kwargs(self):
        f = Foo(x=2, y='blah')
        self.assertEqual(f.x, 2)
        self.assertEqual(f.y, 'blah')

    def test_attribute_access_partly_kwargs(self):
        f = Foo(2, y='blah')
        self.assertEqual(f.x, 2)
        self.assertEqual(f.y, 'blah')

    def test_attribute_access_missing_values(self):
        f = Foo(2)
        self.assertEqual(f.x, 2)
        self.assertEqual(f.y, None)

    def test_attribute_access_missing_values_partial_kwargs(self):
        f = Foo(y=2)
        self.assertEqual(f.x, None)
        self.assertEqual(f.y, 2)

    def test_comparisons(self):
        small = Foo(1, 'irreleant')
        medium = Foo(2, 5)
        another_medium = Foo(2, 5)
        large = Foo(2, 15)

        self.assertEqual(medium, another_medium)

        self.assertTrue(small < medium)
        self.assertTrue(small < large)
        self.assertTrue(small <= medium)
        self.assertTrue(small <= large)
        self.assertTrue(medium < large)
        self.assertTrue(medium <= another_medium)
        self.assertTrue(another_medium <= medium)

        self.assertTrue(medium > small)
        self.assertTrue(large > small)
        self.assertTrue(medium >= small)
        self.assertTrue(large >= medium)
        self.assertTrue(large > medium)
        self.assertTrue(medium >= another_medium)
        self.assertTrue(another_medium >= medium)

        self.assertTrue(small != medium)
        self.assertTrue(medium != small)
        self.assertTrue(medium != large)
        self.assertTrue(large != medium)

        with self.assertRaises(TypeError):
            small < 1

        with self.assertRaises(TypeError):
            small <= 1

        with self.assertRaises(TypeError):
            small > 1

        with self.assertRaises(TypeError):
            small >= 1

        self.assertFalse(small == 1)
        self.assertTrue(small != 1)

    def test_repr(self):
        f = Foo(1, 'irrelevant')
        self.assertEqual(repr(f), "Foo(x=1, y='irrelevant')")

    def test_pickle(self):
        f = Foo(1, 'irrelevant')
        self.assertEqual(f, pickle.loads(pickle.dumps(f)))


if __name__ == '__main__':
    unittest.main()
