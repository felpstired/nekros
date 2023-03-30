<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,200;0,400;0,700;1,200;1,400;1,700&display=swap" rel="stylesheet">
    <title>Home | Projeto</title>
</head>
<body>
    <script>
        function menu() {
            document.getElementById("dropa").classList.toggle("show");
        }

        window.onclick = function(event) {
            if (!event.target.matches('.menu')) {
                var dropdowns = document.getElementsByClassName("dropa");
                var i;
                for (i = 0; i < dropdowns.length; i++) {
                    var openDropdown = dropdowns[i];
                    if (openDropdown.classList.contains('show')) {
                        openDropdown.classList.remove('show');
                    }
                }
            }
        }
    </script>
    <section id="header">
        <nav class="navb">
            <div>
                <a href="#"><img class="logo" src="./img/logo.jpg" alt=""></a>
                <!-- <img src="./img/logo.jpg" alt=""> -->
            </div>
            <ul class="navl">
                <li class="litem"><a href="index.php?page=home">Home</a></li>
                <li class="litem"><a href="index.php?page=sin">Sinopse</a></li>
                <li class="litem"><a href="index.php?page=cl">Cadastro / Login</a></li>
                <li class="litem">
                    <div class="drop">
                        <button onclick="menu()" class="menu">☰</button>
                        <div class="dropa" id="dropa">
                            <a href="">Galeria de Personagens</a>
                            <hr>
                            <a href="">Galeria de Backgrounds</a>
                            <hr>
                            <a href="">Galeria de BGM</a>
                            <hr>
                            <a href="">Processo Criativo</a>
                            <hr>
                            <a href="">Desenvolvedores</a>
                        </div>
                    </div>
                </li>
            </ul>
        </nav>
    </section>
    <section>
        <div class="corpo">
        <?php
    
        include_once './func/func.php';

        if(isset($_GET['page']) && !empty($_GET['page'])){
            $sp = $_GET['page'];
            if($sp == 'home'){
                include_once './index.php';
            } else if($sp == 'sin'){
                include_once './sin.php';
            } else if($sp == 'cl'){
                include_once './cl.php';
            }else {
                echo 'Essa página não existe!';
            }
        } else {
            echo 'Favor clicar em algum menu!';
        }
        
        ?>
        </div>
    </section>
    <section class="footer">
        <p>- © Copyright 2023 Minerva Games Limited -</p>
        <br>
        <p>- Todos os direitos reservados -</p>
    </section>
</body>
</html>