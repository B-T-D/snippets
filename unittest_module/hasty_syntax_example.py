import unittest
	
import petals_funcs as pf

class TestNumSegments(unittest.TestCase):

    def setUp(self):
         pass

    def test_num_segments_returns_int(self):
        """Confirms that the function that returns the number of segments returns an  integer."""
        ret_obj = pf.num_segments(petals=8)
        self.assertIs(int, type(ret_obj))

class TestDegrees(unittest.TestCase):
    """Tests for the function(s) that return the number of degrees to be
    used in turning the turtle 'arrow' to draw the next segment."""

    def test_multiple_of_360(self):
        """Is total number of degrees (degrees * number of petals) a multiple
        of 360?"""
        for i in range(5, 100):
            print(i)
            total_degrees = pf.degrees(i) * i
            print(f"total degrees is {total_degrees}")
            self.assertEqual(0, total_degrees % 360)
    
if __name__ == '__main__':
    unittest.main()
