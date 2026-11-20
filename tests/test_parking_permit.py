from src.parking_permit import is_permit_valid
import pytest

@pytest.mark.parametrize(
    "permit_active, parked_minutes, expected_validity",
    [
        (True, 0, True),       # Active permit, zero minutes [cite: 261]
        (True, 120, True),     # Active permit, exact 120 minute limit [cite: 261]
        (True, 121, False),    # Active permit, exceeds 120 minutes [cite: 261]
        (False, 30, False),    # Inactive permit, valid minutes [cite: 261]
        (False, 150, False),   # Inactive permit, exceeds minutes [cite: 261]
    ],
)
def test_is_permit_valid_scenarios(permit_active, parked_minutes, expected_validity):
    # Act 
    result = is_permit_valid(permit_active, parked_minutes)

    # Assert
    assert result is expected_validity

@pytest.mark.parametrize(
    "permit_active, parked_minutes",
    [
        (True, -1),            # Negative parked minutes [cite: 260, 261]
        (False, -10),          # Out of permitted range [cite: 260, 261]
    ],
)
def test_is_permit_valid_out_of_range_raises_value_error(permit_active, parked_minutes):
    #Act & Assert
    with pytest.raises(ValueError):
        is_permit_valid(permit_active, parked_minutes)

@pytest.mark.parametrize(
    "invalid_permit, invalid_minutes",
    [
        (1, 60),               # Integer instead of bool [cite: 260, 261]
        ("True", 60),          # String instead of bool [cite: 260, 261]
        (True, "60"),          # String instead of int [cite: 260, 261]
        (True, 30.5),          # float instead of int [cite: 260, 261]
    ],
)
def test_is_permit_valid_invalid_type_raises_type_error(invalid_permit, invalid_minutes):
    # Act & Assert
    with pytest.raises(TypeError):
        is_permit_valid(invalid_permit, invalid_minutes)