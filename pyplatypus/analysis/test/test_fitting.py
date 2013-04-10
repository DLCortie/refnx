import unittest
import pyplatypus.analysis.reflect as reflect
import numpy as np
import numpy.testing as npt

class TestDifferentialEvolution(unittest.TestCase):

    def setUp(self):
        pass
                 
    def test_differential_evolutionfit(self):
        '''
            test differential evolution fitting process
        '''
        np.seterr(invalid='raise')
        theoretical = np.loadtxt('pyplatypus/analysis/test/c_PLP0011859_q.txt')

        qvals, rvals, evals, dummy = np.hsplit(theoretical, 4)

        coefs = np.zeros((16))
        coefs[0] = 2
        coefs[1] = 1.
        coefs[2] = 2.07
        coefs[4] = 6.36
        coefs[6] = 2e-6
        coefs[7] = 3
        coefs[8] = 300
        coefs[9] = 3.47
        coefs[11] = 4
        coefs[12] = 250
        coefs[13] = 2
        coefs[15] = 4
        fitted_parameters = np.array([3,5,6,7,8,9,10,11,12,13,14,15])

        a = reflect.ReflectivityFitObject(qvals, rvals, evals, coefs, fitted_parameters = fitted_parameters)
        a.fit()




if __name__ == '__main__':
    unittest.main()