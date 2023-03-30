<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <?php

    include_once './config/func.php';

    $msg = false;

    if (isset($_FILES['arquivo'])) {
        $d = 'upload/';
        $arq = basename($_FILES['arquivo']['name']);
        $darq = $d . $arq;
        $ext = pathinfo($darq, PATHINFO_EXTENSION);
        $nome = md5(uniqid($arq['name'])).".".$ext;
        move_uploaded_file($arq['tmp_name'], $darq);
        if(teste($nome) == 'True'){
          $msg = "Arquivo enviado com sucesso!";
        } else {
          $msg = "Falha ao enviar arquivo.";
        }
    }

    ?>

    <h1>TESTE - ENVIO DE ARQUIVO</h1>
    <?php
    
    if (isset($msg) && $msg != false) {
        echo "<p> $msg </p>";
    }
    
    ?>
    <br>
    <form action="teste.php" method="post" enctype="multipart/form-data">
        <label for="arquivo">Arquivo: </label><br>
        <input type="file" name="arquivo" id="arquivo">
        <br>
        <br>
        <input type="submit" value="Enviar">
    </form>

    <div align="center">
        
        <?php
        
        $imgs = pegar('tbteste');

        while ($img = mysqli_fetch_assoc($imgs)) {
        ?>

        <img src="./upload/<?php echo $data['nome']; ?>" alt="">

        <?php
        
        }
        
        ?>

    </div>

</body>

</html>