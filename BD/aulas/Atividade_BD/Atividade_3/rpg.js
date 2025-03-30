const { MongoClient } = require("mongodb");

async function main() {
    const uri = "mongodb://127.0.0.1:27017";
    const client = new MongoClient(uri);

    try {
        await client.connect();
        console.log("Conectado ao MongoDB!");

        const database = client.db("rpg_db");
        const personagens = database.collection("personagens");
 
            await personagens.insertMany([
                { nome: "Jacobo Fogo", classe: "mago", nivel: 12, habilidades: ["bola de fogo", "invisibilidade"], vida: 100 },
                { nome: "Borin Pedraqueixo", classe: "guerreiro", nivel: 15, habilidades: ["golpe de machado", "grito de guerra"], vida: 150 },
                { nome: "Eldrin Sombralis", classe: "arqueiro", nivel: 8, habilidades: ["disparo sombrio", "visão aguçada"], vida: 80 },
                { nome: "Thalion Aster", classe: "mago", nivel: 18, habilidades: ["tempestade arcana", "barreira mágica"], vida: 120 },
                { nome: "Kara Valente", classe: "guerreiro", nivel: 10, habilidades: ["escudo impenetrável", "corte veloz"], vida: 170 },
                { nome: "Seraphina Luz", classe: "curandeiro", nivel: 5, habilidades: ["cura divina", "proteção sagrada"], vida: 50 }
            ]);
            console.log("Personagens cadastrados");
        

        // Listar personagens com nível superior a 10
        const nivelAlto = await personagens.find({ nivel: { $gt: 10 } }).toArray();
        console.log("Personagens acima do nível 10:", nivelAlto);

        // Encontrar guerreiros disponíveis para uma missão urgente
        const guerreiros = await personagens.find({ classe: "guerreiro" }).toArray();
        console.log("Guerreiros disponíveis:", guerreiros);

        // Aumentar a vida de todos os guerreiros para 200
        // await personagens.updateMany({ classe: "guerreiro" }, { $set: { vida: 200 } });
        // console.log("Vida dos guerreiros aumentada para 200!");

        // // Remover personagens com vida menor que 30 (derrotados)
        // await personagens.deleteMany({ vida: { $lt: 30 } });
        // console.log("Personagens com vida menor que 30 foram removidos.");

    } finally {
        await client.close();
        console.log("Conexão fechada.");
    }
}
/*
comandos no cmd:
mongosh
use rpg_db
show collections
db.personagens.find()  # Listar todos os personagens
db.personagens.find({ nivel: { $gt: 10 } })  # Listar personagens com nível maior que 10
db.personagens.find({ classe: "guerreiro" })  # Encontrar guerreiros disponíveis
db.personagens.updateMany({ classe: "guerreiro" }, { $set: { vida: 200 } })  # Aumentar a vida dos guerreiros
db.personagens.deleteMany({ vida: { $lt: 30 } })  # Remover personagens derrotados

*/
// Rodar a função principal
main().catch(console.error);
