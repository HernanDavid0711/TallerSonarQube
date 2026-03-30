import pytest

from main import calculate_discount, process_user_data, save_to_file


def test_calculate_discount_senior():
    assert calculate_discount(100, 65) == 50.0


def test_calculate_discount_adult():
    assert calculate_discount(100, 30) == 10.0


def test_calculate_discount_minor():
    assert calculate_discount(100, 15) == 0.0


def test_calculate_discount_negative_price():
    assert calculate_discount(-100, 25) == 0.0


def test_process_user_data_returns_parameterized_query():
    result = process_user_data("105")
    assert result["query"] == "SELECT * FROM users WHERE id = %s"
    assert result["params"] == (105,)


def test_process_user_data_rejects_invalid_value():
    with pytest.raises(ValueError):
        process_user_data("abc")


def test_save_to_file(tmp_path):
    file_path = tmp_path / "log.txt"
    saved_path = save_to_file("hola", str(file_path))
    assert saved_path.exists()
    assert saved_path.read_text(encoding="utf-8") == "hola"
