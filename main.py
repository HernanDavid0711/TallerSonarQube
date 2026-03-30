from pathlib import Path
from typing import Tuple


def build_user_query(user_id: int) -> Tuple[str, tuple[int]]:
    """Build a parameterized query safely."""
    if user_id <= 0:
        raise ValueError("El id del usuario debe ser positivo")
    return "SELECT * FROM users WHERE id = %s", (user_id,)


def process_user_data(user_input_id: str) -> dict[str, object]:
    """Validate the input and simulate a safe query build."""
    try:
        user_id = int(user_input_id)
    except ValueError as exc:
        raise ValueError("El id del usuario debe ser un numero entero") from exc

    query, params = build_user_query(user_id)
    return {"query": query, "params": params}


def calculate_discount(price: float, age: int) -> float:
    """Calculate discount according to the customer's age."""
    if price <= 0 or age <= 18:
        return 0.0
    if age > 60:
        return price * 0.5
    return price * 0.1


def save_to_file(data: str, file_path: str = "log.txt") -> Path:
    """Append text to a file and return the path used."""
    if not isinstance(data, str):
        raise TypeError("data debe ser una cadena de texto")

    path = Path(file_path)
    with path.open("a", encoding="utf-8") as file:
        file.write(data)
    return path


if __name__ == "__main__":
    result = process_user_data("101")
    print(result)
