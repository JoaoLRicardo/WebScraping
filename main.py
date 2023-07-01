from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://setrece.com.br/page/3/?unonce=539cb25314&uformid=62&s=uwpsfsearchtrg&taxo%5B0%5D%5Bname%5D=meu-bairro&taxo%5B0%5D%5Bopt%5D=1&taxo%5B0%5D%5Bterm%5D=uwpqsftaxoall&taxo%5B1%5D%5Bname%5D=categoria-escola&taxo%5B1%5D%5Bopt%5D=1&taxo%5B1%5D%5Bterm%5D=uwpqsftaxoall"

headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# tio_list = soup.find_all('h5')
# print(tio_list)

nome_tio = soup.find_all('div', 'descr')

lista_contatos = []

for i,j in enumerate(list(nome_tio)):
    lista_contatos.append(str(j).split('>'))

with open('tabela_tios.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Nome' + ';' + 'Tel1' + ';' + 'Tel2' + ';' + 'WhatsApp' + ';']
    thewriter.writerow(header)

for item in lista_contatos:
  init = item[31].find("+55")
  fim = item[31].find("&amp")
  nome = item[4][:-4]
  telefone1 = item[19][:-4]
  telefone2 = item[25][:-4]
  whatsapp = item[31][init:fim]
  print(nome)
  print(telefone1)
  print(telefone2)
  print(whatsapp)
  print()
info = [nome + ';']
info = ['nome' + ';' + 'telefone1' + ';' + 'telefone1' + ';' + 'whatsapp' + ';']

thewriter.writerow(info)
    


# for nome in tio_list:
#     nome_tios = nome.text
#     print(nome_tios)

# whats_list = soup.find_all('li', {'class':'icon-fav'})
# print(whats_list)

# for nome in tio_list.find_all('h5'):
#     rows = nome.find_all('h5')
#     for row in rows:
#         nome_tio = row.find('h5').text
#         print(nome_tio)



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


