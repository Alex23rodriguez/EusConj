from random import choice

from cligame import Game

from util import check_non_self_ref, nor_, nor_nori, nor_nori_nork, nor_nork

pronouns_nor = {
    "1s": "ni",
    "2s": "zu",
    "3s": "hura",
    "1p": "gu",
    "2p": "zuek",
    "3p": "haiek",
}

pronouns_nori = {
    "1s": "niri",
    "2s": "zuri",
    "3s": "hari",
    "1p": "guri",
    "2p": "zuei",
    "3p": "haiei",
}

pronouns_nork = {
    "1s": "nik",
    "2s": "zuk",
    "3s": "hark",
    "1p": "guk",
    "2p": "zuek",
    "3p": "haiek",
}


pronouns = ["1s", "2s", "3s", "1p", "2p", "3p"]


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
    print(pronouns_nor[arg])
    given = input("".ljust(17))
    return given, correct


def nor_nork_question():
    n, nk = get_2_args()
    correct = nor_nork(n, nk)
    print("nork nor")
    print(pronouns_nork[nk], pronouns_nor[n])
    given = input("".ljust(17))
    return given, correct


def nor_nori_question():
    n, ni = get_2_args()
    print("nor nori")
    correct = nor_nori(n, ni)
    print(pronouns_nor[n], pronouns_nori[ni])
    given = input("".ljust(17))
    return given, correct


def nor_nori_nork_question():
    n = choice(["3s", "3p"])
    ni, nk = get_2_args()
    print("nork nor nori")
    correct = nor_nori_nork(n, ni, nk)
    print(pronouns_nork[nk], pronouns_nor[n], pronouns_nori[ni])
    given = input("".ljust(17))
    return given, correct


funcs = {
    "nor": nor_question,
    "nor_nork": nor_nork_question,
    "nor_nori": nor_nori_question,
    "nor_nori_nork": nor_nori_nork_question,
}


def question(_):
    choices = ["nor", "nor_nork", "nor_nori", "nor_nori_nork"]

    given, ans = funcs[choice(choices)]()

    correct = "".join(ans).replace(" ", "").replace("_", "")

    return given == correct, f"{correct}: " + " - ".join(ans)


if __name__ == "__main__":
    mygame = Game(question)
    mygame.start()

    mygame.save_raw("stats.json")
