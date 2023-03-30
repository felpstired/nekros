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

            idb($user, $email, $senha);

            echo '
                <h1>Cadastro realizado com sucesso!</h1>
                <h4>Agora suas informações e seu progresso no jogo poderá ficar salvos!</h4>
                <a href="./index.php">Clique aqui para voltar para página principal</a>
            ';
            
            ?>
        </div>
    </div>
</section>