//Importar o MongoClient

const {MongoClient} = require("mongodb")
async function main() {
    //Definir a URI de conexão com o MongoDb
    const uri = "mongodb://127.0.0.1:27017"
    //Criar instância do cliente MongoDB
    const client = new MongoClient(uri);

    try{
        await client.connect();
        const database = client.db("biblioteca-aula");
        //selecionar coleção "livros"
        const livros = database.collection("livros"); 

        /*
        await livros.insertMany([
            {"titulo": "1984", "autor": "George Orwell", "ano": "1949", "genero": "Distopia"},
            {"titulo":"Dom Casmurro", "autor": "Machado de Assis", "ano": "1899", "genero": "Romance"},
            {"titulo": "Senhor Dos Aneis", "autor": "J.R.R Tolkei", "ano":"1954", "genero": "Fantasia"},
        ]);
        

        // Consulta todos os documentos da coleção
        const todosLivros = await livros.find({}).toArray();
        console.log("Livros:",todosLivros);

        //Atualizar documento
        await livros.updateOne({"titulo":"1984"}, {$set:{"ano":"1950"}});
     

        //Deletar documento
        await livros.deleteOne({"titulo":"Dom Casmurro"});
        */
    }finally{
        await client.close();
    }
}
main().catch(console.error);



