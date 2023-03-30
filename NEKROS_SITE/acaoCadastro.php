<section class="acaoC">
    <div class="acaoCa">
        <div class="acaoCad">
            <?php
            
            if (isset($_POST['user']) && !empty($_POST['user'])) {
                $user = $_POST['user'];
            } else {
                echo 'Ocorreu um erro ao tentar acessar a informação.';
                echo 'Por favor, tente novamente.';
                exit();
            }

            if (isset($_POST['emailc']) && !empty($_POST['emailc'])) {
                $email = $_POST['emailc'];
            } else {
                echo 'Ocorreu um erro ao tentar acessar a informação.';
                echo 'Por favor, tente novamente.';
                exit();
            }

            if (isset($_POST['senhac']) && !empty($_POST['senhac'])) {
                $senha = $_POST['senhac'];
            } else {
                echo 'Ocorreu um erro ao tentar acessar a informação.';
                echo 'Por favor, tente novamente.';
                exit();
            }
            
            $ver = verificar($email);

            if ($ver != 1) {
                idb($user, $email, $senha);
                echo '
                    <h1>Cadastro realizado com sucesso!</h1>
                    <h4>Agora suas informações e seu progresso no jogo poderá ficar salvos!</h4>
                    <a href="./index.php">Clique aqui para voltar para página principal</a>
                ';
            } else {
                echo '
                    <h1>Não foi possível realizar o cadastro!</h1>
                    <h4>Já existe uma conta com esse e-mail cadastrado no nosso site!</h4>
                    <h4>Tente novamente com outros dados!</h4>
                    <a href="./index.php?page=cadastro">Clique aqui para voltar para página de cadastro</a>
                ';
            }
            
            ?>
        </div>
    </div>
</section>