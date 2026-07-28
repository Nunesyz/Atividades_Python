# Atividade - Aula 15 (API REST)

## Resultado após inserir 15 livros (POST) e atualizar o id 1 (PUT)

Comando: `Invoke-RestMethod http://127.0.0.1:5000/api/livros`

```
ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-28 11:05:21.534602
id           : 3
titulo       : 1984

ano          : 1915
autor        : Franz Kafka
data_criacao : 2026-07-28 11:05:50.727873
id           : 13
titulo       : A Metamorfose

ano          : 1945
autor        : George Orwell
data_criacao : 2026-07-28 11:05:50.672688
id           : 7
titulo       : A Revolução dos Bichos

ano          : 1937
autor        : Jorge Amado
data_criacao : 2026-07-28 11:05:50.652847
id           : 5
titulo       : Capitães da Areia

ano          : 1967
autor        : Gabriel García Márquez
data_criacao : 2026-07-28 11:05:50.736880
id           : 14
titulo       : Cem Anos de Solidão

ano          : 2026
autor        : 3A1
data_criacao : 2026-07-28 11:05:21.534594
id           : 1
titulo       : Cotemig

ano          : 1866
autor        : Fiódor Dostoiévski
data_criacao : 2026-07-28 11:05:50.718737
id           : 12
titulo       : Crime e Castigo

ano          : 1965
autor        : Frank Herbert
data_criacao : 2026-07-28 11:05:50.701112
id           : 10
titulo       : Duna

ano          : 1995
autor        : José Saramago
data_criacao : 2026-07-28 11:05:50.773659
id           : 18
titulo       : Ensaio Sobre a Cegueira

ano          : 1956
autor        : Guimarães Rosa
data_criacao : 2026-07-28 11:05:50.636797
id           : 4
titulo       : Grande Sertão: Veredas

ano          : 1997
autor        : J.K. Rowling
data_criacao : 2026-07-28 11:05:50.692038
id           : 9
titulo       : Harry Potter e a Pedra Filosofal

ano          : 1865
autor        : José de Alencar
data_criacao : 2026-07-28 11:05:50.764573
id           : 17
titulo       : Iracema

ano          : 1881
autor        : Machado de Assis
data_criacao : 2026-07-28 11:05:50.663302
id           : 6
titulo       : Memórias Póstumas de Brás Cubas

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-28 11:05:21.534601
id           : 2
titulo       : O Cortiço

ano          : 1937
autor        : J.R.R. Tolkien
data_criacao : 2026-07-28 11:05:50.710059
id           : 11
titulo       : O Hobbit

ano          : 1943
autor        : Antoine de Saint-Exupéry
data_criacao : 2026-07-28 11:05:50.682143
id           : 8
titulo       : O Pequeno Príncipe

ano          : 1954
autor        : J.R.R. Tolkien
data_criacao : 2026-07-28 11:05:50.745931
id           : 15
titulo       : O Senhor dos Anéis: A Sociedade do Anel

ano          : 1938
autor        : Graciliano Ramos
data_criacao : 2026-07-28 11:05:50.755513
id           : 16
titulo       : Vidas Secas
```

## Resultado após excluir os livros de id 5, 6 e 7 (DELETE)

Comando: `Invoke-RestMethod http://127.0.0.1:5000/api/livros`

```
ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-28 11:05:21.534602
id           : 3
titulo       : 1984

ano          : 1915
autor        : Franz Kafka
data_criacao : 2026-07-28 11:05:50.727873
id           : 13
titulo       : A Metamorfose

ano          : 1967
autor        : Gabriel García Márquez
data_criacao : 2026-07-28 11:05:50.736880
id           : 14
titulo       : Cem Anos de Solidão

ano          : 2026
autor        : 3A1
data_criacao : 2026-07-28 11:05:21.534594
id           : 1
titulo       : Cotemig

ano          : 1866
autor        : Fiódor Dostoiévski
data_criacao : 2026-07-28 11:05:50.718737
id           : 12
titulo       : Crime e Castigo

ano          : 1965
autor        : Frank Herbert
data_criacao : 2026-07-28 11:05:50.701112
id           : 10
titulo       : Duna

ano          : 1995
autor        : José Saramago
data_criacao : 2026-07-28 11:05:50.773659
id           : 18
titulo       : Ensaio Sobre a Cegueira

ano          : 1956
autor        : Guimarães Rosa
data_criacao : 2026-07-28 11:05:50.636797
id           : 4
titulo       : Grande Sertão: Veredas

ano          : 1997
autor        : J.K. Rowling
data_criacao : 2026-07-28 11:05:50.692038
id           : 9
titulo       : Harry Potter e a Pedra Filosofal

ano          : 1865
autor        : José de Alencar
data_criacao : 2026-07-28 11:05:50.764573
id           : 17
titulo       : Iracema

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-28 11:05:21.534601
id           : 2
titulo       : O Cortiço

ano          : 1937
autor        : J.R.R. Tolkien
data_criacao : 2026-07-28 11:05:50.710059
id           : 11
titulo       : O Hobbit

ano          : 1943
autor        : Antoine de Saint-Exupéry
data_criacao : 2026-07-28 11:05:50.682143
id           : 8
titulo       : O Pequeno Príncipe

ano          : 1954
autor        : J.R.R. Tolkien
data_criacao : 2026-07-28 11:05:50.745931
id           : 15
titulo       : O Senhor dos Anéis: A Sociedade do Anel

ano          : 1938
autor        : Graciliano Ramos
data_criacao : 2026-07-28 11:05:50.755513
id           : 16
titulo       : Vidas Secas
```
