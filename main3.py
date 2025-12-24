from random import choice

from cligame import Game

from german_verbs import (verbos_nor, verbos_nor_nori, verbos_nor_nori_nork,
                          verbos_nor_nork)
from pronouns import de_pronouns, de_pronouns_akk, de_pronouns_dat, pronouns
from util import check_non_self_ref, nor_, nor_nori, nor_nori_nork, nor_nork


def get_2_args():
    while True:
        args = choice(pronouns), choice(pronouns)
        try:
            check_non_self_ref(*args)
            return args
        except ValueError:
            pass


def nor_question():
    arg = choice(pronouns)
    correct = nor_(arg)

    print("nor")
    verb = "gehen"
    print(f"{de_pronouns[arg]} {verbos_nor[verb][arg]}")
    given = input("joan ".rjust(17))
    return given, correct


def nor_nork_question():
    n, nk = get_2_args()
    correct = nor_nork(n, nk)

    print("nor nork")
    verb = "sehen"
    print(f"{de_pronouns[nk]} {verbos_nor_nork[verb][nk]} {de_pronouns_akk[n]}")
    given = input("ikusi ".rjust(17))
    return given, correct


def nor_nori_question():
    n, ni = get_2_args()
    correct = nor_nori(n, ni)

    print("nor nori")
    verb = "gehen zu"
    print(f"{de_pronouns[n]} {verbos_nor_nori[verb][n]} {de_pronouns_dat[ni]}")

    given = input("joan ".rjust(17))
    return given, correct


def nor_nori_nork_question():
    n = choice(["3s", "3p"])
    ni, nk = get_2_args()

    print("nor nori nork")
    verb = "geben"
    nor_text = "das Buch" if n == "3s" else "die Bücher"
    print(
        f"{de_pronouns[nk]} {verbos_nor_nori_nork[verb][nk]} {de_pronouns_dat[ni]} {nor_text}"
    )

    correct = nor_nori_nork(n, ni, nk)
    given = input("eman ".rjust(17))
    return given, correct


funcs = {
    "nor": nor_question,
    "nor_nork": nor_nork_question,
    "nor_nori": nor_nori_question,
    "nor_nori_nork": nor_nori_nork_question,
}


def question(_):
    # choices = ["nor", "nor_nork", "nor_nori", "nor_nori_nork"]
    choices = ["nor_nori_nork"]

    given, ans = funcs[choice(choices)]()

    correct = "".join(ans).replace(" ", "").replace("_", "")

    return given == correct, f"{correct}: " + " - ".join(ans)


if __name__ == "__main__":
    mygame = Game(question)
    mygame.start()

    mygame.save_raw("stats.json")
