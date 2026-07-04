import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================
# CONFIGURAÇÕES DE LOGIN
# ==========================================
USUARIO_RA = "00001103685569sp"
SENHA_SED = "Jpb@123456"
URL_PLATAFORMA = "https://educacao.sp.gov.br"

# Inicializa o Navegador Chrome
servico = Service(ChromeDriverManager().install())
opcoes = webdriver.ChromeOptions()
opcoes.add_argument("--start-maximized")  # Abre em tela cheia
navegador = webdriver.Chrome(service=servico, options=opcoes)

try:
    # 1. Acessar a plataforma SED
    print("Acessando o portal SED... Aguardando carregamento inicial.")
    navegador.get(URL_PLATAFORMA)
    
    # Configura a espera dinâmica máxima para 40 segundos
    aguardar = WebDriverWait(navegador, 40)
    time.sleep(8)  # Espera inicial garantida
    
    # 2. Realizar o Login
    print("Preenchendo dados de login...")
    campo_usuario = aguardar.until(EC.presence_of_element_located((By.ID, "Name"))) 
    campo_senha = navegador.find_element(By.ID, "Senha")
    botao_entrar = navegador.find_element(By.ID, "btnEntrar")
    
    campo_usuario.send_keys(USUARIO_RA)
    time.sleep(2)  # Pausa humana entre ações
    campo_senha.send_keys(SENHA_SED)
    time.sleep(2)
    
    botao_entrar.click()
    print("Login efetuado! Aguardando o painel carregar por completo...")
    time.sleep(12)  # Tempo estendido para carregar o dashboard da SED
    
    # 3. Navegar até o Centro de Mídias (CMSP) / Tarefas
    print("Buscando o menu de tarefas no menu lateral...")
    menu_cmsp = aguardar.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'Centro de Mídias')] | //a[contains(@href, 'Tarefa')] | //span[contains(text(), 'Aluno')]")
    ))
    menu_cmsp.click()
    print("Menu expandido. Aguardando links internos...")
    time.sleep(6)

    # 4. Localizar e abrir a primeira tarefa disponível
    print("Acessando a lista de tarefas disponíveis...")
    card_tarefa = aguardar.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class, 'card')] | //tr[contains(@class, 'linha-tarefa')] | //a[contains(text(), 'Atividades')]")
    ))
    
    janela_principal = navegador.current_window_handle
    card_tarefa.click()
    print("Tarefa aberta. Carregando interface do questionário...")
    time.sleep(10)  # Tempo para carregar a nova aba ou o iframe
    
    # Verifica se a tarefa abriu em uma nova aba
    if len(navegador.window_handles) > 1:
        for janela in navegador.window_handles:
            if janela != janela_principal:
                navegador.switch_to.window(janela)
                print("Mudou o foco para a aba dedicada da tarefa.")
                time.sleep(5)
                break

    # Verifica se o conteúdo está embutido em um iframe interno do CMSP
    if len(navegador.find_elements(By.TAG_NAME, "iframe")) > 0:
        iframe = navegador.find_element(By.TAG_NAME, "iframe")
        navegador.switch_to.frame(iframe)
        print("Entrou com sucesso no ambiente interno da atividade (iframe).")
        time.sleep(5)

    # 5. Lógica para Localizar e Responder as Questões
    print("Procurando bloco de questões na página...")
    perguntas = navegador.find_elements(By.XPATH, "//div[contains(@class, 'question')] | //div[contains(@class, 'bloco')] | //fieldset")
    
    if not perguntas:
        print("Tentando seletor alternativo para as questões...")
        perguntas = navegador.find_elements(By.CLASS_NAME, "bloco-pergunta")

    print(f"Total de {len(perguntas)} questões detectadas.")
    
    for i, pergunta in enumerate(perguntas):
        print(f"Iniciando a resolução da questão {i+1}...")
        
        # Centraliza a pergunta suavemente na tela
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", pergunta)
        time.sleep(3)  # Pausa maior para evitar falhas de animação de tela
        
        # Encontra as alternativas textuais
        alternativas = pergunta.find_elements(By.XPATH, ".//label | .//input[@type='radio']/.. | .//span")
        
        if alternativas:
            # Seleciona a primeira opção
            alternativa_alvo = alternativas[0]
            
            # Força o clique injetando o comando direto nos navegadores
            navegador.execute_script(
                "arguments[0].dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true, view: window}));", 
                alternativa_alvo
            )
            print(f"Questão {i+1} marcada.")
            time.sleep(3)  # Espera o site computar a resposta interna
        else:
            print(f"Aviso: Nenhuma opção clicável identificada para a questão {i+1}.")

    # 6. Enviar a tarefa finalizada
    print("Procurando o botão de envio final...")
    botao_enviar = navegador.find_element(By.XPATH, "//button[contains(text(), 'Enviar') or contains(text(), 'Finalizar') or @type='submit']")
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_enviar)
    time.sleep(3)
    
    navegador.execute_script("arguments[0].click();", botao_enviar)
    print("Tarefa concluída e enviada com sucesso!")
    time.sleep(6)

except Exception as erro:
    # Captura e detalha exatamente qual foi o erro no terminal
    print(f"\n[ERRO CONSTATADO]: {erro}")

finally:
    navegador.quit()
    print("Navegador fechado automaticamente.")

