class Calculator:
    """A simple calculator class for demonstration."""
    
    def add(self, x: float, y: float) -> float:
        """Add two numbers."""
        return x + y
    
    def subtract(self, x: float, y: float) -> float:
        """Subtract two numbers."""
        return x - y
    
    def multiply(self, x: float, y: float) -> float:
        """Multiply two numbers."""
        return x * y
    
    def divide(self, x: float, y: float) -> float:
        """Divide two numbers."""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y