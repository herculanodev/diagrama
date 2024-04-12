from graphviz import Digraph
import os

# Definindo o caminho para o diretório onde o gráfico será salvo
directory = "grafico"
path = os.path.join(os.getcwd(), directory)

# Verifica se o diretório existe. Se não, cria o diretório
if not os.path.exists(path):
    os.makedirs(path)

# Cria um novo gráfico direcionado para o diagrama de caso de uso
dot = Digraph('WeaCast_Use_Case_Diagram', format='png')

# Configurações globais para o gráfico
dot.attr(rankdir='TB', label='Diagrama de Caso de Uso do WeaCast', fontsize='20', fontname='bold')
dot.attr('node', style='filled', shape='box', fontname='Arial')

# Cores e estilos para atores e casos de uso
dot.node('U', 'Usuário', shape='ellipse', color='lightgreen', fontcolor='black', fillcolor='darkolivegreen1', gradientangle='270')
dot.node('A', 'Ver Previsão do Tempo', fillcolor='lightblue2:skyblue', gradientangle='90')
dot.node('B', 'Alterar Localização', fillcolor='lightblue2:skyblue', gradientangle='90')
dot.node('C', 'Receber Alertas Meteorológicos', fillcolor='lightblue2:skyblue', gradientangle='90')
dot.node('D', 'Visualizar Detalhes Meteorológicos', fillcolor='lightblue2:skyblue', gradientangle='90')
dot.node('E', 'Configurar Preferências', fillcolor='lightblue2:skyblue', gradientangle='90')

# Estilos de aresta para indicar tipos de relação
dot.attr('edge', style='solid', color='black', arrowhead='vee')

# Definindo as conexões entre os nós
dot.edges(['UA', 'UB', 'UC', 'UD', 'UE'])

# Renderização do gráfico
output_file = os.path.join(path, 'WeaCast_Use_Case_Diagram')
dot.render(output_file)

print("O gráfico foi salvo em:", output_file)
