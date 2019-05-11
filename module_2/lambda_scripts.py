scientists = ["Marie", "Albert", "Niels", "Isaac", "Charles", "Antoine"]


if __name__ == "__main__":
    # Sorts by last letter in the name
    print(sorted(scientists, key=lambda name: name[-1]))