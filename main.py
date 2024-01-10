import subprocess
import csv

# Leia os endereços IP do arquivo de entrada
with open('caminho\do\arquivo\ips.txt', 'r') as f:
    ips = f.readlines()

# Crie uma lista para armazenar os resultados
results = []

# Faça um ping em cada IP e armazene o resultado
for ip in ips:
    ip = ip.strip()  # Remova espaços em branco e quebras de linha
    command = ['ping', '-n', '1', ip] # Comando de ping que o subprocess vai executar
    result = subprocess.run(command, text=True, capture_output=True) # Executa o comando

    #Verificação se a saida tem o TTL, se tiver o IP está online e pingando se não está offline
    if "TTL" in result.stdout:
        status = 'Online'
    else:
        status = 'Offline'
    results.append((ip, status))

# Escreva os resultados no arquivo CSV
with open('relatorio-ip.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['IP', 'Status'])  # Escreve o cabeçalho
    for ip, status in results:
        writer.writerow([ip, status])  # Escreve os dados
    
    print('Informacoes salva no arquivo relatorio')
