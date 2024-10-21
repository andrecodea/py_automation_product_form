# 1. Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login;
# 1.1. Instalar PyAutoGUI e importar o módulo time e a biblioteca pandas
import pyautogui
import time
import pandas as pd

# pyautogui.write -> escreve um texto
# pyautogui.click -> clica com o mouse
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> executa um atalho (ex: Ctrl + C)

# Define uma pausa para cada execução de linha de código
pyautogui.PAUSE = 0.2 

# 1.2. abrir o navegador

# 1.2.1. apertar a tecla do windows
pyautogui.press("win")
# 1.2.2. busca o chrome na barra de pesquisa
pyautogui.write("chrome")
# 1.2.3. aperta enter e abre o chrome
pyautogui.press("enter")

# 2. Logar no sistema da empresa;
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)
# 2.1 Clicar na caixa de seleção e escrever o email de login
pyautogui.click(x=957, y=408)
pyautogui.write("codeajr@gmail.com")
# 2.3 Clicar na caixa de seleção e escrever a senha de login
pyautogui.press("tab")
pyautogui.write("Kcw21-09*Bs")
# 2.4 Clicar na caixa de seleção e realizar o login
pyautogui.click(x=958, y=568) # pyautogui(x = , y = , clicks = 2)

time.sleep(1)

# 3. Importar a base de dados com Pandas;
tabela = pd.read_csv("produtos.csv")

# 4. Cadastrar produtos;
for linha in tabela.index:
    pyautogui.click(x=928, y=296)
    # 4.1. Código do produto
    codigo_produto = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo_produto))
    pyautogui.press("tab")
    # 4.2. Marca do produto
    marca_produto = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca_produto))
    pyautogui.press("tab")
    # 4.3. Tipo do produto
    tipo_produto = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo_produto))
    pyautogui.press("tab")
    # 4.4. Categoria do produto
    categoria_produto = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria_produto))
    pyautogui.press("tab")
    # 4.5. Valor unitário do produto
    preco_unitario_produto = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario_produto))
    pyautogui.press("tab")
    # 4.6. Custo do produto
    custo_produto = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo_produto))
    pyautogui.press("tab")
    # 4.7. Observação
    observacao = tabela.loc[linha, "obs"]
    if not pd.isna(observacao):
        pyautogui.write(str(observacao))
    pyautogui.press("tab")
    # 4.8. Enviar
    pyautogui.press("enter")
    # 4.9. Rolar a tela para o header da página.
    pyautogui.press("home")