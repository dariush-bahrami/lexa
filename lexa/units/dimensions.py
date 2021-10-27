from dataclasses import dataclass

import sympy

from ..utils import batch_isinstance


@dataclass(frozen=True)
class Dimension:
    name: str
    symbol: sympy.Symbol

    def __post_init__(self):
        if not self.name.isidentifier():
            raise Exception(f'"{self.name}" is not a valid python identifier')

    def __mul__(self, other):
        if type(self) == type(other):
            return self.symbol * other.symbol
        elif isinstance(other, sympy.Expr):
            return self.symbol * other
        else:
            return NotImplemented

    def __truediv__(self, other):
        if type(self) == type(other):
            return self.symbol / other.symbol
        elif isinstance(other, sympy.Expr):
            return self.symbol / other
        else:
            return NotImplemented

    def __pow__(self, other, modulo=None):
        if modulo is not None:
            return NotImplemented
        elif type(self) == type(other):
            return self.symbol ** other.symbol
        elif batch_isinstance(other, (int, float, sympy.Expr)):
            return self.symbol ** other
        else:
            return NotImplemented

    def __rmul__(self, other):
        if batch_isinstance(other, (int, float, sympy.Expr)):
            return other * self.symbol
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if batch_isinstance(other, (int, float, sympy.Expr)):
            return other / self.symbol
        else:
            return NotImplemented

    def __rpow__(self, other, modulo=None):
        if modulo is not None:
            return NotImplemented
        elif batch_isinstance(other, (int, float, sympy.Expr)):
            return other ** self.symbol
        else:
            return NotImplemented


@dataclass(frozen=True)
class BaseDimensions:
    length: Dimension
    mass: Dimension
    time: Dimension
    current: Dimension
    temperature: Dimension
    amount: Dimension
    luminous_intensity: Dimension


base_dimensions = BaseDimensions(
    Dimension("length", sympy.Symbol("L")),
    Dimension("mass", sympy.Symbol("M")),
    Dimension("time", sympy.Symbol("T")),
    Dimension("current", sympy.Symbol("I")),
    Dimension("temperature", sympy.Symbol("Θ")),
    Dimension("amount", sympy.Symbol("N")),
    Dimension("luminous_intensity", sympy.Symbol("J")),
)
