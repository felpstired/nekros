<?php
ob_start();
if (isset($_SESSION['email']) && isset($_SESSION['senha'])){
    header("Location: index.php?page=log");
}
?>

<section class="login">
    <div class="loginf">
        <div class="lt">
            <img src="./css/img/DIVERSOS/locaad.png" class="limg" alt="">
            <h2>Login</h2>
        </div>
        <form name="login" id="login" action="index.php?page=logSucesso" method="post">
            <div>
                <label for="email">E-mail:</label><br>
                <input type="email" class="inpe" name="email" id="email" placeholder="Digite seu email" maxlength="45" required="required">
            </div>
            <br>
            <div>
                <label for="senha">Senha:</label><br>
                <input type="password" class="inps" name="senha" id="senha" placeholder="Digite sua senha" maxlength="45" required="required">
            </div>
            <br>
            <button name="btnlogin" id="btnlogin" type="submit">Fazer login</button>
        </form>
        <p>Não tem uma conta? <a href="index.php?page=cadastro">Faça seu cadastro!</a></p>
    </div>
    <!-- <div class="logint">
        <h1>Faça seu Login!</h1>
        <h3>Ao fazer o login, seu progresso no jogo voltará de onde parou!</h3>
    </div> -->
</section>