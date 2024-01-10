# ping-maquinas

Esse script em python tem como objetivo pingar em varias maquinas, facilitando quem tem um grande parque de maquinas para gerenciar.

Nele utilizamos algumas biblioteca do python como subprocess e csv.

O processo que o script realiza é ler um arquivo .txt que deve conter os IPs que vamos pingar um abaixo do outro, conforme o exemplo no arquivo ip.txt. Após a leitura, ele efetua o ping de apenas um único pacote e, em seguida, gera um arquivo relatorio-ip.csv com o resultado do ping, informando se a máquina está online ou offline.
