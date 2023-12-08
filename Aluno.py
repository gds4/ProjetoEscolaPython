import sys

import Funcoes_Gerais as FG
from Menu import menu_cadastro


class Aluno:

    alunos_cadastrados = []

    def __init__(self, nome, sexo, cpf, nasc, matricula):
        self.nome = nome
        self.sexo = sexo
        self.CPF = cpf
        self.Nasc = nasc
        self.Matricula = matricula
        Aluno.alunos_cadastrados.append(self)


    @classmethod
    def inserir_aluno(cls):
        
        nome = FG.obter_dado_Nome('Aluno')
    
        sexo = FG.obter_dado_Sexo('Aluno')

        cpf = FG.obter_dado_CPF('Aluno')

        dataNasc = FG.obter_dado_dataNasc('Aluno')

        matricula = FG.obter_dado_Matricula('Aluno')

        cls(nome = nome, sexo = sexo, cpf = cpf, nasc = dataNasc, matricula = matricula)

    
    @classmethod
    def excluir_aluno(cls):
        sair = 1
        print('Para retornar digite [0]')
        print('Insira a matricula do aluno: ', end = ' ')
        while sair:
            
            matricula_excluir = str(input())
            if matricula_excluir == '0':
                return
                
            for aluno in cls.alunos_cadastrados:
                if aluno.Matricula == matricula_excluir:
                    cls.alunos_cadastrados.remove(aluno)
                    print('\nAluno removido com sucesso!')
                    break
    
            print('\nMatricula nao encontrada!')
            print('Digite novamente: ', end = ' ')

    @classmethod
    def listar_alunos(cls):
        print('Matricula Nome                           Sexo CPF             Nasc      \n')
        for aluno in cls.alunos_cadastrados:
            print(f'{aluno.Matricula.ljust(9)} {aluno.nome.ljust(30)} {aluno.sexo.ljust(4)} {aluno.CPF.ljust(15)} {aluno.Nasc.ljust(10)}')

    @classmethod
    def atualizar_cadastro(cls):
        print('Digite o nome completo do aluno: ', end = ' ')

        while True:
            nome_do_aluno = str(input())
            encontrou_aluno = 0
            
            for aluno in cls.alunos_cadastrados:
                if aluno.nome == nome_do_aluno:
                    encontrou_aluno = 1
                    menu_cadastro()
                    while True:
                        aux = input()
                        if aux.isdigit():
                            opcao_cadastro = int(aux)
                            match opcao_cadastro:
                                case 0:
                                    break
                                case 1:
                                    aluno.Maricula = FG.obter_dado_Matricula('Aluno')
    
                                case 2:
                                    aluno.nome = FG.obter_dado_Nome('Aluno')
    
                                case 3:
                                    aluno.sexo = FG.obter_dado_Sexo('Aluno')
                                    
                                case 4:
                                    aluno.CPF = FG.obter_dado_CPF('Aluno')
                                    
                                case 5:
                                    aluno.Nasc = FG.obter_dado_dataNasc('Aluno')
                                    
                                case _:
                                    FG.valor_invalido(opcao_cadastro)
                            break
                        else:
                            FG.valor_invalido(aux)
                            
                    break
    
            if encontrou_aluno == 0:
                print('Nao existe nenhum aluno com este nome no Sistema')
                print('Tente novamente')
            else:
                break