MIN: int = 5

def validation(num: int) -> bool:
    return num >= MIN

def input_num(char_type: str) -> int:
    prompt: str = f"\n Enter the amount of {char_type} you want in your password: "
    trials = 3
    for _ in range(trials):
        res: str = input(prompt)
        try:
            num: int = int(res)
            if validation(num):
                return num
            else:
                print(f"Expected input that is greater than {MIN} got {num}")
        except ValueError:
            print(f"{num} is not a valid input please try again!.")
            continue

    # raise ValueError(f"User entered an invalid integrt {trials} times.")
    print(f"\nUser entered an invalid integer {trials} times.")
    exit()

if __name__ == "__main__":
    value: bool = input_num("symbols")
    print(value)