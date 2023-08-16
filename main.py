from bs4 import BeautifulSoup
import requests
from csv import writer
import math

url = "https://setrece.com.br/page/1/?unonce=539cb25314&uformid=62&s=uwpsfsearchtrg&taxo%5B0%5D%5Bname%5D=meu-bairro" \
      "&taxo%5B0%5D%5Bopt%5D=1&taxo%5B0%5D%5Bterm%5D=uwpqsftaxoall&taxo%5B1%5D%5Bname%5D=categoria-escola&taxo%5B1%5D" \
      "%5Bopt%5D=1&taxo%5B1%5D%5Bterm%5D=uwpqsftaxoall"

headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

qtd = 56
ultima_pag = math.ceil(int(qtd) / 8)
c = 1
while True:
    if c < ultima_pag:
        url_page = f'https://setrece.com.br/page/{c}/?unonce=539cb25314&uformid=62&s=uwpsfsearchtrg&taxo%5B0' \
                   f'%5D%5Bname%5D' \
                   f'=meu-bairro&taxo%5B0%5D%5Bopt%5D=1&taxo%5B0%5D%5Bterm%5D=uwpqsftaxoall&taxo%5B1%5D' \
                   f'%5Bname%5D' \
                   f'=categoria-escola&taxo%5B1%5D%5Bopt%5D=1&taxo%5B1%5D%5Bterm%5D=uwpqsftaxoall'
        page = requests.get(url_page)
        soup = BeautifulSoup(page.text, 'html.parser')
        # print(url_page)
        print(f'Pagina {c}')
        with open('tabela_tios.csv', 'w', encoding='utf-8', newline='') as f:
            thewriter = writer(f)
            header = ['Nome' + ';' + 'Tel1' + ';' + 'Tel2' + ';' + 'WhatsApp' + ';']
            thewriter.writerow(header)

            nome_tio = soup.find_all('div', 'descr')
            lista_contatos = []

            for i2, j in enumerate(list(nome_tio)):
                lista_contatos.append(str(j).split('>'))

                for item in lista_contatos:
                    init = item[31].find("+55")
                    fim = item[31].find("&amp")
                    nome = item[4][:-4]
                    telefone1 = item[19][:-4]
                    telefone2 = item[25][:-4]
                    whatsapp = item[31][init:fim]

                    info = [nome + ';' + telefone1 + ';' + telefone2 + ';' + whatsapp + ';']

                    thewriter.writerow(info)
        c += 1
        break
    