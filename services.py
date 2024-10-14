import requests
import xml.etree.ElementTree as ET


async def get_currency():
    try:
        xml = requests.get('https://cbr.ru/scripts/XML_daily.asp').text
        root = ET.fromstring(xml)
        # R01235 - код валюты
        # замена запятой на точку для корректного преобразования 
        usd = root.findall('./Valute[@ID="R01235"]/Value')[0].text.replace(',', '.')
        return round(float(usd), 2)
    except requests.exceptions.RequestException:
        return -1
