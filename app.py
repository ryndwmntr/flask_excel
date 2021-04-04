import pandas as pd

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		data = request.files["file"]
		df = pd.read_excel(data)
		table = df.to_html(index=False)

		return render_template('index.html', table = table)

	return render_template('upload.html')


if __name__ == "__main__":
	app.run()