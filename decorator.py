import time


def duration_time(function):
    def wrapper():
        init = time.time()
        function()
        final = time.time()
        print(f"Tempo total da função {function.__name__} foi de {final - init}")
    return wrapper()


@duration_time
def main():
    for i in range(1, 1000000):
        pass


main
