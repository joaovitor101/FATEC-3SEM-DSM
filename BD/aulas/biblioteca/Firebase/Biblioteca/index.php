<?php
require_once 'vendor/autoload.php';

use Krait\Firebase\Factory;

class FirebaseCRUD{
    private $datebase;

    public function __construct(){
        $firebase = (new Factory)
        ->withServiceAccount(__DIR__ .'/private_key.json')
        ->withDataBaseUri('https://biblioteca-dsm3-89bc0-default-rtdb.firebaseio.com/')
        ->createDataBase();

        $this->datebase = $firebase;
    }

    public function create($livro){
        $ref = $this->database->getReference('livros');
        $ref->push($livro);
    }

    public function read(){
        $ref = $this->database->getReference('livros');
        $livros = $ref ->getValue();
    }

    public function update($id, $livros){
        $ref = $this->database->getReference('livros');
        $ref->set($livro)
    }

    public function delete(){
        $ref = $this->database->getReference('livros/$id');
        $ref->remove();

    }

    $firebaseCRUD->create({
        'titulo' => '1984',
        'autor'=> 'George Orwell',
        'ano'=> '1948',
        'genero'=> ''

    })
}