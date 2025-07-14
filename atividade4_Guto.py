import random

random.seed(1234)  # Define a semente para gerar os mesmos sorteios

dado = [1, 2, 3, 4, 5, 6]
n_lancamento = 0
sorteio = 0

while sorteio != 5:
    sorteio = random.choice(dado)  # Sorteia um valor aleatório do dado
    n_lancamento += 1
    
    print(f"\nLançamento: {n_lancamento}\nValor Sorteado: {sorteio}")
