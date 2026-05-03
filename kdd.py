import time

palavras = list()

print("=" * 60)
print("LEITURA DO ARQUIVO E ARMAZENAMENTO DE PALAVRAS")
print("=" * 60)

try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                palavras_linha = linha.split()
                palavras.extend(palavras_linha)
    
    print(f"Total de palavras lidas: {len(palavras)}")
    print(f"Primeiras 10 palavras: {palavras[:10]}\n")
except FileNotFoundError:
    print("ERRO: Arquivo 'dados.txt' não encontrado!")
    exit(1)

# ORDENAÇÃO USANDO SORT NATIVO PYTHON
print("=" * 60)
print("ORDENAÇÃO - SORT NATIVO (Python)")
print("=" * 60)

# Medidor de tempo de execução do sort nativo
tempo_inicio = time.time()
resultado_ordenado = sorted(palavras)
tempo_fim = time.time()
tempo_execucao = tempo_fim - tempo_inicio

print(f"\n✓ Ordenação concluída com sucesso!")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
print(f"Total de palavras ordenadas: {len(resultado_ordenado)}")
print(f"\nPrimeiras 10 palavras ordenadas: {resultado_ordenado[:10]}")
print(f"Últimas 10 palavras ordenadas: {resultado_ordenado[-10:]}")

# SALVAR RESULTADO NO ARQUIVO
print("\n" + "=" * 60)
print("SALVANDO RESULTADO NO ARQUIVO")
print("=" * 60)

# Criar arquivo de saída com as palavras ordenadas
nome_arquivo_saida = "palavras_ordenadas.txt"
try:
    with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
        for palavra in resultado_ordenado:
            arquivo_saida.write(palavra + "\n")
    
    print(f"✓ Arquivo '{nome_arquivo_saida}' criado com sucesso!")
    print(f"  Total de palavras salvas: {len(resultado_ordenado)}")
    print(f"  Método utilizado: Sort Nativo Python")
    print(f"  Tempo de execução: {tempo_execucao:.6f} segundos")
except Exception as e:
    print(f"ERRO ao salvar arquivo: {e}")

print("=" * 60)
