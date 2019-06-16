def foo():
    print("ccc")

if __name__ == '__main__':
    print("I'm module2, I'm excuting myself")
else:
    print("I'm module2, I've been called",__name__, __package__)