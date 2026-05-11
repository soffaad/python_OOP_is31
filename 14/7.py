def print_info(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

data = {"name": "Bob", "age": "25"}
print_info(**data)