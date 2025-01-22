-- Recuperações simples com SELECT Statement

-- Lista todos os clientes
SELECT * FROM Cliente;

-- Lista todas as ordens de serviço
SELECT numero_os, data_emissao, status, valor_total FROM OrdemServico;


--  Filtros com WHERE Statement

-- Busca clientes com telefone preenchido
SELECT nome, telefone FROM Cliente WHERE telefone IS NOT NULL;

-- Busca ordens de serviço com status "Aberto"
SELECT * FROM OrdemServico WHERE status = 'Aberto';

-- Atributos derivados

-- Calcula o valor total de servicos de uma OS
SELECT numero_os, SUM(valor_mao_de_obra * quantidade) AS valor_servicos
FROM OS_Servico
JOIN Servico ON OS_Servico.id_servico = Servico.id_servico
GROUP BY numero_os;


-- Ordenações com ORDER BY

-- Lista ordens de serviço ordenadas pela data de emissão
SELECT * FROM OrdemServico ORDER BY data_emissao DESC;

-- Lista mecanicos ordenados por especialidade
SELECT * FROM Mecanico ORDER BY especialidade;


-- Filtros com HAVING Statement

-- Exibe OS com valor total maior que 1000
SELECT numero_os, SUM(valor_mao_de_obra * quantidade) AS valor_servicos
FROM OS_Servico
JOIN Servico ON OS_Servico.id_servico = Servico.id_servico
GROUP BY numero_os
HAVING valor_servicos > 1000;


-- Junções entre tabelas

-- Recupera informações de cliente e veículo
SELECT Cliente.nome, Veiculo.placa, Veiculo.modelo
FROM Cliente
JOIN Veiculo ON Cliente.id_cliente = Veiculo.id_cliente;

-- Recupera mecanicos associados a uma OS específica
SELECT OrdemServico.numero_os, Mecanico.nome, Mecanico.especialidade
FROM OS_Mecanico
JOIN OrdemServico ON OS_Mecanico.numero_os = OrdemServico.numero_os
JOIN Mecanico ON OS_Mecanico.id_mecanico = Mecanico.id_mecanico
WHERE OrdemServico.numero_os = 1;



