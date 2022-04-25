# ACMEVita

Projeto de modelagem de dados e criação de uma API utilizando Python e Flask.

## Sobre o projeto

A ACMEVita está expandindo seus negócios e precisa de um sistema para gerenciar seus departamentos, colaboradores e dependentes.

O seu único desenvolvedor backend está de ferias, você foi recrutado para finalizar este projeto, boa sorte!

### Requisitos

#### Como um Usuário da API eu gostaria de consultar todos os departamentos para visualizar a organização da ACMEVita.

* Cada departamento deve possuir um *nome do departamento*.
* A API deve responder com uma listagem de departamentos no formato JSON informando o *nome do departamento* de cada departamento.

#### Como um Usuário da API eu gostaria de consultar todos os colaboradores de um departamento para visualizar a organização da ACMEVita.

* Cada colaborador deve possuir um *nome completo*.
* Cada colaborador deve pertencer a *um* departamento.
* Cada colaborador pode possuir *nenhum, um ou mais* dependententes.
* A API deve responder com uma listagem de colaboradores do departamento no formato JSON informando o *nome completo* de cada colaborador e a respectiva flag booleana `have_dependents` caso o colaborador possua *um ou mais dependentes*.
