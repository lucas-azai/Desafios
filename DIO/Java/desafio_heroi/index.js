// Definindo o nome 
let nomeDoHeroi = "Azai";
let experienciaDoHeroi = 6000; 

// Verificação do nível 
let nivelDoHeroi;

switch (true) {
    case experienciaDoHeroi < 1000:
        nivelDoHeroi = "Ferro";
        break;
    case experienciaDoHeroi >= 1001 && experienciaDoHeroi <= 2000:
        nivelDoHeroi = "Bronze";
        break;
    case experienciaDoHeroi >= 2001 && experienciaDoHeroi <= 5000:
        nivelDoHeroi = "Prata";
        break;
    case experienciaDoHeroi >= 5001 && experienciaDoHeroi <= 7000:
        nivelDoHeroi = "Ouro";
        break;
    case experienciaDoHeroi >= 7001 && experienciaDoHeroi <= 8000:
        nivelDoHeroi = "Platina";
        break;
    case experienciaDoHeroi >= 8001 && experienciaDoHeroi <= 9000:
        nivelDoHeroi = "Ascendente";
        break;
    case experienciaDoHeroi >= 9001 && experienciaDoHeroi <= 10000:
        nivelDoHeroi = "Imortal";
        break;
    default:
        nivelDoHeroi = "Radiante";
}

// Saida
console.log(`O Herói de nome ${nomeDoHeroi} está no nível de ${nivelDoHeroi}`);