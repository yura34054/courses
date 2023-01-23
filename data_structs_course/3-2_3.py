def get_hash(s):
    return sum([ord(s[i]) for i in range(len(s))])

def recount_hash(h, c1, c2):
    return h - ord(c1) + ord(c2)


def main():    
    pattern = input()
    text = input()

    pattern_hash = get_hash(pattern)
    current_hash = get_hash(text[:len(pattern)])

    for i in range(len(text)-len(pattern)):
        if pattern_hash == current_hash and text[i:i+len(pattern)] == pattern:
            print(i, end=' ')

        current_hash = recount_hash(current_hash, text[i], text[i+len(pattern)])

    if pattern_hash == current_hash and text[len(text)-len(pattern):] == pattern:
        print(len(text)-len(pattern))


if __name__ == '__main__': main()