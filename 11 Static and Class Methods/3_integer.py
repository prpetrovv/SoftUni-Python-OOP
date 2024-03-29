class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return f"value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, r_number):
        roman_numbers = {"I": 1,
                         "V": 5,
                         "X": 10,
                         "L": 50,
                         "C": 100,
                         "D": 500,
                         "M": 1000
                         }

        int_value = 0

        for i in range(len(r_number)):
            if r_number[i] in roman_numbers:
                if i + 1 < len(r_number) and roman_numbers[r_number[i]] < roman_numbers[r_number[i + 1]]:
                    int_value -= roman_numbers[r_number[i]]
                else:
                    int_value += roman_numbers[r_number[i]]
        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
