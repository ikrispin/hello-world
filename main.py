def hello(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main():
    print(hello())
    print(hello("Developer"))


if __name__ == "__main__":
    main()
