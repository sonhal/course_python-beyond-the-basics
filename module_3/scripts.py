
def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)


if __name__ == "__main__":
    print(sort_by_last_letter(("asdas", "asdasda"))) # ['asdasda', 'asdas']
