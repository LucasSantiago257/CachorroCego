import random

rows, cols = (10, 10)
actions = ['cima', 'baixo', 'esquerda', 'direita']
dog_position = (0,0)
print("Cachorro cego começando na posição", dog_position)
food_position = (random.randint(0, rows-1), random.randint(0, cols-1))
print("Comida colocada na posição", food_position)

def choose_action(position, action) -> tuple[int, int]:
    """
    Escolhe a próxima ação com base na posição atual e na ação desejada.
    Args:
    position (tuple): A posição atual do cachorro (linha, coluna).
    action (str): A ação desejada ('cima', 'baixo', 'esquerda', 'direita').

    Returns:
    Uma tupla representando a ação que o cachorro tomará.
    """
    
    r, c = position
    if action == 'cima' and r > 0:
        r -= 1
    elif action == 'baixo' and r < rows - 1:
        r += 1
    elif action == 'esquerda' and c > 0:
        c -= 1
    elif action == 'direita' and c < cols - 1:
        c += 1
    return (r, c)

best_path = None

max_steps = input("Quantos passos seu cachorro pode dar?")
try:
    max_steps = int(max_steps)
except:
    print("Seu cachorro não te obedeceu e vai andar 1000 passos")
    max_steps = 1000

episode_amount = input("Em quantos episódios você quer treinar o cachorro?")
try:
    episode_amount = int(episode_amount)
except:
    print("Entrada inválida. Utilizando valor padrão de 100 episódios")
    episode_amount = 100
for episode in range(episode_amount): # N Vezes até achar o melhor caminho
    dog_position = (0,0)
    path = [dog_position]
    steps_taken = 0
    while dog_position != food_position and steps_taken < max_steps: # A cada iteração, tem uma chance de percorrer um passo já conhecido...
        if best_path and random.random() < 0.7:
            next_index = len(path)-1
            if next_index < len(best_path)-1:
                dog_position = best_path[next_index + 1]
            else:
                break
            
        else: # ... Ou um aleatório
            action = random.choice(actions)
            next_step = choose_action(dog_position, action)
            steps_taken += 1
            
            
            if next_step not in path:
                path.append(dog_position)
                dog_position = next_step
            
        
        if dog_position == food_position: # Achou! Verifica se o caminho achado é melhor que o achado anteriormente
            path.append(dog_position)
            if not best_path or len(path) < len(best_path):
                best_path = path
            break
        else:
            if steps_taken >= max_steps:
                final_path = path
                break

if best_path:
    print(f"O Cachorro cego encontrou a comida em {steps_taken} passos!")
    print("Caminho:", best_path)

if not best_path:
    print("O Cachorro cego não conseguiu encontrar a comida.")
    print("R.I.P")
    print("Caminho final:", final_path)
