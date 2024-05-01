### BuscaCEP - Automatização de Pesquisa de Endereço ###
Este é um projeto simples de automação desenvolvido em Python usando a biblioteca Selenium. O objetivo deste projeto é realizar uma pesquisa de endereço no site dos Correios de forma automatizada, sem intervenção manual.

Funcionamento
O programa utiliza a biblioteca Selenium para abrir uma instância do navegador Chrome e navegar até o site de busca de CEP dos Correios. Em seguida, insere um CEP específico no campo de pesquisa, aciona o botão de busca e aguarda o resultado ser carregado. Após isso, extrai o endereço retornado pelo site e o exibe no console.

Requisitos
Python 3.x
Biblioteca Selenium
WebDriver do Chrome
Como usar
Certifique-se de ter o Python 3.x instalado em seu sistema.
Instale a biblioteca Selenium executando o comando pip install selenium.
Baixe o WebDriver do Chrome compatível com a versão do seu navegador e o coloque em um local acessível. Você pode baixá-lo aqui.
Clone este repositório em seu computador.
No arquivo main.py, atualize a variável chromedriver_path com o caminho para o executável do WebDriver do Chrome que você baixou anteriormente.
Execute o script main.py utilizando o Python.