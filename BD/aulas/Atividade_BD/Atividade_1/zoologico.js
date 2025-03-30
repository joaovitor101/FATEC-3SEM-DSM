const { MongoClient } = require("mongodb");

async function main() {
    // Definir a URI de conexão com o MongoDB
    const uri = "mongodb://127.0.0.1:27017";
    
    // Criar instância do cliente MongoDB
    const client = new MongoClient(uri);

    try {
        await client.connect();
        console.log("Conectado ao MongoDB!");

        const database = client.db("zoo_db");
        const animais = database.collection("animais");

        // Inserindo todos os animais dentro da coleção animais
        await animais.insertMany([
            // Herbívoros
            { nome: "Luna", especie: "Arara-azul", idade: 4, dieta: "Herbívoro", habitat: "Floresta Tropical", vacinado: false },
            { nome: "Milo", especie: "Camelo", idade: 8, dieta: "Herbívoro", habitat: "Deserto", vacinado: false },

            
            // Carnívoros (Felinos)
            { nome: "Rex", especie: "Leão", idade: 10, dieta: "Carnívoro", habitat: "Savana", vacinado: false },
            { nome: "Zara", especie: "Leopardos", idade: 5, dieta: "Carnívoro", habitat: "Savana", vacinado: false },
        
            // Animais do deserto
            { nome: "Sahara", especie: "Camelo", idade: 6, dieta: "Herbívoro", habitat: "Deserto", vacinado: false },
            { nome: "Kalahari", especie: "Suricata", idade: 3, dieta: "Onívoro", habitat: "Deserto", vacinado: false },
        
            // Animais idosos (com mais de 15 anos)
            { nome: "Blaze", especie: "Águia-real", idade: 16, dieta: "Carnívoro", habitat: "Deserto", vacinado: false },
            { nome: "Cactus", especie: "Escorpião", idade: 17, dieta: "Carnívoro", habitat: "Deserto", vacinado: false }
        ]);
        
        
        console.log("Animais cadastrados!");

        // Consultas dos animais herbivoros 
        const herbivoros = await animais.find({ dieta: "Herbívoro" }).toArray();
        console.log("Herbívoros:", herbivoros);

        // Consulta dos animais do deserto
        const animaisDeserto = await animais.find({ habitat: "Deserto" }).toArray();
        console.log("Animais do deserto:", animaisDeserto);

        // Atualização de vacinação apenas dos felinos
        // await animais.updateMany(
        //     { especie: { $in: ["Leão", "Leopardos"] } },{ $set: { vacinado: true } }
        // );
        // console.log("Felinos vacinados!");

        // Removendo animais com mais de 15 anos
        // await animais.deleteMany({ idade: { $gt: 15 } });
        // console.log("Animais idosos removidos!");

    } finally {
        await client.close();
        console.log("Conexão fechada.");
    }
}
/*

comandos no cmd:
mongosh
use zoo_db
show collections
db.animais.find()
db.animais.find({ dieta: "Herbívoro" })
db.animais.find({ habitat: "Deserto" })
db.animais.updateMany({ especie: { $in: ["Leão", "Leopardos"] } }, { $set: { vacinado: true } })
db.animais.deleteMany({ idade: { $gt: 15 } })
*/
// Rodar a função principal
main().catch(console.error);
