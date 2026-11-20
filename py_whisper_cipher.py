def rot_char(c, amt):
    i = 0
    c = ord(c)
    while i < amt:
        c += 1
        if c == ord("z")+1:
            c = ord("a")
        if chr(c) == ord("Z")+1:
            c = ord("A")
        i += 1
    return chr(c)



def whisper_cipher(text: str, shift: int) -> str:
    out = ""

    for c in text:
        if c.isalpha():
            out+=rot_char(c, shift)
        else:
            out+=c

    return out


if __name__ == "__main__":
    a = whisper_cipher("ABC123def", 5)
    print(a)