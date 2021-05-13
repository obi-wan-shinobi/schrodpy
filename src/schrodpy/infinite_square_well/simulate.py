from space import subSpace
from solver import Solver
from plotter import Plotter

from astropy import units as u

def _main():

    pipe = subSpace(0, 10)

    solver = Solver(space = pipe)
    plotter = Plotter(space = pipe)

    eps = []
    eps.append(solver.eigen_state(eps=-1, deps=0.02))

    for i in range(10):
        eps.append(solver.eigen_state(eps=eps[i], deps=0.02))
        print(f'Epsilon {i} = {eps[i]}')

    plotter.plot(solver, eps = eps)

    plotter.show()


if __name__ == '__main__':
    _main()
