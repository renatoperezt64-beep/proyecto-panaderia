from flask import Flask, render_template

# Inicializamos la aplicación
app = Flask(__name__)

# Creamos la ruta principal de la página
@app.route('/')
def inicio():
    # Esto le dice a Python que muestre tu esquema visual de la panadería
    return render_template('index.html')

if __name__ == '__main__':
    # Ejecutamos el servidor en modo de prueba
    app.run(debug=True)