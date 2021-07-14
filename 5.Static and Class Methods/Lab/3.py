import roman
class Integer:
    def __init__(self,value):
        self.value = value

    @classmethod
    def from_float(cls,float_value):
        if not isinstance(float_value,float):
            return 'value is not a float'
        return cls(int(float_value))

    @classmethod
    def from_roman(cls,value):
        result = roman.fromRoman(value)
        return cls(result)

    @classmethod
    def from_string(cls,value):
        if not isinstance(value,str):
            return 'wrong type'
        try:
            return cls(int(value))
        except:
            return 'wrong type'