<?php

$nomeCandidato = $_POST['nomeCandidato'];
$idadeCandidato = $_POST['idadeCandidato'];
$profissaoCandidato = $_POST['profissaoCandidato'];
$pretensaoCandidato = $_POST['pretensaoCandidato'];
$experienciaCandidato = $_POST['experienciaCandidato'];

echo "<strong>Ficha do Candidato:</strong><br><br>";

echo "Nome completo: $nomeCandidato<br>";
echo "Idade: $idadeCandidato<br>";
echo "Profissão: $profissaoCandidato<br>";
echo "Pretensão salarial: $pretensaoCandidato<br>";
echo "Experiência profissional: $experienciaCandidato<br><br>";

$mensagem = "O candidato " . $nomeCandidato;
$mensagem .= " cuja profissão é " . $profissaoCandidato;
$mensagem .= " tem como experiência profissional " . $experienciaCandidato;

echo $mensagem;
?>
<br>
<br>
Clique <a href="cadastro.html"><strong>aqui</strong></a> para voltar ao formulário.