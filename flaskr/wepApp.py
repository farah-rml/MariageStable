from flask import Flask, render_template, request, jsonify
from MariageStable import MariageStable
from SatisfactionCalculator import SatisfactionCalculator
import preferences_generator

class WebApp():
	app : Flask = Flask(__name__)
	def __init__(self):
		self.app.debug = True
		self.app.run()

	@app.route('/')
	def index():
		return render_template('index.html')

	@app.route('/generate-preferences', methods=['POST'])
	def generate_preferences():
		number = int(request.json.get('number'))
		if(number > 100):
			return "Number to high (>100)"
		s, e = preferences_generator.gen_pref(number)
		return jsonify({'s': s, 'e': e})

	@app.route('/stable-marriage', methods=['POST'])
	def stable_marriage():
		preferences = request.json.get('preferences')
		s = preferences['s']
		e = preferences['e']
		m = MariageStable(s, e)
		
		steps = []
		for i in range(1000):
			if not m.hasNext():
				break
			steps.append(m.next())

		stats = SatisfactionCalculator(s,e, m.matches)
		
		metadata = {
			"result" : m.matches,
			"satisfaction" : {
				"Students_satisfaction": stats.getStudentsSatisfaction(),
				"Schools_satisfaction": stats.getSchoolsSatisfaction(),
				"Average_student satisfaction": stats.getAverageStudentSatisfaction(),
				"Average_school satisfaction": stats.getAverageSchoolSatisfaction(),
				"Average_global satisfaction": stats.getGlobalSatisfaction()
			}
		}
			
		return jsonify({'steps': steps, 'metadata': metadata})