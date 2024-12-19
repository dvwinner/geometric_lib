import unittest
import segment, time, math

class SegmentTestCase(unittest.TestCase):
    def test_default(self):
        self.assertAlmostEqual(segment.distance(0, 0, 10, 10), (2 * (10 ** 2)) ** 0.5)
        self.assertAlmostEqual(segment.distance(0, 0, 3, 4), 5)
    
    def test_zero_len(self):
        self.assertEqual(segment.distance(0, 0, 0, 0), 0)
        self.assertEqual(segment.distance(5, 5, 5, 5), 0)
    
    def test_negative_coords(self):
        self.assertAlmostEqual(segment.distance(-5, -5, -8, -9), 5)
    
    def test_big_numbers(self): 
        start = time.time()
        self.assertAlmostEqual(segment.distance(0, 0, 10 ** 18, 10 ** 18), (2 * ((10 ** 18) ** 2)) ** 0.5)
        work_time = time.time() - start
        self.assertGreaterEqual(1, work_time)
    