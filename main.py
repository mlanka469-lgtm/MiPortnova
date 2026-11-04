def analyze_numbers(numbers):
    """Анализирует список чисел."""
    if not numbers:
        return None

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
    }


def main():
    numbers = [12, 7, 19, 4, 8]
    result = analyze_numbers(numbers)
    print(result)


if __name__ == "__main__":
    main()
