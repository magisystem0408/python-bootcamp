def d(f):
    def w():
        print('ここにくるやつが前処理として行われる')
        return f()
    return w

@d
def example():
    print("example")


example()
