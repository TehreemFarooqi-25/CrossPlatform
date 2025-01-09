import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_result(operation: str, result: float) -> None:
    """Log the result of an operation."""
    logging.info(f"{operation} result: {result}")
    
def get_timestamp() -> str:
    """Return current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")