# Python Power Up
Python Power Up é uma automação de cadastro de produtos para uma base de dados utilizando Python e PyAutoGUI.
O objetivo desse projeto foi automatizar uma tarefa repetitiva, que é o cadastro de produtos em uma base de dados, onde devem ser inseridas as informações: 
- Nome do produto
- Código do produto
- Marca do produto
- Custo do produto
- Tipo de produto
- Valor unitário do produto
- Observação (Opcional)

## Processo de Desenvolvimento
1. O primeiro passo do projeto foi a importação das bibliotecas `PyAutoGui`, `Pandas` e o módulo `time`;
3. O segundo passo foi definir uma pausa para cada execução de linha de código utilizando `pyautogui.PAUSE = 0.2`;
4. O terceiro passo foi instruir o programa a abrir o navegador e logar no sistema da empresa com URL `https://dlp.hashtagtreinamentos.com/python/intensivao/login` com as instruções `pyautogui.press` e `pyautogui.write`;
5. O quarto passo foi importar a base de dados `produtos.csv` com a instrução `pd.read_csv("produtos.csv")`;
6. O quinto e último passo foi cadastrar os produtos de forma automática com um loop `for` e as isntruções `pyautogui.press` e `pyautogui.write`.  .
 
## Tecnologias utilizadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI%20-%20white%20?style=for-the-badge&logo=PyAutoGUI&color=white)
