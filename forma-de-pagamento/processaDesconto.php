<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["txtNome"];
    $valorCompra = $_POST["txtValorCompra"];
    $formaPagamento = $_POST["cmbPag"];
    $desconto = 0;

    if ($formaPagamento == "cartaoCredito") {
        $desconto = 0;
        $mensagem = "Olá $nome, sua compra de " . sprintf("R$ %.2f",$valorCompra) . " foi realizada com cartão de crédito. Não há desconto.";
    } elseif ($formaPagamento == "boleto") {
        $desconto = $valorCompra * 0.08;
        $mensagem = "Olá $nome, sua compra de " . sprintf("R$ %.2f",$valorCompra) . " foi realizada com boleto. Seu desconto é " . sprintf("R$ %.2f", $desconto). ".";
    } elseif ($formaPagamento == "deposito") {
        $desconto = $valorCompra * 0.1;
        $mensagem = "Olá $nome, sua compra " . sprintf("R$ %.2f",$valorCompra) . " foi realizada com depósito. Seu desconto é de " . sprintf("R$ %.2f", $desconto). ".";
    } else {
        $mensagem = "Forma de pagamento inválida.";
    }

    $descontoAplicado = $valorCompra - $desconto; 
    echo "<!DOCTYPE html>
    <html lang='pt-BR'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Resultado do desconto</title>
        <link rel='stylesheet' href='w3.css'>
        <link rel='stylesheet' href='style.css'>
    </head>
    <body>
        <main class='resultado w3-panel'>
            $mensagem<br>
            <strong>Valor Total: " . sprintf("R$ %.2f", $descontoAplicado) . ".</strong>
        </main>
    </body>
    </html>";
}
?>

<!-- Comentário Reflexivo - Etapas do raciocínio lógico para desenvolvimento do projeto proposto na Agenda. 
    1) Avaliação do código e dos erros presentes no mesmo (cálculos trocados/mensagem faltando);
    2) Correção dos erros dos cálculos do desconto e criação da variavel "descontoAplicado" para exibir a mensagem com o valor total já com desconto aplicado;
    3) Desenvolvimento do formulário somente em HTML (utilizando o formulário da agenda anterior como base para os campos nome, valor, pagamento e enviar);
    4) Inclusão da tag "<select>" para seleção da forma de pagamento;
    5) Testes no localhost para confirmar a corretude da lógica;
    6) Inclusão do comando "sprintf" para que a impressão concatene esse comando e exiba os valores em reais com duas casas decimais;
    7) Desenvolvimento da identidade visual da empresa Madeira & Cia jutamente com o GitHub Copilot. (Identidade Madeira e CIA em tons marrom alaranjado e branco. Visual simples, tradicional e nostálgico.);
    8) Escrita do CSS em uma página externa utilizando o framework w3.css.   

Desenvolvido por: Victor Hugo Almeida dos Santos, Turma FOS -->
