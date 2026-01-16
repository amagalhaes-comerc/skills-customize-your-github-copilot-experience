# 📘 Tarefa: Jogos em Python

## 🎯 Objetivo

Construir o clássico jogo da Forca para praticar manipulação de strings, loops, condicionais e entrada de usuário em Python.

## 📝 Tarefas

### 🛠️ Forca (CLI) Básico

#### Descrição
Crie um jogo da Forca no terminal que escolhe uma palavra aleatória de uma lista predefinida e permite ao jogador adivinhar uma letra por vez até revelar a palavra ou esgotar as tentativas.

#### Requisitos
Programa concluído deve:

- Manter uma lista com pelo menos 10 palavras e selecionar aleatoriamente uma (ex.: `random.choice`).
- Exibir o progresso usando sublinhados para letras ocultas (ex.: `_ _ a _ _`).
- Aceitar um palpite de uma única letra por turno via `input()` e atualizar o progresso nos acertos.
- Controlar e exibir as tentativas incorretas restantes (sugerido: 6 erros permitidos).
- Exibir letras já tentadas.
- Encerrar quando a palavra for revelada (vitória) ou as tentativas acabarem (derrota), e mostrar a palavra alvo.

Exemplo de interação (simplificado):

```
_ _ _ _ _    Erros restantes: 6    Tentadas: -
Adivinhe uma letra: a
_ a _ _ _    Erros restantes: 6    Tentadas: a
Adivinhe uma letra: e
_ a _ _ _    Erros restantes: 5    Tentadas: a, e
...
Você venceu! A palavra era "magic".
```


### 🛠️ Aprimoramentos e Robustez

#### Descrição
Melhore a experiência do usuário e a confiabilidade com validação de entrada e recursos de qualidade de vida.

#### Requisitos
Programa concluído deve:

- Tratar palpites de forma case-insensível (ex.: `A` igual a `a`).
- Validar entrada: aceitar apenas um único caractere alfabético; solicitar novamente caso contrário.
- Lidar com palpites repetidos sem penalizar; avisar que a letra já foi tentada.
- Perguntar se deseja jogar novamente quando a rodada terminar e reiniciar sem encerrar o programa.
