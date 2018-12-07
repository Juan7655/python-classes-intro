def run():
    for l in generate_data():
        l.map(lambda x: int(x))


def generate_data():
    for n in range(100, 1000000, 100):
        yield list(range(n))


if __name__ == "__main__":
    run()
