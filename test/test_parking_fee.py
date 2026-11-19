from src.parking_fee import calculate_parking_fee
import pytest

@pytest.mark.parametrize(
    "minutes, expected_fee",
    [
        (0, 0),      # Zero minutes cost zero
        (1, 200),    # Started hour 1 [cite: 261]
        (60, 200),   # Exact hour boundary [cite: 261]
        (61, 400),   # Started hour 2 [cite: 261]
        (120, 400),  # Exact two hours boundary [cite: 261]
    ],
)
def test_calculate_parking_fee_valid(minutes, expected_fee):
    # Act
    result = calculate_parking_fee(minutes)

    # Assert
    assert result == expected_fee

@pytest.mark.parametrize(
    "invalid_minutes",
    [
        -1,          # Negative minutes [cite: 261]
        -60,         # Out of permitted range[cite: 261]
    ],
)
def test_calculate_parking_fee_out_of_range_raises_value_error(invalid_minutes):
    # Act & Assert
    with pytest.raises(ValueError):
        calculate_parking_fee(invalid_minutes)

@pytest.mark.parametrize(
    "invalid_type_input",
    [
        "60",        # String instead of int [cite: 260, 261] 
        30.5,        # Float instead of int [cite: 260, 261]
        True,        # Boolean is not a valid integer [cite: 260, 261]
        None,        # NoneType [cite: 260, 261]
    ],
)
def test_calculate_parking_fee_invalid_type_raises_type_error(invalid_type_input):
    # Act & Assert
    with pytest.raises(TypeError):
        calculate_parking_fee(invalid_type_input)
