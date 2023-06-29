from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://setrece.com.br/page/3/?unonce=539cb25314&uformid=62&s=uwpsfsearchtrg&taxo%5B0%5D%5Bname%5D=meu-bairro&taxo%5B0%5D%5Bopt%5D=1&taxo%5B0%5D%5Bterm%5D=uwpqsftaxoall&taxo%5B1%5D%5Bname%5D=categoria-escola&taxo%5B1%5D%5Bopt%5D=1&taxo%5B1%5D%5Bterm%5D=uwpqsftaxoall"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

tio_list = soup.find_all('h5')
# print(tio_list)

# for nome in tio_list:
#     nome_tios = nome.text
#     print(nome_tios)

whats_list = soup.find_all('li', {'class':'icon-fav'})
print(whats_list)

# for nome in tio_list.find_all('h5'):
#     rows = nome.find_all('h5')
#     for row in rows:
#         nome_tio = row.find('h5').text
#         print(nome_tio)


# with open('tabela_tios.csv', 'w', encoding='utf8', newline='') as f:
#     thewriter = writer(f)
#     header = [
#         'Nome' + ';' + 'Team' + ';' + 'Points' + ';' + 'Played' + ';' + 'W' + ';' + 'D' + ';' + 'L' + ';' +
#         'Goals Pro' + ';' + 'Goals Agst' + ';' + 'Goals +']
#     thewriter.writerow(header)

#     for team in tio_list.find_all('tbody'):

#         rows = team.find_all('tr')

#         for row in rows:
#             nome_tio = row.find('td', class_='col-lg-12').text
#             # name_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
#             # points_team = row.find_all('td', class_='standing-table__cell')[9].text
#             # games_team = row.find_all('td', class_='standing-table__cell')[2].text
#             # wins_team = row.find_all('td', class_='standing-table__cell')[3].text
#             # loses_team = row.find_all('td', class_='standing-table__cell')[4].text
#             # empt_team = row.find_all('td', class_='standing-table__cell')[5].text
#             # goalsPro_team = row.find_all('td', class_='standing-table__cell')[6].text
#             # goalsAgts_team = row.find_all('td', class_='standing-table__cell')[7].text
#             # saldo_team = row.find_all('td', class_='standing-table__cell')[8].text

#             info = [nome_tio + ';']
#             # info = [
#             #     position_team + ';' + name_team + ';' + points_team + ';' + games_team + ';' + wins_team + ';' +
#             #     loses_team + ';' + empt_team + ';' + goalsPro_team + ';' + goalsAgts_team + ';' + saldo_team]

#             thewriter.writerow(info)
