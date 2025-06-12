# flowtask/app/services/task_manager.py
# A importação correta é a partir do pacote 'app'
from app.db.models.task import Tarefa

class TaskManager:
    # Gerencia um conjunto de tarefas, permitindo adicionar, listar, buscar, ver detalhes e marcar tarefas como concluídas.

    def __init__(self):
        """Inicializa o TaskManager com uma lista de tarefas vazia."""
        self.tarefas = []

    def adicionar_tarefa(self):
        """Solicita ao usuário os detalhes e adiciona uma nova tarefa à lista."""
        titulo = input('Digite o título da tarefa: ')
        descricao = input('Digite a descrição da tarefa: ')
        tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa)
        print(f'\nTarefa "{titulo}" adicionada com sucesso!')

    def listar_tarefas(self):
        """Exibe todas as tarefas cadastradas."""
        if not self.tarefas:
            print('\nNenhuma tarefa cadastrada.')
            return
        
        print('\n--- Tarefas ---')
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f'--- Tarefa {i} ---')
            print(tarefa)

    def buscar_tarefa(self):
        """Busca por tarefas que contenham um termo no título ou na descrição."""
        if not self.tarefas:
            print('\nNenhuma tarefa cadastrada para buscar.')
            return
            
        termo = input('Digite o termo de busca: ').lower()
        resultados = [
            t for t in self.tarefas 
            if termo in t.titulo.lower() or termo in t.descricao.lower()
        ]

        if not resultados:
            print('\nNenhuma tarefa encontrada com esse termo.')
        else:
            print('\n--- Resultados da busca ---')
            for i, tarefa in enumerate(resultados, start=1):
                print(f'\n--- Resultado {i} ---')
                print(tarefa)

    def mostrar_detalhes(self):
        """Exibe os detalhes de uma tarefa específica pelo seu número na lista."""
        if not self.tarefas:
            print('\nNenhuma tarefa cadastrada.')
            return
            
        self.listar_tarefas()
        try:
            numero = int(input('\nDigite o número da tarefa para ver os detalhes: '))
            if 1 <= numero <= len(self.tarefas):
                tarefa = self.tarefas[numero - 1]
                print(f'\n--- Detalhes da Tarefa {numero} ---')
                print(tarefa)
            else:
                print('\nNúmero de tarefa inválido.')
        except ValueError:
            print('\nEntrada inválida. Por favor, digite um número.')

    def concluir_tarefa(self):
        """Marca uma tarefa específica como concluída."""
        if not self.tarefas:
            print('\nNenhuma tarefa cadastrada.')
            return

        self.listar_tarefas()
        try:
            numero = int(input('\nDigite o número da tarefa a ser marcada como concluída: '))
            if 1 <= numero <= len(self.tarefas):
                tarefa = self.tarefas[numero - 1]
                tarefa.marcar_concluida()
                print(f'\nTarefa "{tarefa.titulo}" marcada como concluída!')
            else:
                print('\nNúmero de tarefa inválido.')
        except ValueError:
            print('\nEntrada inválida. Por favor, digite um número.')
