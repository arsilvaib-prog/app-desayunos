from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('menu.html')

@app.route('/pedido', methods=['POST'])
def pedido():
    producto = request.form['producto']
    cliente = request.form['cliente']
    direccion = request.form['direccion']

    return f"""
    <h1>✅ Pedido recibido</h1>
    <p>Cliente: {cliente}</p>
    <p>Producto: {producto}</p>
    <p>Dirección: {direccion}</p>
    <br>
    <a href="https://wa.me/5214461414743?text=Hola soy {cliente} y pedí {producto} a la dirección {direccion}">
        📲 Confirmar por WhatsApp
    </a>
    """

@app.route('/manifest.json')
def manifest():
    return send_from_directory('.', 'manifest.json')

if __name__ == '__main__':
    app.run()