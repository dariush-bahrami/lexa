from collections import namedtuple

import sympy as sp


class Equation(object):
    def register_symbols(self, parameters, **kwargs):
        self.__parameters = parameters
        Symbols = namedtuple("Symbols", parameters)
        symbols = Symbols(*sp.symbols(parameters, **kwargs))
        self.__symbols = symbols
        return symbols

    @property
    def symbols(self):
        return self.__symbols

    @property
    def parameters(self):
        return self.__parameters

    def register_equation(self, lhs, rhs):
        equation = sp.Eq(lhs, rhs)
        self.__equation = equation
        return equation

    def __str__(self):
        return f"Equation:\t{self.equation}\nParameters:\t{self.parameters}"

    def __repr__(self):
        return str(self)

    @property
    def equation(self):
        return self.__equation

    def solve_for(self, parameter):
        """Solve equation for specified parameter.

        Args:
            parameter (str): Independent variable of equation. To get list of valid
                parameters see "parameters" attribute

        Returns:
            list: List of all solutions.

        Raises:
            Exception: If parameter is unknown.

        """
        syms = self.symbols
        if parameter not in self.__parameters:
            raise Exception(f"Unknown parameter: {parameter}.")
        solutions = sp.solve(self.equation, getattr(syms, parameter))
        return solutions

    def lambdify_for(self, parameter):
        """Solve equation for specified parameter and lambdify solution.

        Args:
            parameter (str): Independent variable of equation. To get list of valid
                parameters see "parameters" attribute

        Returns:
            function: The function to evaluate parameter based on other variables.

        Raises:
            Exception: If there is no available solution for specified "parameter".
            Exception: If there is more than one solution for specified "parameter".

        """
        solutions = self.solve_for(parameter)
        if len(solutions) != 1:
            if len(solutions) == 0:
                raise Exception(f"There is no available solution for {parameter}")
            elif len(solutions) > 1:
                raise Exception(f"There is more than one solution for {parameter}")
        else:
            syms = self.symbols
            solution = solutions[0]
            args_set = self.equation.free_symbols - {getattr(syms, parameter)}
            args = sorted(list(args_set), key=str)
            function = sp.lambdify(args, solution)
            return function
