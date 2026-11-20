import sys

class wordClass():
    def __init__(self, s):
        self.s = s
        self.weight = word_get_weight(s)

    def show(self):
        print(f"{self.s}: \t \t \t {self.weight}")

def cryptic_sorter(strings: list[str]) -> list[str]:
    words = []
    for word in strings:
        words.append(wordClass(word))
    words.sort(key=lambda w: w.weight)
    for w in words:
        w.show()

    return []


def c_is_wovel(c):
    match c:
        case "a": return True
        case "e": return True
        case "i": return True
        case "o": return True
        case "u": return True
    return False

def word_get_weight(s):
    w = 0
    w += len(s)*1000000000000

    miniw = 10000
    for c in s:
        c = c.lower()
        w += miniw*ord(c)
        miniw-=1000

    for c in s:
        w += 100 * c_is_wovel(c)
    return w


def main():
    a = cryptic_sorter(["hello", "world", "hi", "test"])
    print(a)


if __name__ == "__main__":
    main()
