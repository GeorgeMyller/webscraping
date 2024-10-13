from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

# Configuração inicial
url = 'https://www.morphmarket.com/all/c/all'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"
}

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument('--head')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


# Estrutura de dados para armazenar os resultados
dic_produtos = {'marca': [], 'preco': [], 'sexo': [], 'traits': [], 'origem': [], 'nascimento': [], 'link': []}

# Iterar sobre múltiplas páginas da listagem de produtos
for i in range(1, 2):  # Ajuste o range conforme necessário para testar
    url_pag = f'{url}?page_number={i}'
    print(f"Accessing: {url_pag}")  # Debugging: print the current page
    driver.get(url_pag)
    time.sleep(10)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('class="animalCardContent--piRWx"'))

    if not produtos:
        print("No products found on this page.")  # Debugging: If no products are found

    for produto in produtos:
        # Capturar nome da marca e preço
        try:
            marca = produto.find('span', class_=re.compile('animalTitle--lz_Ps')).get_text().strip()
            preco = produto.find('span', class_=re.compile('price--Dcnmw')).get_text().strip()
        except AttributeError:
            print("Error finding marca/preço")  # Debugging: In case of errors
            continue

        # Capturar link do produto
        try:
            produto_link = produto.find('a', href=True)['href']
            produto_url = f'https://www.morphmarket.com{produto_link}'
        except TypeError:
            print("Error finding product link")  # Debugging: If product link not found
            continue

        print(f"Found product: {marca} - {preco} - {produto_url}")  # Debugging: Print each product found

        # Acessar a página de detalhes do produto
        driver.get(produto_url)
        time.sleep(10)
        produto_soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Scraping dos detalhes do produto (Sexo, Traits, Origem, Nascimento)
        try:
            sexo = produto_soup.find('span', text='Sex:').find_next('span').get_text().strip()
        except AttributeError:
            sexo = 'N/A'
        
        try:
            traits = produto_soup.find('span', text='Traits:').find_next('span').get_text().strip()
        except AttributeError:
            traits = 'N/A'
        
        try:
            origem = produto_soup.find('span', text='Origin:').find_next('span').get_text().strip()
        except AttributeError:
            origem = 'N/A'
        
        try:
            nascimento = produto_soup.find('span', text='Birth:').find_next('span').get_text().strip()
        except AttributeError:
            nascimento = 'N/A'

        # Armazenar os resultados
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)
        dic_produtos['sexo'].append(sexo)
        dic_produtos['traits'].append(traits)
        dic_produtos['origem'].append(origem)
        dic_produtos['nascimento'].append(nascimento)
        dic_produtos['link'].append(produto_url)

        print(f'{marca} - {preco} - {sexo} - {traits} - {origem} - {nascimento} - {produto_url}')  # Debugging: Check if details are fetched

    print(f'Página {i} completa: {url_pag}')

# Fechar o driver
driver.quit()

# Verificar os dados armazenados antes de salvar
if dic_produtos['marca']:
    print("Saving results to CSV")  # Debugging: Confirm before saving
    df = pd.DataFrame(dic_produtos)
    df.to_csv('detalhes_produtos.csv', encoding='utf-8', sep=';')
else:
    print("No data to save.")  #
