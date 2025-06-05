from flask import Flask, request, render_template_string
import os
from parser import extract_sections

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_FORM = """
<!doctype html>
<title>Upload Title Insurance Document</title>
<h1>Upload a document</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
{% if sections %}
<h2>Sections Found</h2>
{% for name, content in sections.items() %}
<h3>{{ name.replace('_', ' ').title() }}</h3>
<pre>{{ content }}</pre>
{% endfor %}
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    sections = None
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename:
            path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(path)
            sections = extract_sections(path)
    return render_template_string(HTML_FORM, sections=sections)

if __name__ == '__main__':
    app.run(debug=True)
