def check_non_self_ref(n1, n2):
    if (n1[0] == n2[0] == "1") or (n1[0] == n2[0] == "2"):
        raise ValueError(f"invalid parameter combination: {n1}-{n2}")


def nor_(n):
    nor_dict = {
        "1s": "naiz",
        "2S": "haiz",
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
        "1s": "n a __ u",
        "2S": "h a __ u",
        "3s": "d _ __ u",
        "1p": "g a it u",
        "2s": "z a it u",
        "2p": "z a it u zte",
        "3p": "d _ it u",
    }

    nork_dict = {
        "1s": "t",
        "2S": "k/n",
        "3s": "_",
        "1p": "gu",
        "2s": "zu",
        "2p": "zue",
        "3p": "te",  # (z) te
    }

    nor = nor_dict[n]
    nork = nork_dict[nk]

    if nk == "3p" and nor.replace(" ", "").endswith("tu"):
        nork = "zte"

    return [nor, nork]


def nor_nori(n, ni):
    nor_dict = {
        "1s": "na tzai ___",
        "2S": "ha tzai ___",
        "3s": "__ _zai ___",
        "1p": "ga tzai zki",
        "2s": "za tzai zki",
        "2p": "za tzai zki",  # *te at the end
        "3p": "__ _zai zki",
    }

    nori_dict = {
        "1s": "t",
        "2S": "k/n",
        "3s": "o",
        "1p": "gu",
        "2s": "zu",
        "2p": "zue",  # *te at the end
        "3p": "e",
    }

    nor = nor_dict[n]
    nori = nori_dict[ni]

    ans = [nor, nori]

    if n == "2p":
        ans.append("te")

    return ans


def nor_nori_nork(n, ni, nk):
    check_non_self_ref(ni, nk)

    nor_dict = {
        "3s": "d i ___",
        "3p": "d i zki",
    }

    nori_dict = {
        "1s": "da",  # t if at the end
        "2S": "k/t",
        "3s": "o",
        "1p": "gu",
        "2s": "zu",
        "2p": "zue",
        "3p": "e",
    }

    nork_dict = {
        "1s": "t",
        "2S": "k/t",
        "3s": "_",
        "1p": "gu",
        "2s": "zu",
        "2p": "zue",
        "3p": "te",
    }

    if ni == "1s" and nk == "3s":
        nori = "t"
    else:
        nori = nori_dict[ni]

    ans = [nor_dict[n], nori, nork_dict[nk]]

    return ans
