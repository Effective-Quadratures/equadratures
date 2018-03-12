# Sample test utility!
from unittest import TestCase
import unittest
from equadratures import *
import numpy as np
import os


class TestDR(TestCase):

    def test_dimension_reduction(self):
        X = np.random.rand(520,25)*2 - 1.
        A = np.random.rand(25,2)
        Q, R = np.linalg.qr(A)
        A[:] = Q[:,0:2]
        y = np.dot(X , A)
        fX = 0.02 * y[:,1]**2 + 1.5 * y[:,0]**2 + 50*y[:,1]*y[:,0] -3.5 # A quadratic model!
        m, n = X.shape
        fX = np.reshape(fX, (m,1))
        parameters = []
        totalorders = []
        dimensions = n
        maxorder = 2
        for i in range(0, n):
            parameter = Parameter(param_type='Uniform', lower=-1., upper=1., order=maxorder)
            parameters.append(parameter)
            totalorders.append(maxorder)
        basis = Basis('Total order')
        PolyObject = Polyreg(training_inputs=X, training_outputs=fX, parameters=parameters, basis=basis)

        # Eigenvalue plot!
        e, W = computeActiveSubspaces(PolyObject)
        semilogy_lineplot(np.arange(0, 25), np.abs(e), 'Parameters', 'Eigenvalues')


        # Sufficient summary plot!
        active1 = np.dot( X , W[:,0:1] )
        scatterplot(active1, fX, x_label='w1', y_label='Output')


if __name__ == '__main__':
    unittest.main()
