from dataclasses import dataclass

import sympy

from ..utils import batch_isinstance


@dataclass(frozen=True)
class Quantity:
    name: str
    dimension: sympy.Expr

    def __post_init__(self):
        if not self.name.isidentifier():
            raise Exception(f'"{self.name}" is not a valid python identifier')

    def __mul__(self, other):
        if type(self) == type(other):
            return self.dimension * other.dimension
        elif isinstance(other, sympy.Expr):
            return self.dimension * other
        else:
            return NotImplemented

    def __truediv__(self, other):
        if type(self) == type(other):
            return self.dimension / other.dimension
        elif isinstance(other, sympy.Expr):
            return self.dimension / other
        else:
            return NotImplemented

    def __pow__(self, other, modulo=None):
        if modulo is not None:
            return NotImplemented
        elif type(self) == type(other):
            return self.dimension ** other.dimension
        elif batch_isinstance(other, (int, float, sympy.Expr)):
            return self.dimension ** other
        else:
            return NotImplemented

    def __rmul__(self, other):
        if batch_isinstance(other, (int, float, sympy.Expr)):
            return other * self.dimension
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if batch_isinstance(other, (int, float, sympy.Expr)):
            return other / self.dimension
        else:
            return NotImplemented

    def __rpow__(self, other, modulo=None):
        if modulo is not None:
            return NotImplemented
        elif batch_isinstance(other, (int, float, sympy.Expr)):
            return other ** self.dimension
        else:
            return NotImplemented
