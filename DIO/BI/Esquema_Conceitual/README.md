# Sistema de Gestão de Oficinas Mecânicas

## Descrição do Projeto
Este projeto propõe a modelagem de um banco de dados para controle e gerenciamento de ordens de serviço (OS) em oficinas mecânicas. O sistema permite o cadastro de clientes, veículos, mecânicos, serviços e peças. Ele controla todas as etapas, desde o registro da OS até a execução e conclusão do trabalho.

## Estrutura do Banco
- **Cliente**: Informações dos clientes que utilizam os serviços da oficina.
- **Veículo**: Veículos dos clientes que passam por reparos ou revisões.
- **Ordem de Serviço (OS)**: Dados sobre os serviços executados, incluindo status e valor total.
- **Mecânico**: Registro dos mecânicos e suas especialidades.
- **Serviço**: Descrição dos serviços disponíveis e seus valores de mão de obra.
- **Peça**: Peças utilizadas nos reparos, com preços.

## Relacionamentos
- Clientes possuem vários veículos.
- Veículos têm várias ordens de serviço.
- Cada OS é atribuída a uma equipe de mecânicos e inclui serviços e peças.

## Tecnologias Utilizadas
- **Banco de Dados Relacional**: MySQL
- **Ferramentas de Versionamento**: Git e GitHub

## Como Utilizar
1. Clone o repositório.
2. Execute o script SQL fornecido.
3. Utilize um sistema de interface (ou comandos SQL) para realizar testes.

## Próximos Passos
- Criar uma aplicação para interação com o banco de dados.
- Adicionar relatórios de desempenho dos mecânicos e veículos atendidos.
