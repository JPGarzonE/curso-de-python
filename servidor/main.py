# Para correr el servidor simplemente ejecutrar este script con pyrhon3 en consola

from flask import Flask;

app = Flask(__name__);

@app.route('/')
def helloWorld():
    return 'Hola, mundo.';

if __name__ == '__main__':
    app.run();
