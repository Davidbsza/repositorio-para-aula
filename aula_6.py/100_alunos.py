"""Uma escola está organizando sua primeira olimpíada do conhecimento e deseja separar, 
os 100 alunos em dois grupos de 50. Além de testar os conhecimentos dos alunos, querem 
estimular a formação de novos laços sociais e, por isso, a divisão dos grupos de alunos, 
será feita seguindo um critério:

Alunos com número de matrícula par, ficarão no grupo azul.
Alunos com número de matrícula ímpar, ficarão no grupo amarelo. 

Os alunos ainda não sabem dessa regra de separação dos grupos e, no dia do evento, quando
digitarem o número da matrícula na catraca, deve aparecer no painel a cor do grupo que ele deve integrar. 

DESAFIO: Desenvolvam uma função para retornar se o número passado pelo usuario no console é par ou ímpar.

Caso o número de matrícula do(a) aluno(a) seja par imprima:
VOCÊ ESTÁ NO TIME AZUL

Caso o número de matrícula do(a) aluno(a) seja impar imprima:
VOCÊ ESTÁ NO TIME AMARELO"""


def verificar_time(matricula):
    if matricula % 2 == 0:
        return "Você está no time azul"
    else:
        return "Você está no time amarelo"
matricula = int(input("Digite o numero da sua matricula: "))
print(verificar_time(matricula))

# Se você colocar matricula = int(input(...)) com espaços dentro da função depois do return, ele nunca vai rodar porque:Está dentro da função mas depois de um return → não executa.Python não ignora espaços: indentação determina quais linhas pertencem a qual bloco.