import numpy as np
from astropy import constants, units as u

class Solver:
    def __init__(self, space, steps = 1000, g2 = 200, ep = -0.9):
        self.space = space
        self.N = steps
        self.g2 = g2
        self.v = -1*np.ones(steps)
        self.ep = ep
        self.k2 = g2*(ep-self.v)
        self.l2 = (1/(steps-1))**2

    def __str__(self):
        return f"Solver for: (Space = {self.space})"

    def eigen_state(self, eps, deps):
        k2 = self.g2*(eps-self.v)
        Psi = self.wave_function(k2=k2)
        P1 = Psi[-1]
        eps = eps + deps

        while(abs(deps)>1e-12):
            k2 = self.g2*(eps-self.v)
            Psi = self.wave_function(Psi=Psi, k2=k2)
            P2 = Psi[-1]

            if(P1*P2 < 0):
                deps = -deps/2.0

            eps = eps + deps
            P1 = P2
            
        return eps

    def wave_function(self,ep=None,Psi=None,k2=None):
        if(ep is None):
            ep = self.ep
            if(k2 is None):
                k2 = self.k2
        else:
            k2 = self.g2*(ep-self.v)
        if(Psi is None):
            Psi = np.zeros(self.N)

        Psi[0] = 0
        Psi[1] = 1e-4

        for i in range(2,self.N):
            Psi[i] = (2*(1-(5.0/12)*self.l2*k2[i-1])*Psi[i-1]
                    -(1+(1.0/12)*self.l2*k2[i-2])*Psi[i-2])/(1+(1.0/12)*self.l2*k2[i])

        return Psi
