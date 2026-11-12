from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB = Path("cupcakes_pedro.db")

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS pedidos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL,
            pagamento TEXT NOT NULL,
            entrega TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pedido recebido'
        )""")

@app.route("/api/pedidos", methods=["POST"])
def criar_pedido():
    init_db()
    dados = request.get_json(force=True)
    campos = ["cliente","telefone","endereco","pagamento","entrega","total"]
    faltando = [c for c in campos if not dados.get(c)]
    if faltando:
        return jsonify({"erro":"Campos obrigatórios ausentes","campos":faltando}),400
    with sqlite3.connect(DB) as conn:
        cur=conn.execute(
            "INSERT INTO pedidos(cliente,telefone,endereco,pagamento,entrega,total) VALUES(?,?,?,?,?,?)",
            (dados["cliente"],dados["telefone"],dados["endereco"],dados["pagamento"],dados["entrega"],float(dados["total"]))
        )
        pid=cur.lastrowid
    return jsonify({"pedido_id":pid,"status":"Pedido recebido"}),201

@app.route("/api/pedidos/<int:pedido_id>", methods=["GET"])
def consultar_pedido(pedido_id):
    init_db()
    with sqlite3.connect(DB) as conn:
        row=conn.execute("SELECT id,cliente,pagamento,entrega,total,status FROM pedidos WHERE id=?",(pedido_id,)).fetchone()
    if not row:
        return jsonify({"erro":"Pedido não encontrado"}),404
    return jsonify({"id":row[0],"cliente":row[1],"pagamento":row[2],"entrega":row[3],"total":row[4],"status":row[5]})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
