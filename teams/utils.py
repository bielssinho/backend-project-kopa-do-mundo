from teams.exceptions import NegativeTitlesError
from teams.exceptions import InvalidYearCupError
from teams.exceptions import ImpossibleTitlesError
from datetime import datetime


def data_processing(info_selecao: dict):
    if info_selecao.get("titles"):
        if info_selecao["titles"] < 0:
            raise NegativeTitlesError("titles cannot be negative")

    if info_selecao.get("first_cup"):
        year_first_cup_str = info_selecao["first_cup"].split("-")
        year_first_cup_int = int(year_first_cup_str[0])
        if (year_first_cup_int - 1930) % 4 != 0:
            raise InvalidYearCupError("there was no world cup this year")

        year_atual = datetime.now().strftime("%Y")
        dif_first_atual = int(year_atual) - year_first_cup_int
        if dif_first_atual // 4 < info_selecao["titles"]:
            raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
