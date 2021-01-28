
# @Title: 表示数值的字符串 (表示数值的字符串 LCOF)
# @Author: 18015528893
# @Date: 2021-01-17 22:16:18
# @Runtime: 404 ms
# @Memory: 15 MB

from enum import Enum, auto


class Solution:
    def isNumber(self, s: str) -> bool:
        class State(Enum):
            STATE_INITIAL = auto()
            STATE_INT_SIGN = auto()
            STATE_INTEGER = auto()
            STATE_POINT = auto()
            STATE_POINT_WITHOUT_INT = auto()
            STATE_FRACTION = auto()
            STATE_EXP = auto()
            STATE_EXP_SIGN = auto()
            STATE_EXP_NUMBER = auto()
            STATE_END = auto()

        class CharType(Enum):
            CHAR_NUMBER = auto()
            CHAR_EXP = auto()
            CHAR_POINT = auto()
            CHAR_SIGN = auto()
            CHAR_SPACE = auto()
            CHAR_ILLEGAL = auto()

        def toCharType(ch):
            if ch.isdigit():
                return CharType.CHAR_NUMBER
            elif ch.lower() == "e":
                return CharType.CHAR_EXP
            elif ch == ".":
                return CharType.CHAR_POINT
            elif ch == "+" or ch == "-":
                return CharType.CHAR_SIGN
            elif ch == " ":
                return CharType.CHAR_SPACE
            else:
                return CharType.CHAR_ILLEGAL

        transfer = {
            State.STATE_INITIAL: {
                CharType.CHAR_SPACE: State.STATE_INITIAL,
                CharType.CHAR_NUMBER: State.STATE_INTEGER,
                CharType.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                CharType.CHAR_SIGN: State.STATE_INT_SIGN,
            },
            State.STATE_INT_SIGN: {
                CharType.CHAR_NUMBER: State.STATE_INTEGER,
                CharType.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
            },
            State.STATE_INTEGER: {
                CharType.CHAR_NUMBER: State.STATE_INTEGER,
                CharType.CHAR_EXP: State.STATE_EXP,
                CharType.CHAR_POINT: State.STATE_POINT,
                CharType.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT: {
                CharType.CHAR_NUMBER: State.STATE_FRACTION,
                CharType.CHAR_EXP: State.STATE_EXP,
                CharType.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT_WITHOUT_INT: {
                CharType.CHAR_NUMBER: State.STATE_FRACTION,
            },
            State.STATE_FRACTION: {
                CharType.CHAR_NUMBER: State.STATE_FRACTION,
                CharType.CHAR_EXP: State.STATE_EXP,
                CharType.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_EXP: {
                CharType.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                CharType.CHAR_SIGN: State.STATE_EXP_SIGN,
            },
            State.STATE_EXP_SIGN: {
                CharType.CHAR_NUMBER: State.STATE_EXP_NUMBER,
            },
            State.STATE_EXP_NUMBER: {
                CharType.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                CharType.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_END: {
                CharType.CHAR_SPACE: State.STATE_END,
            },
        }

        st = State.STATE_INITIAL
        for ch in s:
            char_type = toCharType(ch)
            if char_type not in transfer[st]:
                return False
            st = transfer[st][char_type]

        return st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, 
                      State.STATE_EXP_NUMBER, State.STATE_END]

