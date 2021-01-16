<?php
#Ponteiros em php
$a = 1;
$b = $a;
$a = 2;
$c = &$a;

#Demonstrando os ponteiros
$d = [$a, $b, $c];
var_dump($d);
?>