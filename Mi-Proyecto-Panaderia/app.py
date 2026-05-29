from flask import Flask, render_template

# Inicializamos la aplicación
import os
# Esto le dice a Flask que busque la carpeta 'templates' en la misma carpeta donde está app.py
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

# Creamos la ruta principal de la página
@app.route('/')
def inicio():
    # Esto le dice a Python que muestre tu esquema visual de la panadería
    return render_template('index.html')

if __name__ == '__main__':
    # Ejecutamos el servidor en modo de prueba
    app.run(debug=True)