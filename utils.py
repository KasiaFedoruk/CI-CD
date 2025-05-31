"""
Moduł zawierający podstawowe funkcje matematyczne.

Ten moduł dostarcza funkcje do wykonywania podstawowych operacji arytmetycznych
takich jak dodawanie, odejmowanie, mnożenie i dzielenie.
"""


def add(a: int, b: int) -> int:
    """
    Dodaje dwie liczby całkowite.

    Args:
        a (int): Pierwsza liczba do dodania.
        b (int): Druga liczba do dodania.

    Returns:
        int: Suma dwóch liczb.

    Example:
        >>> add(2, 3)
        5
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Odejmuje drugą liczbę od pierwszej.

    Args:
        a (int): Liczba, od której odejmujemy.
        b (int): Liczba, którą odejmujemy.

    Returns:
        int: Różnica dwóch liczb.

    Example:
        >>> subtract(5, 3)
        2
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Mnoży dwie liczby całkowite.

    Args:
        a (int): Pierwsza liczba do pomnożenia.
        b (int): Druga liczba do pomnożenia.

    Returns:
        int: Iloczyn dwóch liczb.

    Example:
        >>> multiply(4, 3)
        12
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Dzieli pierwszą liczbę przez drugą.

    Args:
        a (int): Dzielna.
        b (int): Dzielnik.

    Returns:
        float: Wynik dzielenia.

    Raises:
        ZeroDivisionError: Gdy dzielnik wynosi zero.

    Example:
        >>> divide(6, 2)
        3.0
    """
    if b == 0:
        raise ZeroDivisionError("Nie można dzielić przez zero")
    return a / b
