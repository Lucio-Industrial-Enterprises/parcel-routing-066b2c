"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return the integer quantity represented by *value*.

    Raises
    ------
    ValueError
        If *value* does not represent a positive integer (zero and negatives
        are not valid pick-list quantities).
    """
    qty = int(value.strip())
    if qty <= 0:
        raise ValueError(f"quantity must be a positive integer, got {qty!r}")
    return qty
