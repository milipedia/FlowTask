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

class TaskManager: # Classe para gerenciar as tarefas
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self): # Função para adicionar uma nova tarefa
        titulo = input('Digite o título da tarefa: ')
        descricao = input('Digite a descrição da tarefa: ')
        tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa) # Adiciona a nova tarefa à lista de tarefas
        print(f'Tarefa "{titulo}" adicionada com sucesso!')

    def listar_tarefas(self):
        if not self.tarefas:
            print('Nenhuma tarefa cadastrada.')
        else:
            print('--- Tarefas: ---')
            for i, tarefa in enumerate(self.tarefas, start=1): # Enumerate para listar as tarefas com índice
                print(f'{i}. {tarefa}')

# Função para mostrar os detalhes de uma tarefa específica
    def buscar_tarefa(self):
        termo = input('Digite o termo de busca: ').lower()
        resultados = [t for t in self.tarefas if termo in t.titulo.lower() or termo in t.descricao.lower()]
        if not resultados:
            print('Nenhuma tarefa encontrada com esse termo.')
        else:
            print('--- Resultados da busca: ---')
            for i, tarefa in enumerate(resultados, start=1):
                print(f'{i}. {tarefa}')
        

#Função para mostrar os detalhes de uma tarefa 
    def mostrar_detalhes():
        if not self.tarefas:
            print('Nenhuma tarefa cadastrada.')
            return
        try:
            numero = int(input('Digite o número da tarefa para ver os detalhes: ')) - 1
            tarefa = tarefas[numero]
            print(f'--- Detalhes da Tarefa ---\n{tarefa}')
            print(f'--- Detalhes da Tarefa {numero + 1} ---')
            print(f'Título: {tarefa.titulo}')
            print(f'Descrição: {tarefa.descricao}')
            print(f'Status: {tarefa.status()}')
        except (ValueError, IndexError):
            print('Número de tarefa inválido. Tente novamente.')

#Função para concluir tarefas
    def concluir_tarefa(self):
        if not self.tarefas:
            print('Nenhuma tarefa cadastrada para marcar como concluída.')
            return
        try:
            numero = int(input('Digite o número da tarefa a ser marcada como concluída: ')) - 1
            tarefa = self.tarefas[numero]
            tarefa.marcar_concluida()
            print(f'Tarefa "{tarefa.titulo}" marcada como concluída!')
        except (ValueError, IndexError):
            print('Número de tarefa inválido. Tente novamente.')

def menu():
    gerenciador = TaskManager() # Cria uma instância do gerenciador de tarefas
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

# Executa o programa    
if __name__ == "__main__":
    menu()
