class SimpleMath:
    """Класс с простыми математическими операциями"""

    def square(self, x, y=2):
    # Возвращает квадрат числа
        return x ** y

    def cube(self, y):
    # Возвращает куб числа
        return y * y * y

    def sum(selfself, x, y):
    # Возвращает куб числа
        return x + y

    def diff(self, x, y):
    # Возвращает разницу чисел
        return x - y

    def avg(self, nums):
        if len (nums) == 0:
            raise ValueError("Cannot average an empty list")
        s = sum(nums)
        return s / len(nums)