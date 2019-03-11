Necessario pacote ply para rodar( http://www.dabeaz.com/ply/ )

Rode com os parametros desejados:

./test[0,1,2,3].sh <heuristic> <weight>

<heuristic>: naive, max, add, ff
<weight> heuristic weight (WA*)


### (0) debug

./test0.sh naive 0
./test0.sh max 1

### (1) busca n~
ao-informada

./test1.sh naive 0

### (2) busca WA* com h_add

./test2.sh add 1
./test2.sh add 3

### (3) busca WA* com h_ff

./test3.sh ff 1
./test3.sh ff 3