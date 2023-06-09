class Bank:
    _BALANCE = 0
    _MIN = 50
    _COMMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.10
    _OPERATION: int

    def __init__(self):
        self._OPERATION = 0

    def _in(self, cash: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0:
            self._BALANCE += cash
            self._OPERATION += 1
            return self._OPERATION, self._OPERATION
        else:
            return None

    def out(self, cash: int) -> tuple[int, int] | None:
        if cash % self._MIN and self._BALANCE > 0 and self._BALANCE - cash >= 0:
            self._BALANCE -= cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _check_commission(self, cash: int) ->int:
        pass


    def exit(self):
        return "Всего доброго "

    def start(self, mode: str, cash: int = 0) -> str:

        match mode:
            case "in":
                data = self._in(cash=cash)

                if data:
                    com_data = self._check_commission(cash=cash)

            case "out":
                data = self.out(cash=cash)
                if data:
                    com_data = self._check_commission(cash=cash)
            case "exit":
                return self.exit()