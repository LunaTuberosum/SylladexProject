from dataclasses import dataclass


@dataclass
class CodeData():
    name: str = "-"
    code: str = "-"

    kind: str = ''
    grist: str = ''
    trait_1: str = ''
    trait_2: str = ''
    action_1: str = ''
    action_2: str = ''
    action_3: str = ''
    action_4: str = ''

    cardID: int = 0
