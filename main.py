from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Passo 1: Instanciar o webdriver
driver = webdriver.Chrome()

# Passo 2: Acessando o link
driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

# Passo 3: Encontrando o campo de endereço e inserindo o CEP conhecido
cep_input = driver.find_element(By.NAME, "endereco")
cep_input.send_keys("PUT-CEP-HERE")  # Alteração: Use o CEP diretamente

# Passo 4: Acessando o botão buscar e acionando o evento de clique
buscar_button = driver.find_element(By.XPATH, "//button[text()='Buscar']")
buscar_button.click()

# Passo 7: Aguardando 3 segundos para o resultado aparecer
time.sleep(3)

# Passo 8: Obtendo a tabela de resultados
table = driver.find_element(By.ID, "resultado-DNEC")

# Passo 9: Obtendo os campos de endereço, bairro e cidade/UF
endereco = table.find_element(By.XPATH, ".//tbody/tr[1]/td[1]").text
bairro = table.find_element(By.XPATH, ".//tbody/tr[1]/td[2]").text
cidade_uf = table.find_element(By.XPATH, ".//tbody/tr[1]/td[3]").text

# Passo 10: Apresentando o resultado
print("Endereço:", endereco)
print("Bairro:", bairro)
print("Cidade/UF:", cidade_uf)

# Fechando o webdriver
driver.quit()
