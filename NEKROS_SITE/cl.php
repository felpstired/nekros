<section class="cl">
    <div class="login">
        <h2>Login</h2>
        <form name="login" id="login" action="" method="post">
            <div>
                <label for="email">E-mail:</label><br>
                <input type="email" class="inpe" name="email" id="email" placeholder="Digite seu email" maxlength="44">
            </div>
            <br>
            <div>
                <label for="senha">Senha:</label><br>
                <input type="password" class="inps" name="senha" id="senha" placeholder="Digite sua senha" maxlength="44">
            </div>
            <br>
            <button name="btnlogin" id="btnlogin" type="submit">Enviar</button>
        </form>
    </div>
    <div class="cadastro">
        <h2>Cadastro</h2>
        <form name="cadastro" id="cadastro" action="" method="post">
            <div>
                <label for="user">Usuário:</label><br>
                <input type="text" class="inpu" name="user" id="user" placeholder="Digite um nome de usuário" maxlength="24">
            </div>
            <br>
            <div>
                <label for="emailc">E-mail:</label><br>
                <input type="email" class="inpe" name="emailc" id="emailc" placeholder="Digite um email" maxlength="44">
            </div>
            <br>
            <div>
                <label for="senhac">Senha:</label><br>
                <input type="password" class="inps" name="senhac" id="senhac" placeholder="Digite uma senha" maxlength="44">
            </div>
            <br>
            <button name="btncadastro" id="btncadastro" type="submit">Enviar</button>
        </form>
    </div>
</section>







<?php

echo 'pagina de cadastro ou login';

?>