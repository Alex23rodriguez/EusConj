from random import choice

from ezquiz import APIGame, Q

from conj import conj_past, conj_present
from pronouns import (
    nor_nori_prononuns_sp,
    pronouns,
    sp_direct_obj_pronouns,
    sp_indirect_obj_pronouns,
    sp_pronouns,
)
from spanish_verbs import (
    verbos_nor,
    verbos_nor_nori,
    verbos_nor_nori_nork,
    verbos_nor_nork,
)
from util import check_non_self_ref, nor_, nor_nori, nor_nori_nork, nor_nork


def get_2_args():
    while True:
        args = choice(pronouns), choice(pronouns)
        try:
            check_non_self_ref(*args)
            return args
        except ValueError:
            pass


def nor_seed():
    return choice(pronouns)


def ask_nor(p: str):
    return {
        "type": "fill",
        "context": f"{sp_pronouns[p]} {verbos_nor['ir'][p]}",
        "text": "joan [...]",
    }


def correct_nor(p: str):
    return "".join(nor_(p)).replace(" ", "").replace("_", "")


def explain_nor(p: str):
    return {"type": "text", "value": " - ".join(nor_(p))}


NorQ = Q[str](
    get_seed=nor_seed,
    ask=ask_nor,
    correct=correct_nor,
    # explain=explain_nor,
)


def ask_nor_nork(p: tuple[str, str]):
    n, nk = p
    return {
        "type": "fill",
        "context": f"{sp_pronouns[nk]} {sp_direct_obj_pronouns[n]} {verbos_nor_nork['ver'][nk]}",
        "text": "ikusi [...]",
    }


def correct_nor_nork(p: tuple[str, str]):
    n, nk = p
    return "".join(nor_nork(n, nk)).replace(" ", "").replace("_", "")


def explain_nor_nork(p: tuple[str, str]):
    n, nk = p
    return {"type": "text", "value": " - ".join(nor_nork(n, nk))}


NorNorkQ = Q[tuple[str, str]](
    get_seed=get_2_args,
    ask=ask_nor_nork,
    correct=correct_nor_nork,
    # explain=explain_nor_nork,
)


def nor_nori_common_seed():
    n = choice(["3s", "3p"])
    ni = choice(pronouns)
    return n, ni


def ask_nor_nori(p: tuple[str, str]):
    n, ni = p
    nor_verb = "ha" if n == "3s" else "han"
    nor_text = "el libro" if n == "3s" else "los libros"
    return {
        "type": "fill",
        "context": f"se {sp_indirect_obj_pronouns[ni]} {nor_verb} olvidado {nor_text}",
        "text": "ahaztu [...]",
    }


def ask_nor_nori_all(p: tuple[str, str]):
    n, ni = p
    return {
        "type": "fill",
        "context": f"{verbos_nor_nori['ir a'][n]} {nor_nori_prononuns_sp[ni]}",
        "text": "joan [...]",
    }


def correct_nor_nori(p: tuple[str, str]):
    n, ni = p
    return "".join(nor_nori(n, ni)).replace(" ", "").replace("_", "")


def explain_nor_nori(p: tuple[str, str]):
    n, ni = p
    return {"type": "text", "value": " - ".join(nor_nori(n, ni))}


NorNoriCommonQ = Q[tuple[str, str]](
    get_seed=nor_nori_common_seed,
    ask=ask_nor_nori,
    correct=correct_nor_nori,
    # explain=explain_nor_nori,
)

NorNoriAllQ = Q[tuple[str, str]](
    get_seed=get_2_args,
    ask=ask_nor_nori_all,
    correct=correct_nor_nori,
    # explain=explain_nor_nori,
)


def nor_nori_nork_seed():
    n = choice(["3s", "3p"])
    ni, nk = get_2_args()

    return (n, ni, nk)


def ask_nor_nori_nork(p: tuple[str, str, str]):
    n, ni, nk = p
    nor_text = "el libro" if n == "3s" else "los libros"
    return {
        "type": "fill",
        "context": f"{sp_pronouns[nk]} {sp_indirect_obj_pronouns[ni]} {verbos_nor_nori_nork['dar'][nk]} {nor_text}",
        "text": "eman [...]",
    }


def correct_nor_nori_nork(p: tuple[str, str, str]):
    n, ni, nk = p
    return "".join(nor_nori_nork(n, ni, nk)).replace(" ", "").replace("_", "")


def explain_nor_nori_nork(p: tuple[str, str, str]):
    n, ni, nk = p
    return {"type": "text", "value": " - ".join(nor_nori_nork(n, ni, nk))}


NorNoriNorkQ = Q[tuple[str, str, str]](
    get_seed=nor_nori_nork_seed,
    ask=ask_nor_nori_nork,
    correct=correct_nor_nori_nork,
    # explain=explain_nor_nori_nork,
)

present_qs: dict[str, Q] = {}
for k, v in conj_present.items():
    present_qs[k] = Q.from_dict(v)

past_qs: dict[str, Q] = {}
for k, v in conj_past.items():
    past_qs[k] = Q.from_dict(v)

if __name__ == "__main__":
    mygame = APIGame()
    mygame.add_quiz(
        "aux",
        "Euskera - Verbo auxiliar",
        {
            "nor": NorQ,
            "nor nork": NorNorkQ,
            "nor nori (common)": NorNoriCommonQ,
            "nor nori (all)": NorNoriAllQ,
            "nor nori nork": NorNoriNorkQ,
        },
    )

    mygame.add_quiz(
        "conj_present",
        "Euskera - Conjugacion Presente",
        present_qs,
    )
    mygame.add_quiz(
        "conj_past",
        "Euskera - Conjugacion Pasado",
        past_qs,
    )

    mygame.start(host="0.0.0.0", port=8000)
