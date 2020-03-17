import sys


def my_range(n):
    for x in range(1, n):
        yield x


def fibonacci():
    current, previous = 1, 0
    while True:
        yield previous
        tmp = current + previous
        previous = current
        current = tmp
        #current, previous = current + previous, current


def odd_numbers():
    x1 = 1
    while True:
        yield x1
        x1 += 2


def pi_val():
    odd = odd_numbers()
    approx = 0
    while True:
        approx += 4/(next(odd))
        yield approx
        approx += -4/(next(odd))
        yield approx


if __name__ == "__main__":
    print("starting values")
    my_list = []
    b_range = my_range(5)
    print(next(b_range))
    print("type {} size: {}".format(type(b_range), sys.getsizeof(b_range)))

    for i in b_range:
        my_list.append(i)

    print("{}".format(my_list))

    fib = fibonacci()
    print("type {} size: {}".format(type(fib), sys.getsizeof(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))
    print("Fibonacci no: {}".format(next(fib)))

    print("First 100 odd no:")



    odd_numbers_val = odd_numbers()
    for i in range(100):
        print(next(odd_numbers_val), end=' ')

    pi_numbers = pi_val()
    print("type {} size: {}".format(type(pi_numbers), sys.getsizeof(pi_numbers)))
    for i in range(100):
        print(next(pi_numbers))








