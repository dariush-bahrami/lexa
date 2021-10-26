import sympy as sp

from ..equation import Equation


class ReynoldsNumberEquation(Equation):
    def __init__(self):
        parameters = [
            "reynolds",
            "density",
            "velocity",
            "length",
            "viscosity",
        ]
        syms = self.register_symbols(parameters, real=True)
        lhs = syms.reynolds
        rhs = (syms.density * syms.velocity * syms.length) / syms.viscosity
        self.register_equation(lhs, rhs)
