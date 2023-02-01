# python_exercises

### Python Exercises Homework of Miuul Data Science & Machine Learning Bootcamp

## One Of The Examples:

```python
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.

# TASK 5: Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists and returns these lists.
###############################################

l = [2, 13, 18, 93, 22]


def odds_evens(numbers: list[int]) -> (list[int], list[int]):
    """Takes in a list of numbers and returns two lists => odds, evens

    Args:
        numbers: list of int numbers

    Returns:
        odds: list of odd numbers
        evens: list of even numbers

    """
    odds = [number for number in numbers if number % 2 != 0]
    evens = [number for number in numbers if number % 2 == 0]
    return odds, evens


odds_evens(l)
```

