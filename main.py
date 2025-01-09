from src.calculator import Calculator
from src.utils import log_result
import config

def main():
    """Main application entry point."""
    calculator = Calculator()
    
    # Example operations
    result1 = calculator.add(10, 20)
    log_result("Addition", result1)
    
    result2 = calculator.multiply(5, 6)
    log_result("Multiplication", result2)

if __name__ == "__main__":
    main()