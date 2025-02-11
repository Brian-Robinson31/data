import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/champions', methods=['GET'])
def get_champions():
    url = "https://www.metasrc.com/lol/stats"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, features="html.parser")

    table = soup.find_all("table")
    champions = []
    for row in soup.find_all('tr', class_='_sbzxul'):
        champion_name = row.find('span', hidden='hidden').text.strip()
        role = row.find('div', class_='_l09unh').text.strip()
        win_rate = row.find_all('td', class_='_byr3u7 _dbz54g')[1].text.strip()

        champion_data = {
            'name': champion_name,
            'role': role,
            'win_rate': win_rate
        }
        champions.append(champion_data)
    return jsonify(champions)