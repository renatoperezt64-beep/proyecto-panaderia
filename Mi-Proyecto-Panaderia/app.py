from flask import Flask, render_template
import os

# Esto le dice a Flask dónde buscar tus archivos HTML, sin importar dónde esté el proyecto
template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def inicio():
    # Render buscará 'index.html' dentro de la carpeta 'templates'
    return render_template('index.html')

if __name__ == '__main__':
    # Render asigna el puerto automáticamente, esto es vital
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)