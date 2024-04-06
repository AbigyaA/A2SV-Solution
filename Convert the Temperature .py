class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        kelvin = float(f"{kelvin:.5f}")
        fahrenheit = float(f"{fahrenheit:.5f}")
        ans=[kelvin, fahrenheit]
        return ans
