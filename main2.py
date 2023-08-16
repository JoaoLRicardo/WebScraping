from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.skysports.com/premier-league-table"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

league_table = soup.find('table', class_="standing-table__table")

with open('PremierLeague.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = [
        'Position' + ';' + 'Team' + ';' + 'Points' + ';' + 'Played' + ';' + 'W' + ';' + 'D' + ';' + 'L' + ';' +
        'Goals Pro' + ';' + 'Goals Agst' + ';' + 'Goals +']
    thewriter.writerow(header)

    for team in league_table.find_all('tbody'):

        rows = team.find_all('tr')

        for row in rows:
            position_team = row.find('td', class_='standing-table__cell').text
            name_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
            points_team = row.find_all('td', class_='standing-table__cell')[9].text
            games_team = row.find_all('td', class_='standing-table__cell')[2].text
            wins_team = row.find_all('td', class_='standing-table__cell')[3].text
            loses_team = row.find_all('td', class_='standing-table__cell')[4].text
            empt_team = row.find_all('td', class_='standing-table__cell')[5].text
            goalsPro_team = row.find_all('td', class_='standing-table__cell')[6].text
            goalsAgts_team = row.find_all('td', class_='standing-table__cell')[7].text
            saldo_team = row.find_all('td', class_='standing-table__cell')[8].text

            info = [
                position_team + ';' + name_team + ';' + points_team + ';' + games_team + ';' + wins_team + ';' +
                loses_team + ';' + empt_team + ';' + goalsPro_team + ';' + goalsAgts_team + ';' + saldo_team]

            thewriter.writerow(info)
