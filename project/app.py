from flask import Flask, request, jsonify
from project.models.task import Task

app = Flask(__name__)

# CRUD: Create, Read, Update and Delete
# Tabela: tarefa

tasks = []
task_id_control = 1

# criação do 'create'
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()   # recupera o que o clientes mandou para gente
    new_task = Task(id=task_id_control ,title=data.get("title"), description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"mensagem": "Nova tarefa criada com sucesso"})


# criação do 'read'- buscando todo os objetos
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)


# criação do 'read' - buscando um objeto especifico 
@app.route('/tasks/<int:id>/', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"mensagem": "Não foi possivel encontrar a atividade"}), 404

# criação de 'update' (atualização)
@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message" : "Não foi possivel encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message" : "Tarefa atualizada com sucesso"})

# criação de 'delete' (deletar)
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        print(t.to_dict())
        if t.id == id:
            task = t
            break
    if not task: 
        return jsonify({"message" : "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"messagem" : "Tarefa deletada com sucesso!"})





# paramentro do flask (MUITO USADO)
# Documentação flask.palletsprojects.com 
# retorna o tipo int
@app.route('/user/<int:user_id>')
def show_user_int(user_id):
    print(user_id)
    print(type(user_id))
    return "%s" % user_id

# retorna o tipo string
@app.route('/user/<username>')  # sem parametro a função retorna uma string 
def show_user_string(username):
    print(username)
    print(type(username))
    return username

# retorna o tipo float (ponto flutuante)
@app.route('/user/<float:number>')
def show_user_float(number):
    print(number)
    print(type(number))
    return "%s" % number

# retorna o path (aceita '///')
@app.route('/user/<path:subpath>')
def show_user_path(subpath):
    print(subpath)
    print(type(subpath))
    return "%s" % subpath

if __name__ == "__main__":
    app.run(debug=True) 

