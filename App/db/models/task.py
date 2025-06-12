class Tarefa: # Classe para representar uma tarefa, com título, descrição e status
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False
    
    def marcar_concluida(self): # Método para marcar a tarefa como concluída
        self.concluida = True
    
    def status(self): # Método para retornar o status da tarefa
        return 'Concluída' if self.concluida else 'Pendente'    
    
    def __str__(self): # Método para representar a tarefa como string
        return f'Título: {self.titulo}\nDescrição: {self.descricao}\nStatus: {self.status()}'