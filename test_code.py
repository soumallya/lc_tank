from __future__ import division
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy
import unittest
import os

# This program is just for testing.

from LC_tank_both import voltage,voltage_derivative,response

class TestResponse(unittest.TestCase):
    def test_response1(self):                                        # The first test case is that when both ESR of both
        t = numpy.array(range(0,30000,1))                            # inductor and capacitor is 0 the gain must be 
        t = t/1000                                                   # perfectly zero at anti-resonating frequency.
        A = 1                                       
        i1,V1,t1,gain1 = response(A,1,1,0,0,1,t)                     # When L = 1 Henry. C = 1 Farad. Wr = 1 rad/sec
                                                                     # Checking the gain at Wr is zero or not.
        i2,V2,t2,gain2 = response(A,2,0.5,0,0,0.5,t)                 # When L = 0.5 Henry. C = 0.5 Farad. Wr = 2 rad/sec
            
        i3,V3,t3,gain3 = response(A,2,0.25,0,0,1,t)                  # When L = 0.25 Henry. C = 1 Farad. Wr = 2 rad/sec
            
        i4,V4,t4,gain4 = response(A,2,1,0,0,0.25,t)                  # When L = 1 Henry. C = 0.25 Farad. Wr = 2 rad/sec
        self.assertEqual(round(gain1,3),0)
        self.assertEqual(round(gain2,3),0)
        self.assertEqual(round(gain3,3),0) 
        self.assertEqual(round(gain4,3),0)
        
    
    def test_response2(self):
        t = numpy.array(range(0,30000,1))                            # The second test case tests when the magnitude of both 
        t = t/1000                                                   # L and C are same, then if the ESRs of both L and C are 
        A = 1                                                        # 1 ohm then the gain must be perfectly 1 for angular 
        w = 1                                                        # frequencies w = 1,2,5 rad/sec.
        i1,V1,t1,gain1 = response(A,w,1,1,1,1,t)
        i2,V2,t2,gain2 = response(A,w,0.5,1,1,0.5,t)
        w = 2
        i3,V3,t3,gain3 = response(A,w,1,1,1,1,t)
        i4,V4,t4,gain4 = response(A,w,0.5,1,1,0.5,t)
        w = 5
        i5,V5,t5,gain5 = response(A,w,1,1,1,1,t)
        i6,V6,t6,gain6 = response(A,w,0.5,1,1,0.5,t)
        os.remove("source/LC_tank_both.pyc")
        self.assertEqual(round(gain1,3),1)
        self.assertEqual(round(gain2,3),1)
        self.assertEqual(round(gain3,3),1)
        self.assertEqual(round(gain4,3),1)
        self.assertEqual(round(gain5,3),1)
        self.assertEqual(round(gain6,3),1)
    
    
if __name__ == '__main__':
    unittest.main()
           
