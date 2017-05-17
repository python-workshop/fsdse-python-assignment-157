from unittest import TestCase


class TestBuild(TestCase):
    #check if the array is none then return false
    #check if not array then return []
    #check for the sorted list
    def test_check_if_the_array_is_none_then_return_false(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Faliure")

        value = build(None,base=10)
        self.assertEqual(False,value)

    def test_check_if_not_array_then_return(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Faliure")

        value = build("",base=10)
        self.assertEqual([],value)

    def test_check_for_sorted_list(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Faliure")

        value = build([120,110,121,123],base=10)
        self.assertEqual([110,120,121,123],value)


