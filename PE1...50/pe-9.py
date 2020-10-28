def find_specital_pythagorean():
    max = 10000
    for c in range(1, max):
        for b in range(1, c):
            for a in range(1, b):
                if(a**2 + b ** 2 == c ** 2 and a + b + c == 1000):
                    print(a * b * c)
                    return


find_specital_pythagorean()
