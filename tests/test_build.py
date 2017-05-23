from unittest import TestCase


class TestBuild(TestCase):
    def test_check_if_the_array_is_none_then_return_false(self):
        try:
            from build import sort
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, sort, None)
        self.assertEqual(sort([]), [])
        array = [128, 256, 164, 8, 2, 148, 212, 242, 244]
        expected = [2, 8, 128, 148, 164, 212, 242, 244, 256]
        self.assertEqual(sort(array), expected)



