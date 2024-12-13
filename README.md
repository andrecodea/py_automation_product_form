# Python Automation For Product Data Entries
[PTBR] Isso é automação de cadastro de produtos para uma base de dados utilizando Python e PyAutoGUI.
O objetivo desse projeto foi automatizar uma tarefa repetitiva, que é o cadastro de produtos em uma base de dados, onde devem ser inseridas as informações: 
- Nome do produto
- Código do produto
- Marca do produto
- Custo do produto
- Tipo de produto
- Valor unitário do produto
- Observação (Opcional)

[ENG] This is a Python automation for product registering using PyAutoGUI to insert product data into the company's website's form.
"The objective of this project was to automate a repetitive task, which is the registration of products in a database, where the following information must be entered:
- Product name
- Product code
- Product brand
- Product cost
- Product type
- Unit price of the product
- Observation (Optional)

## Processo de Desenvolvimento | Development Process
1. O primeiro passo do projeto foi a importação das bibliotecas `PyAutoGui`, `Pandas` e o módulo `time` | Importing `PyAutoGui`, `Pandas` libraries, and the `time` module.
3. O segundo passo foi definir uma pausa para cada execução de linha de código utilizando `pyautogui.PAUSE = 0.2` | Define a pause for each line of code.
4. O terceiro passo foi instruir o programa a abrir o navegador e logar no sistema da empresa com URL `https://dlp.hashtagtreinamentos.com/python/intensivao/login` com as instruções `pyautogui.press` e `pyautogui.write` | Instruct the program to open a web browser and log into the company's system via URL
5. O quarto passo foi importar a base de dados `produtos.csv` com a instrução `pd.read_csv("produtos.csv")` | Import DB 
6. O quinto e último passo foi cadastrar os produtos de forma automática com um loop `for` e as isntruções `pyautogui.press` e `pyautogui.write` | Register the products automatically with a `for` loop and `PyAutoGUI` instructions.
 
## Tecnologias utilizadas | Tecnologies Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI%20-%20white%20?style=for-the-badge&logo=PyAutoGUI&color=white)
