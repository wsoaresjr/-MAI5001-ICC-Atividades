# 📘 Resumo das Atividades - Funções em Python

Este resumo reúne os principais conceitos explorados nas **sete atividades sobre funções**, com explicações e exemplos práticos.

---

## 🔹 1. Potência Recursiva

* **Conceito**: calcular uma potência $base^{exp}$ de forma recursiva, ou seja, a função chama a si mesma até chegar a um caso base.
* **Comandos principais e exemplos**:

  * Definição de função:

    ```python
    def potencia(base, exp):
        ...
    ```
  * Caso base: se o expoente for zero, o resultado é sempre 1.

    ```python
    if exp == 0:
        return 1
    ```
  * Passo recursivo: multiplica a base pelo resultado da função com expoente reduzido em 1.

    ```python
    return base * potencia(base, exp-1)
    ```
* **Exemplo prático**:

  ```python
  potencia(2, 3)  # 2*2*2 = 8
  ```

---

## 🔹 2. Contagem de Maiúsculas e Minúsculas

* **Conceito**: percorrer a string caractere por caractere e verificar se são letras maiúsculas ou minúsculas.
* **Comandos principais e exemplos**:

  * `isupper()`: retorna True se o caractere for maiúsculo.

    ```python
    'A'.isupper()  # True
    ```
  * `islower()`: retorna True se o caractere for minúsculo.

    ```python
    'a'.islower()  # True
    ```
  * Contadores vão acumulando os resultados.
* **Exemplo prático**:

  ```python
  "João e Maria" → Maiúscula: 2, Minúscula: 9
  ```

---

## 🔹 3. Maior Divisor Comum (MDC) Recursivo

* **Conceito**: usar o Algoritmo de Euclides para encontrar o maior número que divide dois inteiros.
* **Comandos principais e exemplos**:

  * Caso base: se o segundo número for 0, o resultado é o primeiro.

    ```python
    if b == 0:
        return a
    ```
  * Passo recursivo: chamar a função trocando a ordem dos números e usando o resto da divisão.

    ```python
    return mdc(b, a % b)
    ```
* **Exemplo prático**:

  ```python
  mdc(10, 35)  # 5
  ```

---

## 🔹 4. Fatorial Recursivo

* **Conceito**: o fatorial de n é o produto de n por todos os inteiros menores até 1.
* **Comandos principais e exemplos**:

  * Caso base: 0! e 1! valem 1.

    ```python
    if n == 0 or n == 1:
        return 1
    ```
  * Passo recursivo: multiplica n pelo fatorial de n-1.

    ```python
    return n * fatorial(n-1)
    ```
* **Exemplo prático**:

  ```python
  fatorial(4)  # 4*3*2*1 = 24
  ```

---

## 🔹 5. Sequência de Fibonacci

* **Conceito**: cada termo é a soma dos dois anteriores.
* **Comandos principais e exemplos**:

  * Casos base:

    ```python
    if n == 0:
        return 0
    if n == 1:
        return 1
    ```
  * Passo recursivo:

    ```python
    return fib(n-1) + fib(n-2)
    ```
* **Exemplo prático**:

  ```python
  fibonacci(6)  # 8
  ```

---

## 🔹 6. Série Harmônica Recursiva

* **Conceito**: somar os inversos de 1 até n (Série Harmônica).
* **Comandos principais e exemplos**:

  * Caso base:

    ```python
    if n == 1:
        return 1
    ```
  * Passo recursivo:

    ```python
    return 1/n + serie(n-1)
    ```
  * Impressão formatada para casas decimais:

    ```python
    print(f"{resultado:.3f}")
    ```
* **Exemplo prático**:

  ```python
  serie(7)  # 2.592 (aprox)
  ```

---

## 🔹 7. Balanceamento de Parênteses

* **Conceito**: verificar se todos os parênteses de abertura têm correspondentes de fechamento na ordem correta.
* **Comandos principais e exemplos**:

  * Caso base: string vazia, verificar se contador é 0.
  * Passo recursivo: aumenta contador se for '(', diminui se for ')'.
  * Retorna False se o contador ficar negativo.
* **Exemplo prático**:

  ```python
  balanceado("(())")  # True
  balanceado("(()")   # False
  ```

---

# 🧾 Principais Conceitos Consolidados

* **Definição de funções**: `def nome_funcao(parametros):`
* **Recursão**: sempre ter um caso base e um passo recursivo.
* **Controle de fluxo**: `if`, `else`.
* **Operadores**: `%` (módulo), `*` (multiplicação), `+` (adição).
* **Strings**: `isupper()`, `islower()`, indexação (`s[0]`, `s[1:]`).
* **Formatação de saída**: f-strings (`f"{variavel:.3f}"`).
* **Definição de funções**: `def nome_funcao(parametros):`
* **Recursão**: usar caso base e passo recursivo.
* **Controle de fluxo**: `if`, `else`.
* **Operadores**: `%` (módulo), `*` (multiplicação), `+` (adição).
* **Strings**: `isupper()`, `islower()`, indexação (`s[0]`, `s[1:]`).
* **Formatação de saída**: f-strings (`f"{variavel:.3f}"`).

---

📌 Essas atividades mostram a importância das **funções recursivas** em Python para resolver problemas matemáticos e de manipulação de strings, reforçando lógica, condições e boas práticas de programação.
