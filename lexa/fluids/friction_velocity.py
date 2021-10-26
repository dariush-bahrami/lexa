import sympy as sp

from ..equation import Equation


class FrictionVelocityEquation(Equation):
    def __init__(self):
        parameters = [
            "friction_velocity",
            "wall_shear_stress",
            "density",
        ]
        syms = self.register_symbols(parameters, real=True)
        lhs = syms.friction_velocity
        rhs = sp.sqrt(syms.wall_shear_stress / syms.density)
        self.register_equation(lhs, rhs)
