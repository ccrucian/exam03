def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    while True:
        curr_char = s1[0]
        if curr_char in s2:
            s1 = s1.replace(curr_char, "", 1)
            s2 = s2.replace(curr_char, "", 1)
        else:
            return False
        if s1 == "":
            return True


if __name__ == "__main__":
    a = string_permutation_checker("abc", "cab")
    print(a)