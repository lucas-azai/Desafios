# Desafio de Banco de Dados - Sistema de Pedidos

## Descrição do Projeto
Este projeto é uma solução para o desafio de modelagem de banco de dados, que propõe a criação de um sistema de gerenciamento de pedidos com as seguintes caracteristicas:
- Clientes podem ser **Pessoa Fisica (PF)** ou **Pessoa Juridica (PJ)**.
- Contas estão associadas a clientes e são exclusivas.
- Pedidos possuem múltiplas formas de pagamento.
- Entregas têm status e código de rastreamento.

## Estrutura do Banco de Dados
A modelagem considera:
- **Cliente**: Representa Pessoa Fisica ou Juridica.
- **Conta**: Associada a um cliente, controla o saldo.
- **Pedido**: Contem informações sobre compras realizadas.
- **FormaPagamento**: Métodos de pagamento disponíveis.
- **PedidoPagamento**: Relaciona pedidos e formas de pagamento.
- **Entrega**: Gerencia informações logísticas.

## Tecnologias Utilizadas
- MySQL para modelagem e estruturação.
- GitHub para versionamento e apresentação.

## Como Utilizar
1. Clone o repositório.
2. Execute o script SQL para criar o banco de dados.
3. Integre com uma aplicação ou insira dados diretamente para testes.

## Próximos Passos
- Implementar uma API para interação com o banco de dados.
- Desenvolver interface para usuários finais.
