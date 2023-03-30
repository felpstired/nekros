<section class="acaoL">
    <div class="acaoLo">
        <div class="acaoLog">
            <?php
            ob_start();

            if (isset($_POST['email']) && !empty($_POST['email'])) {
                $email = $_POST['email'];
            } else {
                echo 'Ocorreu um erro ao tentar acessar a informação.';
                echo 'Por favor, tente novamente.';
                exit();
            }

            if (isset($_POST['senha']) && !empty($_POST['senha'])) {
                $senha = $_POST['senha'];
            } else {
                echo 'Ocorreu um erro ao tentar acessar a informação.';
                echo 'Por favor, tente novamente.';
                exit();
            }
            
            $login = login($email, $senha);

            if ($login == 1) {
                $_SESSION['email'] = $email;
                $_SESSION['senha'] = $senha;
                echo '
                <h1>Login realizado com sucesso!</h1>
                <h4>Você será redirecionado para página principal.</h4>
                ';
                header("refresh:3; url=index.php");
            } else if ($login == 0) {
                echo '
                <h1>Email e/ou senha incorretos OU inexistentes!</h1>
                <h4>Por favor, tente novamente.</h4>
                <a href="./index.php?page=login">Clique aqui para voltar para página de login</a>
                ';
            } else {
                include_once './index.php?page=erro';
            }

            ?>
        </div>
    </div>
</section>