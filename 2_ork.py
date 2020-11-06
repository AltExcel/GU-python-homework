class NullDivision:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def null_divide(divider, denominator):
        try:
            return divider / denominator
        except ZeroDivisionError:
            return f"Деление на ноль недопустимо"


div = NullDivision(45, 10)
print(NullDivision.null_divide(45, 0))
print(NullDivision.null_divide(45, 0.1))
print(div.null_divide(10, 0))
