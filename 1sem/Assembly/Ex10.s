.data
gran:.asciiz"Digite um numero grande: "
ze:.asciiz"Proibida a divisao por 0\n"
peq:.asciiz"Digite um numero menor: "
res:.asciiz"Total: "
n:.asciiz"\n"
.text

main:
li $v0,4
la $a0,gran
syscall
li $v0,5
syscall
add $t1,$v0,$zero
beqz $t1,novot1

li $v0,4
la $a0,peq
syscall
li $v0,5
syscall
add $t2,$v0,$zero
beqz $t2,novot2

continua:
bgt $t2,$t1,troca
j dividir

j fim

troca:
add $t3,$t1,$zero   # t3 = t1
add $t1,$t2,$zero   # t1 = t2
add $t2,$t3,$zero   # t2 = t3
j continua

dividir:
# falta esse pedaço
div $t0,$t1,$t2

novot1:
li $v0,4
la $a0,ze
syscall
li $v0,4
la $a0,gran
syscall
li $v0,1
syscall
add $t1,$v0,$zero
beqz $t1,novot1
j continua

novot2:
li $v0,4
la $a0,ze
syscall
li $v0,4
la $a0,peq
syscall
li $v0,1
syscall
add $t2,$v0,$zero
beqz $t2,novot2
j continua

fim:
