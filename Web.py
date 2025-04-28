from flask import Flask
import os

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World", 200

if __name__ == '__main__':
    # Azure asigna el puerto mediante la variable de entorno PORT,
    # si no existe, se usa el puerto 80 por defecto.
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)

