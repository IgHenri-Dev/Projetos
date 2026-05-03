from colorama import Fore, Style, init

# Inicializa o colorama para garantir funcionamento no Windows e limpar o estilo automaticamente
init(autoreset=True)

def exibir_alerta(nivel_index):
    """
    Função responsável por definir a cor e exibir a mensagem 
    conforme o nível informado.
    """
    # Lista de dicionários para organizar os dados de forma estruturada
    niveis = [
        {"msg": "Muito baixo (crítico)", "cor": Fore.RED},
        {"msg": "Baixo", "cor": Fore.YELLOW},
        {"msg": "Médio", "cor": Fore.GREEN},
        {"msg": "Alto", "cor": Fore.CYAN},
        {"msg": "Muito alto (alerta)", "cor": Fore.BLUE}
    ]

    try:
        # Busca os dados na lista baseados no índice (0 a 4)
        status = niveis[nivel_index]
        
        print(f"Status do Reservatório: {status['cor']}{status['msg']}")
        
    except IndexError:
        print(f"{Fore.WHITE}Nível inválido. Informe um valor entre 1 e 5.")

# --- Simulação do Sistema ---

print("--- MONITORAMENTO DE RESERVATÓRIO ---")

# Exemplo: Percorrendo todos os níveis para demonstração
for i in range(5):
    print(f"Nível {i+1}: ", end="")
    exibir_alerta(i)

# O estilo já é restaurado automaticamente pelo 'autoreset=True' no init()