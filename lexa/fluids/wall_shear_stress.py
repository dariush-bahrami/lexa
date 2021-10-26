import sympy as sp

from ..equation import Equation


class WallShearStressEquation(Equation):
    def __init__(self):
        parameters = [
            "wall_shear_stress",
            "skin_friction_coefficient",
            "density",
            "velocity",
        ]
        syms = self.register_symbols(parameters, real=True)
        lhs = syms.wall_shear_stress
        rhs = (
            sp.Rational(1, 2)
            * syms.skin_friction_coefficient
            * syms.density
            * syms.velocity
        )
        self.register_equation(lhs, rhs)
