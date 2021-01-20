<?php
#Mostrar valor
if (isset($_POST["entrada1"])) {
    print($_POST["entrada1"]);
}
?>

<!--Form para input-->
<form method="POST">
    <input type="hidden" name="entrada1"/ value="entrada">
    <button type="submit" onclick="return myFunction1()">Mostrar valor</button>
</form>
<form method="POST">
    <input type="hidden" name="entrada2"/>
    <button type="submit" onclick="return myFunction2()">Apagar valor</button>
</form>

<!--Script para confirmar entrada, o confirm retorna um true e false durante a operacao-->
<script>
function myFunction1() {
    return window.confirm("decisao");
}
function myFunction2() {
    return window.confirm("decisao");
}
</script>