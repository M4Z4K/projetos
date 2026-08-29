<?php
// FOR
$numParcelas = $_POST['numParcelas'];

if ($numParcelas > 1) {
    for ($parcela = 1; $parcela <= $numParcelas; $parcela++) {
        echo "Parcela $parcela de $numParcelas <br>";
    }
} else {
    echo "Pagamento à vista <br>";
}

// WHILE
$tentativa = 0;
$maxTentativas = 3;

while ($tentativa < $maxTentativa) {
    $sucesso = loginAutorizado($usuarioCorreto, $senhaCorreta);

    if ($sucesso){
        break;
    }

    $tentativa++;
}

if ($tentativa == $maxTentativa) {
    echo "Usuário bloqueado, tente novamente mais tarde.";
}

// DO-WHILE
do {
    $formaPagamento = selecaoFormaPagamento();  // Vamos supor que essa função apresenta as formas de pagamento e captura qual forma o cliente escolheu. 
    echo $carrinho . "<br>O Valor total da sua compra é de: $valorTotal <br> Forma de pagamento escolhida: $formaPagamento"; 
    $sucesso = processaPagamento($valorTotal, $formaPagamento); // Vamos supor que essa função tenta processar o pagamento conforme o valor e a forma de pagamento selecionada. 

} while ($sucesso == false);

// FOREACH
$carrinhoDeCompras = getCarrinhoArrayAssociativo(); // Vamos supor que essa função captura a lista associativa contendo os itens do carrinho de compra, no formato ["nome" => "Calculadora", "preco" => 11.5]

foreach ($carrinhoDeCompras as $produto) {
    echo "Produto: " . $produto["nome"] . " - Preço: " . $produto["preco"] . "<br>";
}

// FUNÇÃO NATIVA
$emailCliente = $_POST['emailCliente'];
$emailFormatado = strtolower($emailCliente);

// FUNÇÃO SEM RETORNO
function boasVindas($nome, $loja){
    echo "Olá $nome, seja bem-vindo(a) à $loja!";
}

boasVindas($nomeUsuario, $nomeLoja);

// FUNÇÃO COM RETORNO
function calcularValorTotal($carrinhoDeCompras) {
    $valorTotal = 0;
    foreach ($carrindoDeCompras as $produto) {
        $valorTotal += $produto["preco"]; 
    }
    return $valorTotal;
}
?>