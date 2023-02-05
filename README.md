# Detection of unknown attacks

Este projeto visa replicar, analisar e construir um IDS (intrusion detection systems) baseados em ataques desconhecidos.
Para isto utilizaremos a base de dados referente ao problema [Intrusion Detection Evaluation Dataset](https://www.unb.ca/cic/datasets/ids-2017.html)

## Orientações gerais

Para criarmos um projeto reproduzível, vamos utilizar um ambiente [docker](https://docs.docker.com/engine/install/ubuntu/) em conjunto com o
[MAKEFILE](https://terminalroot.com.br/2019/12/como-criar-um-makefile.html)

### Ambiente desenvolvimento

Para o ambiente de desenvolvimento vamos utilizar [Jupyter Notebook](https://jupyter.org) para melhor visualização das informações e gráficos.

### Instalação de pacotes

Existe um arquivo chamado `setup.py` nele estarão os pacotes com as versões utilizadas.

É muito importante quando for instalar um novo pacote, adiciona-lo neste script e buildar a imagem novamente para garantirmos a reprodutibilidade do projeto e
garantir que todos estao usando a mesma versão do ambiente.

### MAKEFILE

Utilizaremos o makefile para buildar e executar o ambiente de desenvolvimente. É bastante importante verificar se a imagem está atualizada.

#### Buildar a imagem docker

```
$ make build
```

#### Criar um conteiner com a imagem docker

```
$ make dev
```

#### Rodar os comandos sem o makefile

Dentro do arquivo makefile existem os comandos para serem rodados diretamente `docker run ...` ou `docker build ... `.

## Boas práticas gitlab

Para evitar problemas é sempre bom criar uma branch de trabalho a partir da master e ao final abrir um merge Request para as pessoas validadarem e por fim
aprovarem para fazer o merge para a master

É bastante importante evitar o dar push diretamente na master, pois podem ocorrer erros e acabar quebrando o que outros estão fazendo.
Segue uma referencia do [github](https://guides.github.com/introduction/flow/). Neste caso o pull request(github) é o mesmo que o merge request(gitlab)

## Referencias para análises

O site [kaggle](www.kaggle.com), que é um site de competições envolvendo machine learning e também para aprendizado, possui diversos problemas já resolvidos como o
[titanic](https://www.kaggle.com/startupsci/titanic-data-science-solutions).
Neste é feita uma serie de análises até o modelo final, pode servir como uma boa base para começar os estudos.

Existem também um [trello de data science](https://trello.com/b/rbpEfMld/data-science) que lista diversas referencias para aprender sobre data science como R, python,
spark e outros.


