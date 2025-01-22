CREATE DATABASE Oficina;
USE Oficina;

-- Tabela Cliente
CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(15),
    endereco VARCHAR(255)
);

-- Tabela Veículo
CREATE TABLE Veiculo (
    id_veiculo INT PRIMARY KEY AUTO_INCREMENT,
    placa VARCHAR(10) UNIQUE NOT NULL,
    modelo VARCHAR(50),
    marca VARCHAR(50),
    ano YEAR,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Tabela Ordem de Serviço (OS)
CREATE TABLE OrdemServico (
    numero_os INT PRIMARY KEY AUTO_INCREMENT,
    data_emissao DATE NOT NULL,
    data_conclusao DATE,
    valor_total DECIMAL(10, 2),
    status ENUM('Aberto', 'Em Execução', 'Concluído'),
    id_veiculo INT,
    FOREIGN KEY (id_veiculo) REFERENCES Veiculo(id_veiculo)
);

-- Tabela Mecânico
CREATE TABLE Mecanico (
    id_mecanico INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255),
    especialidade VARCHAR(50)
);

-- Tabela Serviço
CREATE TABLE Servico (
    id_servico INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(255) NOT NULL,
    valor_mao_de_obra DECIMAL(10, 2)
);

-- Tabela Peça
CREATE TABLE Pecas (
    id_peca INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2)
);

-- Relacionamento OS e Mecânico
CREATE TABLE OS_Mecanico (
    id_mecanico INT,
    numero_os INT,
    PRIMARY KEY (id_mecanico, numero_os),
    FOREIGN KEY (id_mecanico) REFERENCES Mecanico(id_mecanico),
    FOREIGN KEY (numero_os) REFERENCES OrdemServico(numero_os)
);

-- Relacionamento OS e Serviço
CREATE TABLE OS_Servico (
    id_servico INT,
    numero_os INT,
    quantidade INT,
    PRIMARY KEY (id_servico, numero_os),
    FOREIGN KEY (id_servico) REFERENCES Servico(id_servico),
    FOREIGN KEY (numero_os) REFERENCES OrdemServico(numero_os)
);

-- Relacionamento OS e Peça
CREATE TABLE OS_Pecas (
    id_peca INT,
    numero_os INT,
    quantidade INT,
    PRIMARY KEY (id_peca, numero_os),
    FOREIGN KEY (id_peca) REFERENCES Pecas(id_peca),
    FOREIGN KEY (numero_os) REFERENCES OrdemServico(numero_os)
);
