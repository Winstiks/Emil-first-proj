import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = "https://www.cbar.az/"  # Центральный банк Азербайджана
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        rates = soup.find_all("div", class_="valyuta")
        
        for rate in rates:
            if "USD" in rate.text:
                value = rate.find("span").text.strip()
                return float(value.replace(",", "."))

        raise Exception("Не удалось найти курс USD")

    def convert_to_usd(self, azn):
        return azn / self.usd_rate


if __name__ == "__main__":
    converter = CurrencyConverter()

    amount = float(input("Введите сумму в манатах (AZN): "))
    result = converter.convert_to_usd(amount)

    print(f"{amount} AZN = {result:.2f} USD")