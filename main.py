import sys

import Aluno as al
import Funcoes_Gerais as FG

import Menu



sair = int(5)
menu_inicial = None

while True:

    Menu.menu_inicial()

    opcao_tmp = input()


    if opcao_tmp.isdigit() is True:

        menu_inicial = int(opcao_tmp)
        match menu_inicial:
        
            case  0:
                print('Sistema Finalizado.')
                sys.exit()
    
            case 1:
                while True:
                    Menu.menu_principal()
    
                    opcao_tmp = input()
    
                    if opcao_tmp.isdigit() is True:
    
                        opcao_menu_inicial = int(opcao_tmp)

                        match opcao_menu_inicial:
                            case 0:
                                break
    
                            case 1:
                                while True:
                                    
                                    Menu.menu_aluno()
                                    
                                    opcao_aluno = str(input())
                                    
                                    if opcao_aluno.isdigit() is True:
                                        opcao_menu_aluno = int(opcao_aluno)
                                        
                                        match opcao_menu_aluno:
                                            case 0:
                                                break
        
                                            case 1:
                                                al.Aluno.inserir_aluno()
        
                                            case 2:
                                                al.Aluno.listar_alunos()
                                                
                                            case 3:
                                                al.Aluno.atualizar_cadastro()
                                                
                                            case 4:
                                                al.Aluno.excluir_aluno()
                                                
                                            case _:
                                                FG.valor_invalido(opcao_tmp)
                                        
                            case 2:
                                Menu.menu_professor()
                                opcao_professor = input()
        
                            case 3:
                                Menu.menu_disciplina()
                                opcao_disciplina = input()
        
                            case _:
                                FG.valor_invalido(opcao_menu_inicial)
        
                    else:
                        FG.valor_invalido(opcao_tmp)
    
            case _:
                FG.valor_invalido(menu_inicial)
    
    else:
        FG.valor_invalido(opcao_tmp)