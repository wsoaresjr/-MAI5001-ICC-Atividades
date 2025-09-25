# 📘 Resumo das Atividades - Conceitos Básicos e Estruturas de Controle em Python

Este resumo reúne os principais conceitos explorados nas **nove atividades** realizadas, com explicações simples sobre a lógica, os comandos mais usados e exemplos práticos.

---

## 🔹 1. Conversão de Tempo (HH\:MM\:SS → Segundos)

* **Conceito**: manipulação de strings e operações matemáticas.
* **Comandos principais**:

  * `split(":")`: separa a string em partes.
    Exemplo: `"02:30:53".split(":") → ['02','30','53']`
  * `int()`: converte string para inteiro.
    Exemplo: `int('02') → 2`
  * Operações matemáticas: `h*3600 + m*60 + s`.
    Exemplo: `2*3600 + 30*60 + 53 → 9053`

---

## 🔹 2. Divisíveis por 5 e 7

* **Conceito**: uso de laços e condições.
* **Comandos principais**:

  * `for n in range(min, max+1)`: percorre o intervalo.
    Exemplo: `range(10,20) → 10,11,...,19,20`
  * `if n % 7 == 0 and n % 5 == 0`: verifica múltiplos.
  * `lista.append(n)`: adiciona valores.
  * `",".join(lista)`: formata saída.
    Exemplo: `[105,140] → "105,140"`

---

## 🔹 3. Frequência de Caracteres

* **Conceito**: contagem de elementos em uma string.
* **Comandos principais**:

  * `for c in texto`: percorre cada caractere.
  * Dicionário `{}`: armazena frequências.
    Exemplo: `{'a':2, 'b':1}`
  * Estrutura condicional:

    ```python
    if c in freq:
        freq[c]+=1
    else:
        freq[c]=1
    ```

---

## 🔹 4. Multiplicação de Matrizes 2x2

* **Conceito**: aritmética com matrizes.
* **Comandos principais**:

  * `split()`: separa valores da entrada.
  * Fórmulas:
    `c11 = a11*b11 + a12*b21`
  * Impressão:

    ```python
    print(c11, c12)
    print(c21, c22)
    ```

---

## 🔹 5. Contagem de Palavras

* **Conceito**: processamento de strings.
* **Comandos principais**:

  * `lower()`: minúsculas. → `"Teste".lower() → "teste"`
  * `re.sub()`: remove pontuações.
    Exemplo: `re.sub(r'[^a-zA-Z ]','',texto)`
  * `split()`: divide em palavras. → `"um teste" → ['um','teste']`
  * Dicionário para frequências.

---

## 🔹 6. Números Primos

* **Conceito**: verificar se um número tem apenas dois divisores.
* **Comandos principais**:

  * `for n in range(min, max+1)` → percorre intervalo.
  * Testa divisores até `int(n**0.5)+1`.
    Exemplo: `n=29` → checa até 6.
  * Se nenhum divisor → número é primo.

---

## 🔹 7. Média de Três Números

* **Conceito**: aritmética simples.
* **Comandos principais**:

  * `map(int, input().split())`: lê três inteiros. → `"4 5 6" → [4,5,6]`
  * `sum(lista)/3`: calcula média. → `(4+5+6)/3 = 5`
  * `print(f"{media:.1f}")`: imprime com 1 casa decimal. → `5.0`

---

## 🔹 8. Frequência de Bigramas

* **Conceito**: pares consecutivos de palavras.
* **Comandos principais**:

  * `split()`: divide texto em lista. → `"eu gosto" → ['eu','gosto']`
  * `for i in range(len(palavras)-1)`: percorre pares.
  * `palavras[i] + " " + palavras[i+1]`: cria bigrama. → `"eu gosto"`

---

## 🔹 9. Números Perfeitos

* **Conceito**: soma dos divisores próprios.
* **Comandos principais**:

  * `for i in range(1, n)`: percorre divisores.
  * `if n % i == 0`: soma divisor.
  * Se soma == número → é perfeito. → Exemplo: `6 = 1+2+3`
  * Cada número em linha separada:

    ```python
    for p in perfeitos:
        print(p)
    ```

---

# 🧾 Principais Conceitos Consolidadores

* **Entrada e saída**:

  * `input()`: lê do usuário.
  * `sys.stdin.read()`: lê tudo de uma vez (usado em juízes online).
  * `print()`: exibe saída.
* **Conversão**: `int()`, `map()`, `list()`.
* **Laços**: `for`, `range()`, `while`.
* **Condições**: `if`, `else`, operadores (`%`, `==`, `and`, `or`).
* **Estruturas de dados**: listas (`[]`), dicionários (`{}`).
* **Manipulação de strings**: `split()`, `lower()`, `join()`, `replace()`, `re.sub()`.
* **Formatação**: f-strings (`f"{variavel:.1f}"`).

---

📌 Este conjunto de atividades cobre a base essencial para programar em Python: **entrada/saída, estruturas de repetição, condições, manipulação de strings, listas, dicionários e operações matemáticas**, agora com exemplos práticos de aplicação.
