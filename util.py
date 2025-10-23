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


def nor(n):
    nor_dict = {
        "1s": "naiz",
        "2s": "zara",
        "3s": "da",
        "1p": "gara",
        "2p": "zarete",
        "3p": "dira",
    }

    return nor_dict[n]


def nor_nork(nor, nork):
    nor_dict = {
        "1s": "nau",
        "2s": "zaitu",
        "3s": "du",
        "1p": "gaitu",
        "2p": "zaituzte",
        "3p": "ditu",
    }

    nork_dict = {
        "1s": "t",
        "2s": "zu",
        "3s": "",
        "1p": "gu",
        "2p": "zue",
        "3p": "te",  # (z) te
    }

    ans = nor_dict[nor] + nork_dict[nork]

    ans = ans.replace("tute", "tuzte")

    return ans


def nor_nori(nor, nori):
    nor_dict = {
        "1s": "natzai",
        "2s": "zatzaizki",
        "3s": "zai",
        "1p": "gatzaizki",
        "2p": "zatzaizki",  # *te at the end
        "3p": "zaizki",
    }

    nori_dict = {
        "1s": "t",
        "2s": "zu",
        "3s": "o",
        "1p": "gu",
        "2p": "zue",  # *te at the end
        "3p": "e",
    }

    ans = nor_dict[nor] + nori_dict[nori]

    if nor == "2p":
        ans += "te"

    return ans


def nor_nori_nork(nor, nori, nork):
    nor_dict = {
        "3s": "di",
        "3p": "dizki",
    }

    nori_dict = {
        "1s": "da",  # t if at the end
        "2s": "zu",
        "3s": "o",
        "1p": "gu",
        "2p": "zue",
        "3p": "e",
    }

    nork_dict = {
        "1s": "t",
        "2s": "zu",
        "3s": "",
        "1p": "gu",
        "2p": "zue",
        "3p": "te",
    }

    if nori == "1s" and nork == "3s":
        ans = nor_dict[nor] + "t"
    else:
        ans = nor_dict[nor] + nori_dict[nori] + nork_dict[nork]

    return ans
