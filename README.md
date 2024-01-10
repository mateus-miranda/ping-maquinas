# ping-maquinas

Esse script em python tem como objetivo pingar em varias maquinas, facilitando quem tem um grande parque de maquinas para gerenciar.

Nele utilizamos algumas biblioteca do python como subprocess e csv.

O processo que o script faz é ler um arquivo .txt que deve ter os IP que vamos pingar um abaixo do outro conforme o exemplo no arquivo ip.txt, após ler ele efetua o ping de apenas um unico pacote e logo em seguida gera um  arquivo relatorio-ip.csv com o resultado do ping e informa se a maquina está online ou offline.
