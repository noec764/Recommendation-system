# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    f = open("books-rating.dat", "a")
    movieSet = set()
    mu = 15
    sigma = 5
    for i in range(1, 31):  # pour chaque utilisateur
        for j in range(1, int(abs(random.gauss(mu, sigma)))):  # on génère entre 15 et 25 notes
            idMOvie = random.randint(1, 30)
            while idMOvie in movieSet:
                idMOvie = random.randint(1, 30)
            movieSet.add(idMOvie)
            f.write(str(i) + "::" + str(idMOvie) + "::" + str(random.randint(1, 5)) + "::978300719\n")
        movieSet.clear()
    f.close()
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
