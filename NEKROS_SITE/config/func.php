<?php

function conectar() {
    try {
        $conn = new PDO('mysql:host=localhost; charset=utf8mb4; dbname=dbnekros' , 'root', '');
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
        echo "Erro ao conectar ao banco de dados:  " . $e->getMessage();
        die();
    }
    return $conn;
}

function usuario(){
    $conn = conectar();
    $lista = $conn->query('SELECT * FROM tbusuario;');
    $lista->execute();
    if ($lista->rowCount() > 0) {
        return $lista->fetchAll(PDO::FETCH_OBJ);
    } else {
        return 'A lista está vazia.';
    }
}

function idb($user, $email, $senha){
    $conn = conectar();
    $lista = $conn->query("INSERT INTO tbusuario (user, email, senha) VALUES ('$user','$email','$senha')");
    $lista->execute();
    if ($lista->rowCount() > 0) {
        return 'True';
    } else {
        return 'False';
    }
}

?>