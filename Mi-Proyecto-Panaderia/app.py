from flask import Flask, render_template
import os

# Configuramos la ruta absoluta hacia la carpeta 'templates'
# Esto le dice a Flask: "Busca 'templates' donde sea que esté este archivo app.py"
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    # Render asigna el puerto automáticamente mediante una variable de entorno
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)