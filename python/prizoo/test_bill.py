'''
Created on May 24, 2016

@author: wjadams
'''
import unittest
import numpy as np
from bill import geom_avg, geom_avg_mat, gm_priorities, bpriorities


class Test(unittest.TestCase):

    testMat1 = np.array([[1, 2, 6], [1./2, 1, 3], [1./6, 1./3, 1]])
    def test_geom_avg(self):
        x = [2, 8]
        v = geom_avg(x)
        self.assertEqual(v, 4.0, "Problem with geom_avg")
        
    def test_geom_avg_mat(self):
        info = geom_avg_mat(self.testMat1)
        ideal = info / max(info)
        #print(info)
        np.testing.assert_array_almost_equal(ideal, [1, 0.5, 1./6], 6, "Whoops, didn't work")
        np.testing.assert_almost_equal(max(info), 2.289428, 6, "Whoops again")

    def test_gm_priorities(self):
        val = gm_priorities(self.testMat1)
        actual= [0.6, 0.3, 0.1]
        np.testing.assert_array_almost_equal(val, actual, 6)
        
    def test_bpriorities(self):
        val = bpriorities(self.testMat1)
        actual= [0.6, 0.3, 0.1]
        np.testing.assert_array_almost_equal(val, actual, 6)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_geom_avg']
    unittest.main()