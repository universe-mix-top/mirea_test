import sys


def main():
    n = int(input())
    synonyms = []
    for _ in range(n):
        synonyms.append(set(input().split(' ')))
    word = input()

    synonym = filter(lambda x: word in x, synonyms).__next__()
    synonym.remove(word)
    print(synonym.pop())


if __name__ == '__main__':
    main()
