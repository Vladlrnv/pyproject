def filter_by_state(list_: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает список словарей по ключу state"""
    return [x for x in list_ if x.get("state") == state]


# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#         "CANCELED",
#     )
# )


def sort_by_date(list_: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращает список словарей отсортированный по ключу date"""
    return sorted(list_, key=lambda list_: list_["date"], reverse=reverse)


# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#         False,
#     )
# )
