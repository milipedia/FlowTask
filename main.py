from app.services.task_manager import TaskManager #Trazendo o arquivo correto do pacote 'app'

def menu(gerenciador: TaskManager):
    # Menu principal do FlowTask
     while True:
        print('\nO que deseja fazer?')
        print('1 - Adicionar tarefa')
        print('2 - Listar tarefas')
        print('3 - Buscar tarefa')
        print('4 - Mostrar detalhes da tarefa')
        print('5 - Marcar tarefa como concluída')
        print('6 - Sair')

        escolha = input('Digite o número da opção desejada: ')
        if escolha == '1':
            gerenciador.adicionar_tarefa()
        elif escolha == '2':
            gerenciador.listar_tarefas()
        elif escolha == '3':
            gerenciador.buscar_tarefa()
        elif escolha == '4':
            gerenciador.mostrar_detalhes()
        elif escolha == '5':
            gerenciador.concluir_tarefa()
        elif escolha == '6':
            print('Saindo do FlowTask. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    # Cria uma única instância do gerenciador de tarefas
    task_manager = TaskManager()
    
    # Inicia o menu, passando a instância do gerenciador de tarefas
    menu(task_manager)
    