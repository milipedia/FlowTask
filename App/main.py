#Começando uma variavel para armazenar as tarefas, inicialmente vazia
tarefas = []

class Tarefa: # Classe para representar uma tarefa, com título, descrição e status
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False
    
    def marcar_concluida(self):
        self.concluida = True
    
    def status(self):
        return 'Concluída' if self.concluida else 'Pendente'    
    
    def __str__(self):
        return f'Título: {self.titulo}\nDescrição: {self.descricao}\nStatus: {self.status()}'


def adicionar_tarefa():
    titulo = input('Digite o título da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    tarefa = Tarefa(titulo, descricao)
    tarefas.append(tarefa)#Adicionando a tarefa à lista de tarefas    
    print(f'Tarefa "{titulo}" adicionada com sucesso!')

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
    else:
        print('--- Tarefas: ---')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefa}')

# Função para mostrar os detalhes de uma tarefa específica
def buscar_tarefa():
    termo = input('Digite o termo de busca: ').lower()
    resultados = []
    for tarefa in tarefas:
        if termo in tarefa.titulo.lower() or termo in tarefa.descricao.lower():
            resultados.append(tarefa)
    if not resultados:      
        print('Nenhuma tarefa encontrada com esse termo.')
    else: 
        print('--- Resultados da busca: ---')
        for i, tarefa in enumerate(resultados, start=1):
            print(f'{i}. {tarefa}')

#Função para mostrar os detalhes de uma tarefa 
def mostrar_detalhes():
    if not tarefas:
        print('Nenhuma tarefa cadastrada para mostrar detalhes.')
        return
    try:
        numero = int(input('Digite o número da tarefa para ver os detalhes: ')) - 1
        tarefa = tarefas[numero]
        print(f'--- Detalhes da Tarefa {numero + 1} ---')
        print(f'Título: {tarefa.titulo}')
        print(f'Descrição: {tarefa.descricao}')
        print(f'Status: {tarefa.status()}')
    except (ValueError, IndexError):
        print('Número de tarefa inválido. Tente novamente.')

#Função para concluir tarefas
def concluir_tarefa():
    if not tarefas:
        print('Nenhuma tarefa cadastrada para marcar como concluída.')
        return
    try:
        numero = int(input('Digite o número da tarefa a ser marcada como concluída: ')) - 1
        tarefa = tarefas[numero]
        tarefa.marcar_concluida()
        print(f'Tarefa "{tarefa.titulo}" marcada como concluída!')
    except (ValueError, IndexError):
        print('Número de tarefa inválido. Tente novamente.')

def menu():
    # Função para exibir o menu principal e gerenciar as opções do usuário
    print("Bem-vinda ao FlowTask! ")
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
