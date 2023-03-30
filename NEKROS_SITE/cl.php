<section class="cl">
    <div class="login">
        <h2>Login</h2>
        <form name="login" id="login" action="" method="post">
            <div>
                <label for="email">E-mail:</label><br>
                <input type="email" class="inpe" name="email" id="email" placeholder="Digite seu email">
            </div>
            <br>
            <div>
                <label for="senha">Senha:</label><br>
                <input type="password" class="inps" name="senha" id="senha" placeholder="Digite sua senha">
            </div>
            <br>
            <button name="btnlogin" id="btnlogin" type="submit">Enviar</button>
        </form>
    </div>
    <div class="cadastro">
        <h2>Cadastro</h2>
        <form name="cadastro" id="cadastro" action="" method="post">
            <div>
                <label for="nome">Usuário:</label><br>
                <input type="text" class="inpu" name="user" id="" placeholder="Digite um nome de usuário">
            </div>
            <br>
            <div>
                <label for="email">E-mail:</label><br>
                <input type="email" class="inpe" name="email" id="email" placeholder="Digite um email">
            </div>
            <br>
            <div>
                <label for="senha">Senha:</label><br>
                <input type="password" class="inps" name="senha" id="senha" placeholder="Digite uma senha">
            </div>
            <br>
            <button name="btncadastro" id="btncadastro" type="submit">Enviar</button>
        </form>
    </div>
</section>







<?php

echo 'pagina de cadastro ou login';

?>