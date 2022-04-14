"""A Module containing definition of field element class"""

class FieldElement:
    """
    A class used to represent field element

    ...
    Attributes
    ___________
    number: int 
        a number in the set of field element
    prime: int 
        a prime number that represent field

    """
    def __init__(self, number: int, prime: int):
        """Create a new instance of FieldElement"""
        if number >= prime or number < 0:
            raise ValueError(f"Number {number} is not in field range from 0 to {prime-1}")
        self.number = number
        self.prime = prime

    def __repr__(self):
        return f"FieldElement({self.number}, {self.prime})"

    def __eq__(self, other): 
        if other is None:
            return False
        return self.number == other.number and self.prime == other.prime

    def __add__(self, other):
        if self.prime != other.prime: 
            raise TypeError("Cannot Add two numbers in different Fields")
        number = (other.number + self.number) % self.prime
        return self.__class__(number, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime: 
            raise TypeError("Cannot Subtract two numbers in different Fields")
        number = (self.number - other.number) % self.prime
        return self.__class__(number, self.prime)
    def __mul__(self, other):
        if self.prime != other.prime: 
            raise TypeError("Cannot Multiply two numbers in different Fields")
        number = (self.number * other.number) % self.prime
        return self.__class__(number, self.prime)

    def __pow__(self, exponent):
        n = exponent
        if n < 0:
            n += self.prime - 1
        number = pow(self.number, n, self.prime)
        return self.__class__(number, self.prime)

    def __div__(self, other):
        # Fermat Little Theorem required
        pass

    def __truediv__(self, other):
        pass
    
