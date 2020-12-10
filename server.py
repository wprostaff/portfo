from flask import Flask, render_template, request, url_for, redirect
import csv #para tratar con ficheros extensión csv


app = Flask(__name__)


@app.route('/') 
def my_home():
	return render_template('index.html')


# @app.route('/about.html') #sería más cómodo /about pero es para ver que tb podemos especificar más
# def about():
# 	#flask, cuando usa render_template, busca en una carpeta llamada templates. Luego colocamos nuestros ficheros allí
#     return render_template('about.html')

# @app.route('/index.html')
# def home():
#     return render_template('index.html')

# #ahora se mostrará en 127.0.0.1:5000/home 

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')
# Vamos a hacer esto de arriba de forma dinámica, en lugar de tener que estar definiéndolo nosotros


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


def escribe_a_fichero(data):
	try:
		with open('database.txt', mode='a') as database_h:
			email = data['email']
			subject = data['subject']
			message = data['message']
			file = database_h.write(f'\n{email},{subject},{message}')
			
	except	FileNotFoundError:
		print('Archivo no encontrado:', 'database.txt')


def escribe_a_csv(data):
	try:
		with open('database.csv', mode='a', newline='') as database_h_csv:
			email = data['email']
			subject = data['subject']
			message = data['message']
			#configuración del objeto. Ver módulo csv en docs.python.org
			csv_writer = csv.writer(database_h_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			csv_writer.writerow([email,subject,message])
	except	FileNotFoundError:
		print('Archivo no encontrado:', 'database.csv')



@app.route('/enviar_formulario', methods=['POST', 'GET'])
def enviar_formulario():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			#print(data)
			#escribe_a_fichero(data)
			escribe_a_csv(data)
		return redirect('/gracias.html')
		except:
			return '¡No se pudo salvar a la base de datos!'
	else:
		return 'Algo fue mal, inténtalo de nuevo.'
#Para servir los ficheros css y js, consultamos la documentacion de flask quickstart y nos detenemos en
#Static Files
#Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from. Ideally your web server is configured to serve them for you, but during development Flask can do that as well. Just create a folder called static in your package or next to your module and it will be available at /static on the application.

#To generate URLs for static files, use the special 'static' endpoint name:

#url_for('static', filename='style.css')
#The file has to be stored on the filesystem as static/style.css.

