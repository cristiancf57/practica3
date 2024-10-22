from flask import Flask,render_template,redirect,session,request,url_for

app = Flask(__name__)
app.secret_key = 'clavesecreta'

@app.route('/')
def index():
    if 'lista' not in session:
        session['lista']=[]
    return render_template("index.html",lista = session['lista'])

@app.route('/procesa',methods=['GET','POST'])
def procesa():
    fecha = request.form.get('fecha')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    turno = request.form.get('turno')
    seminario = request.form.getlist('seminario')
    if 'lista' not in session:
        session['lista'] = []

    # diccionario de datos
    nuevo={
        'fecha':fecha,
        'nombre':nombre,
        'apellido':apellido,
        'turno':turno,
        'seminario':'; '.join(seminario)
    }
    # agregar el inscrito a la session
    session['lista'].append(nuevo)
    session.modified=True
    return redirect(url_for('index'))

@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

@app.route('/editar')
def editar(dato):
    
    if 'lista' in session and len(session['lista'])>index:
        session['lista'].pop(index)
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar(index):
    if 'lista' in session and len(session['lista'])>index:
        session['lista'].pop(index)
    return redirect(url_for('lista'))

@app.route('/vaciar')
def vaciar():
    session.pop('lista',None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)