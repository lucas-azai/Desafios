# Sistema de E-commerce - Modelagem Lógica de Banco de Dados

## Descrição do Projeto
Este projeto modela um banco de dados para gerenciar um sistema de e-commerce, incluindo clientes (Pessoa Fisica e Jurídica), produtos, pedidos, pagamentos e entregas.

## Estrutura do Banco
- **Cliente**: Informações dos clientes (PF ou PJ).
- **Conta**: Relacionada ao cliente, armazena saldo.
- **Produto**: Produtos disponíveis no e-commerce.
- **Pedido**: Registro de compras realizadas.
- **ItemPedido**: Produtos contidos em cada pedido.
- **Pagamento**: Registro de pagamentos feitos nos pedidos.
- **Entrega**: Controle de status e rastreamento de entregas.
- **FornecedorProduto**: Relação entre fornecedores e produtos.

## Queries SQL
- Consultas simples: `SELECT`, `WHERE`.
- Consultas avançadas: atributos derivados, filtros com `HAVING`, ordenações, e junções.
- Exemplos incluem: total gasto por cliente, pedidos por cliente, produtos com fornecedores, etc.

## Tecnologias Utilizadas
- MySQL para modelagem e execução do banco de dados.
- Git e GitHub para versionamento.
