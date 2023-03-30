<section class="acaoL">
    <div class="acaoLo">
        <div class="acaoLog">
            <?php

            $listau = usuario();

            if (isset($_POST['email']) && !empty($_POST['email'])) {
                $email = $_POST['email'];
                foreach ($listau as $itemlinha){
                    if ($email == $itemlinha->email) {
                        if (isset($_POST['senha']) && !empty($_POST['senha'])) {
                            $senha = $_POST['senha'];
                            if ($senha == $itemlinha->senha) {
                                echo 'logado';
                            } else {
                                echo 'email e/ou senha incorretos';
                                exit();
                            }
                        } else {
                            echo 'senha não inserida';
                            exit();
                        }
                    } else {
                        echo 'email e/ou senha incorretos';
                        exit();
                    }
                }
                
            } else {
                echo 'Ocorreu um erro ao tentar acessar a informação.';
                echo 'Por favor, tente novamente.';
                exit();
            }
            
            ?>
        </div>
    </div>
</section>