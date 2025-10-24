def check_non_self_ref(n1, n2):
    if (n1[0] == n2[0] == "1") or (n1[0] == n2[0] == "2"):
        raise ValueError(f"invalid parameter combination: {n1}-{n2}")


def nor_(n):
    nor_dict = {
        "1s": "naiz",
        "2s": "zara",
        "3s": "da",
        "1p": "gara",
        "2p": "zarete",
        "3p": "dira",
    }

    return [nor_dict[n]]


def nor_nork(n, nk):
    check_non_self_ref(n, nk)

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

    nor = nor_dict[n]
    nork = nork_dict[nk]

    if nk == "3p" and nor.endswith("tu"):
        nork = "zte"

    return [nor, nork]


def nor_nori(n, ni):
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

    nor = nor_dict[n]
    nori = nori_dict[ni]

    ans = [nor, nori]

    if n == "2p":
        ans.append("_te")

    return ans


def nor_nori_nork(n, ni, nk):
    check_non_self_ref(ni, nk)

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

    if ni == "1s" and nk == "3s":
        nori = "t"
    else:
        nori = nori_dict[ni]

    ans = [nor_dict[n], nori, nork_dict[nk]]

    return ans
