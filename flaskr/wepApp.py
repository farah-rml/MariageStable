from flask import Flask, render_template, request
from MariageStable import MariageStable
import preferences_generator

class WebApp():
	app : Flask = Flask(__name__)
	def __init__(self):
		self.app.debug = True
		self.app.run()

	@app.route('/', methods=['POST', 'GET'])
	def hello():
		if request.method == 'POST':
			s,e = preferences_generator.gen_pref(int(request.form.get("number")))
			m = MariageStable(s,e)
			return m.solve(False)
		elif request.method == 'GET':
			return render_template('index.html')
			