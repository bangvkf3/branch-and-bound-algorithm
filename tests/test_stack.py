import unittest

from bnb.stack import PopEmptyStackError, Stack


class StackTest(unittest.TestCase):
    def test_init_stack(self):
        s = Stack()
        self.assertEqual(0, s.size())
        self.assertTrue(s.is_empty())

    def test_pop_from_empty_stack(self):
        s = Stack()
        with self.assertRaises(PopEmptyStackError):
            s.pop()

    def test_pust_one_element(self):
        s = Stack()
        s.push("apple")
        self.assertEqual(1, s.size())

    def test_pust_two_elements(self):
        s = Stack()
        s.push("apple")
        s.push("banana")
        self.assertEqual(2, s.size())

    def test_pop_from_stack_two_elements(self):
        s = Stack()
        first = "apple"
        second = "banana"
        s.push(first)
        s.push(second)
        self.assertEqual(second, s.pop())

    def test_pop_twice_from_stack_two_elements(self):
        s = Stack()
        first = "apple"
        second = "banana"
        s.push(first)
        s.push(second)
        self.assertEqual(second, s.pop())
        self.assertEqual(first, s.pop())
        self.assertTrue(s.is_empty())
