<?php
session_start();
?>

<section class="acaoL">
    <div class="acaoLo">
        <div class="acaoLog">
            <?php

            if (isset($_POST['email']) && !empty($_POST['email'])) {
                $email = $_POST['email'];
                $_SESSION['email'] = $email;
            } else {
                echo 'Ocorreu um erro ao tentar acessar a informação.';
                echo 'Por favor, tente novamente.';
                exit();
            }

            if (isset($_POST['senha']) && !empty($_POST['senha'])) {
                $senha = $_POST['senha'];
                $_SESSION['senha'] = $senha;
            } else {
                echo 'Ocorreu um erro ao tentar acessar a informação.';
                echo 'Por favor, tente novamente.';
                exit();
            }
            
            $login = login($email, $senha);

            if ($login == 1) {
                echo '
                <h1>Login realizado com sucesso!</h1>
                <a href="./index.php">Clique aqui para voltar para página principal</a>
                ';
            } else if ($login == 0) {
                echo '
                <h1>Email e/ou senha incorretos!</h1>
                <h4>Por favor, tente novamente.</h4>
                <a href="./index.php">Clique aqui para voltar para página principal</a>
                ';
            } else {
                include_once './index.php?page=erro';
            }

            ?>
        </div>
    </div>
</section>