def is_equal(a, b):
    return a == b


if __name__ == '__main__':
    import os

    print(os.environ)
    print("hahaha", os.getenv("BES_SECRET"))
