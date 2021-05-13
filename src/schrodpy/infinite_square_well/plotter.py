import numpy as np
from astropy import constants, units as u
from matplotlib import pyplot as plt
from solver import Solver

class Plotter():
    def __init__(self, space):
        self.space = space


    def plot(self, solver, eps = None):

        fig = plt.figure()
        ax = plt.axes()

        ax.set_xlabel(r'$\tilde x$')
        ax.set_ylabel(r'$\psi(\tilde x)$')
        ax.grid()
        ax.axhline(y=0,color = 'black')

        if(eps is None):
            eps = solver.ep

        x = np.linspace(0,1000,1000)

        if(isinstance(eps, list)):
            for energy in eps:
                y = solver.wave_function(ep = energy)
                ax.plot(x,y)
        else:
            y = solver.wave_function(ep = eps)
            ax.plot(x,y)


    def show(self):
        plt.show()
