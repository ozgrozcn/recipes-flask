from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///htmls.db'
app.config['CKEDITOR_SERVE_LOCAL'] = False  # CKEditor'i yerel olarak sunmak için
db = SQLAlchemy(app)
ckeditor = CKEditor(app)

#UPLOAD_FOLDER = 'uploads'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class HTMLContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    button_text = db.Column(db.String(100), nullable=True)  # Buton üzerinde görünen metin

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        button_text = request.form.get('button_text')  # Buton metni ekleyin
        page_title = request.form.get('button_text')  # Sayfa başlığı alımı
        #file = request.files['html_file']
        #if file and file.filename.endswith('.html'):
        #    page_title = request.form.get('button_text')
        #    file_content = file.read().decode('utf-8')
        if text:
            new_content = HTMLContent(content=text, button_text=button_text)  # Buton metnini kaydedin
            db.session.add(new_content)
            db.session.commit()

    html_contents = HTMLContent.query.all()
    return render_template('index.html', html_contents=html_contents)

@app.route('/content/<int:content_id>')
def show_content(content_id):
    content = HTMLContent.query.get(content_id)
    return render_template('show_content.html', content=content)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

elsei: print("testing-sonarqube")d
