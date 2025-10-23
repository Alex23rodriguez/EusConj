from random import choice

from util import nor, nor_nori, nor_nori_nork, nor_nork

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
    "2s": "hark",
    "3s": "guk",
    "1p": "zuk",
    "2p": "zuek",
    "3p": "haiek",
}


pronouns = ["1s", "2s", "3s", "1p", "2p", "3p"]

forbidden = [
    ("1s", "1s"),
    ("1s", "1p"),
    ("1p", "1s"),
    ("1p", "1p"),
    ("2s", "2s"),
    ("2s", "2p"),
    ("2p", "2s"),
    ("2p", "2p"),
]


def get_2_args():
    while True:
        args = choice(pronouns), choice(pronouns)
        if args not in forbidden:
            return args


VERB = "esan"


def nor_question():
    arg = choice(pronouns)
    correct = nor(arg)
    given = input(f"{pronouns_nor[arg]} {VERB} ")
    return correct == given, correct


def nor_nork_question():
    n, nk = get_2_args()
    correct = nor_nork(n, nk)
    given = input(f"{pronouns_nork[nk]} {pronouns_nor[n]} {VERB} ")
    return correct == given, correct


def nor_nori_question():
    n, ni = get_2_args()
    correct = nor_nori(n, ni)
    given = input(f"{pronouns_nor[n]} {pronouns_nori[ni]} {VERB} ")
    return correct == given, correct


def nor_nori_nork_question():
    n = choice(["3s", "3p"])
    ni, nk = get_2_args()
    correct = nor_nori_nork(n, ni, nk)
    given = input(f"{pronouns_nork[nk]} {pronouns_nor[n]} {pronouns_nori[ni]} {VERB} ")
    return correct == given, correct


funcs = {
    "nor": nor_question,
    "nor_nork": nor_nork_question,
    "nor_nori": nor_nori_question,
    "nor_nori_nork": nor_nori_nork_question,
}


def question(_):
    choices = ["nor", "nor_nork", "nor_nori", "nor_nori_nork"]

    return funcs[choice(choices)]
