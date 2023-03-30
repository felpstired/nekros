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
    <link href="https://fonts.googleapis.com/css2?family=Butcherman&family=Eater&display=swap" rel="stylesheet">
    <title>Home | Nekrós</title>
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
    <div class="body">
    <section id="header">
        <nav class="navb">
            <div>
                <a href="index.php"><img class="logo" src="./img/logo.jpg" alt=""></a>
                <!-- <img src="./img/logo.jpg" alt=""> -->
            </div>
            <ul class="navl">
                <li class="litem"><a href="index.php">Home</a></li>
                <li class="litem"><a href="index.php?page=sinopse">Sinopse</a></li>
                <!-- <li class="litem"><a href="index.php?page=cl">Cadastro / Login</a></li> -->
                <li class="litem"><a href="index.php?page=login">Login</a></li>
                <li class="litem">
                    <div class="drop">
                        <button onclick="menu()" class="menu">☰</button>
                        <div class="dropa" id="dropa">
                            <a href="index.php?page=personagens">Galeria de Personagens</a>
                            <hr>
                            <a href="index.php?page=backgrounds">Galeria de Backgrounds</a>
                            <hr>
                            <a href="index.php?page=bgm">Galeria de BGM</a>
                            <hr>
                            <a href="index.php?page=processo_criativo">Processo Criativo</a>
                            <hr>
                            <a href="index.php?page=devs">Desenvolvedores</a>
                        </div>
                    </div>
                </li>
            </ul>
        </nav>
    </section>
    <section class="corp">
        <div class="corpo">
        <?php
    
        include_once './func/func.php';

        if(isset($_GET['page']) && !empty($_GET['page'])){
            $sp = $_GET['page'];
            if($sp == ''){
                include_once './erro.php';
            } else if($sp == 'sinopse'){
                include_once './sin.php';
            } /* else if($sp == 'cl'){
                include_once './cl.php';
            } */ else if($sp == 'personagens'){
                include_once './glp.php';
            } else if($sp == 'backgrounds'){
                include_once './glbg.php';
            } else if($sp == 'bgm'){
                include_once './glbgm.php';
            } else if($sp == 'processo_criativo'){
                include_once './pc.php';
            } else if($sp == 'devs'){
                include_once './dev.php';
            } else if($sp == 'login'){
                include_once './login.php';
            } else if($sp == 'cadastro'){
                include_once './cadastro.php';
            } else {
                include_once './erro.php';
            }
        } else {
            include_once './home.php';
        }
        
        ?>
        </div>
    </section>
    <section class="footer">
        <p>- Todos os direitos reservados -</p>
        <p>- © Copyright 2023 Minerva Games Limited -</p>
    </section>
    </div>
</body>
</html>