def echo_string_prep(s):
    out = ""
    for c in s:
        if c.isalpha():
            out += c

    return out.lower()


def echo_validator(text: str) -> bool:
    text = echo_string_prep(text)
    i = 0
    while i < len(text)/2:
        print(f"{text[i]} and {text[len(text) - 1 - i]}")
        if text[i] != text[len(text) - 1 - i]:
            return False
        i += 1
    return True


def main():
    a = echo_validator("A man a plan a canal Panama")
    print(a)


if __name__ == "__main__":
    main()
