#Começando uma variavel para armazenar as tarefas, inicialmente vazia
tarefas = []

def adicionar_tarefa():
    titulo = input('Digite o título da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    #Criando um dicionário para armazenar a tarefa
    tarefa = {
        'titulo': titulo,
        'descricao': descricao,
        'concluida': False
    }
    #Adicionando a tarefa à lista de tarefas    
    tarefas.append(tarefa)
    print(f'Tarefa "{titulo}" adicionada com sucesso!')

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
    else:
        print('--- Tarefas: ---')
        for i, tarefa in enumerate(tarefas, start=1):
            status = 'Concluída' if tarefa['concluida'] else 'Pendente'
            print(f'{i}. {tarefa["titulo"]} - Status: {status}')

# Função para mostrar os detalhes de uma tarefa específica
def buscar_tarefa():
    termo = input('Digite o termo de busca: ').lower()
    resultados = []
    for tarefa in tarefas:
        if termo in tarefa['titulo'].lower() or termo in tarefa['descricao'].lower():
            resultados.append(tarefa)
    if not resultados:      
        print('Nenhuma tarefa encontrada com esse termo.')
    else: 
        print('--- Resultados da busca: ---')
        for i, tarefa in enumerate(resultados, start=1):
            status = 'Concluída' if tarefa['concluida'] else 'Pendente'
            print(f'{i}. {tarefa["titulo"]} - Status: {status}') 


def mostrar_detalhes():
    if not tarefas:
        print('Nenhuma tarefa cadastrada para mostrar detalhes.')
        return
    try:
        numero = int(input('Digite o número da tarefa para ver os detalhes: ')) - 1
        tarefa = tarefas[numero]
        print(f'Título: {tarefa["titulo"]}')
        print(f'Descrição: {tarefa["descricao"]}')
        status = 'Concluída' if tarefa['concluida'] else 'Pendente'
        print(f'Status: {status}')
    except (ValueError, IndexError):
        print('Número de tarefa inválido.')

def concluir_tarefa():
    if not tarefas:
        print('Nenhuma tarefa cadastrada para marcar como concluída.')
        return
    try:
        numero = int(input('Digite o número da tarefa a ser marcada como concluída: ')) - 1
        tarefas[numero]['concluida'] = True
        print(f'Tarefa "{tarefas[numero]["titulo"]}" marcada como concluída!')
    except (ValueError, IndexError):
        print('Número de tarefa inválido.')

def menu():
    # Função para exibir o menu principal e gerenciar as opções do usuário
    print("Bem-vinda ao FlowTask! 💚")
    while True:
        print('\nO que deseja fazer?')
        print('1 - Adicionar tarefa')
        print('2 - Listar tarefas')
        print('3 - Detalhes da tarefa')
        print('4 - Marcar tarefa como concluída')
        print('5 - Sair')

        escolha = input('Digite o número da opção desejada: ')
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            mostrar_detalhes()
        elif escolha == '4':
            concluir_tarefa()
        elif escolha == '5':
            print('Saindo do FlowTask. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')

# Executa o programa    
if __name__ == "__main__":
    menu()
