from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario

app = Flask(__name__)
CORS(app)
engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

#criar usuario cuidador
@app.route('/usuarios', methods=["POST"])
def add_usuario():
    s = Session()
    data = request.json

    u = Usuario(
        nome = data["nome"],
        email = data["email"],
        telefone = data["telefone"],
        cidade = data["cidade"],
        valor = data["valor"],
        experiencia = data.get("experiencia")
    )

    s.add(u)
    s.commit()
    return jsonify({
        "message": "Usuário criado!"
    })

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    s = Session()
    usuarios = s.query(Usuario).all()
    
    return jsonify([{
            "id": u.id,
            "nome": u.nome,
            "email": u.email,
            "telefone": u.telefone,
            "cidade": u.cidade,
            "valor": round(u.valor, 2),
            "experiencia": u.experiencia
        } for u in usuarios])

#buscar usuarios por cidade
@app.route("/usuarios/<cidade>", methods=["GET"])
def get_unique_usuario(cidade):
    s = Session()
    usuarios = s.query(Usuario).filter(Usuario.cidade == cidade).all()

    return jsonify([{
            "id": u.id,
            "nome": u.nome,
            "email": u.email,
            "telefone": u.telefone,
            "cidade": u.cidade,
            "valor": round(u.valor, 2),
            "experiencia": u.experiencia
        } for u in usuarios])
    

#editar informações do usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def editar_informacoes_usuario(id):
    s = Session()
    data = request.json
    usuario = s.query(Usuario).filter_by(id=id).first()

    usuario.nome = data.get('nome', usuario.nome)
    usuario.email = data.get('email', usuario.email)
    usuario.telefone = data.get('telefone', usuario.telefone)
    usuario.cidade = data.get('cidade', usuario.cidade)
    usuario.valor = data.get('valor', usuario.valor)
    usuario.experiencia = data.get('experiencia', usuario.experiencia)

    s.commit()
    return jsonify({"mensagem": "Usuário atualizado com sucesso"})

# # #excluir usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    s = Session()
    usuario = s.query(Usuario).filter_by(id=id).first()

    s.delete(usuario)
    s.commit()

    return jsonify({
        "mensagem": "Conta excluída com sucesso"
    })

if __name__ == "__main__": 
    app.run(debug=True)