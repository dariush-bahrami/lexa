import sympy as sp

from ..equation import Equation


class YPlusEquation(Equation):
    def __init__(self):
        params = [
            "y_plus",
            "y",
            "friction_velocity",
            "density",
            "viscosity",
        ]
        syms = self.register_symbols(params, real=True)
        lhs = syms.y_plus
        rhs = (syms.y * syms.friction_velocity * syms.density) / syms.viscosity
        self.register_equation(lhs, rhs)
