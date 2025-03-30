const { MongoClient } = require("mongodb");

//para executar um de cada vez comente as operações que não queremos executar

async function main() {
    // Conectar ao MongoDB (Local)
    const uri = "mongodb://127.0.0.1:27017";
    const client = new MongoClient(uri);

    try {
        await client.connect();
        console.log("Conectado ao MongoDB!");


        const database = client.db("space_db");
        const naves = database.collection("naves");

        // Cadastrar naves
        await naves.insertMany([
            { nome: "Patricio AmongUs", tipo: "exploração", capacidadeTripulantes: 6, emMissao: true },
            { nome: "Colossus", tipo: "carga", capacidadeTripulantes: 3, emMissao: false },
            { nome: "Vingador Estelar", tipo: "combate", capacidadeTripulantes: 8, emMissao: true },
            { nome: "Falcão Cósmico", tipo: "carga", capacidadeTripulantes: 2, emMissao: true }
        ]);
        console.log("Naves cadastradas!");

        // Listar todas as naves que estão em missão
        // const emMissao = await naves.find({ emMissao: true }).toArray();
        // console.log("Naves em missão:", emMissao);

        // // Encontrar naves com mais de 5 tripulantes
        // const grandes = await naves.find({ capacidadeTripulantes: { $gt: 5 } }).toArray();
        // console.log("Naves com mais de 5 tripulantes:", grandes);

        
        // // Desativar todas as naves de carga 
        // await naves.updateMany({ tipo: "carga" }, { $set: { emMissao: false } });
        // console.log("Todas as naves de carga foram desativadas");

        // // Remover naves com capacidade menor que 3 tripulantes
        // await naves.deleteMany({ capacidadeTripulantes: { $lt: 3 } });
        // console.log("Naves obsoletas removidas");

    } finally {
        await client.close();
        console.log("Conexão fechada.");
    }
}
/*
comandos no cmd:
mongosh
use space_db
show collections
db.naves.find() Listar todas as naves
db.naves.find({ emMissao: true })  Listar naves em missão
db.naves.find({ capacidadeTripulantes: { $gt: 5 } })  Naves com mais de 5 tripulantes
db.naves.updateMany({ tipo: "carga" }, { $set: { emMissao: false } })  Desativar naves de carga
db.naves.deleteMany({ capacidadeTripulantes: { $lt: 3 } })  Remover naves obsoletas
*/

main().catch(console.error);
