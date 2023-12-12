import os
from flask import Flask, render_template
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.utils import secure_filename

from brain_module import ChatGPT
from read_doc import read_docx
from prompt import q
from models import db, Job

UPLOAD_FOLDER = os.path.abspath('./tmp/')
ALLOWED_EXTENSIONS = {'docx'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a81283c8820127df04a5720056b029b91d0e8dd1ec049db6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db.init_app(app)
bot = ChatGPT()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        job_id = request.form['id']
        job_title = request.form['title']
        job_location = request.form['location']
        job_content = request.form['content']
        new_job = Job(id=job_id, 
                      title=job_title, 
                      location=job_location, 
                      content=job_content)
        
        try:
            db.session.add(new_job)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the Job'
    else:
        jobs = Job.query.order_by(Job.date_created).all()
        return render_template('index.html', jobs=jobs)

@app.route('/delete/<int:id>')
def delete(id):
    job_to_delete = Job.query.get_or_404(id)

    try:
        db.session.delete(job_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting the Job description'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    job = Job.query.get_or_404(id)
    print(job.title)
    print(job.content)
    if request.method == 'POST':
        job.id = request.form['id']
        job.title = request.form['title']
        job.location = request.form['location']
        job.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating the Job description'
    else:
        return render_template('update.html', job=job)


@app.route('/outline/<int:id>', methods=['GET', 'POST'])
def outline(id):
    job = Job.query.get_or_404(id)

    if request.method == 'POST':
        # check if the post request has the file part
        if 'resume' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['resume']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            profile = f'Position: {job.title}\nLocation: {job.location}\n\n{job.content}'

            resume = read_docx(f'{UPLOAD_FOLDER}/{filename}')
            question_1 = q["sumarize_resume"].format(resume = resume)
            question_2 = q["qualify_resume"].format(job = profile, resume = resume)

            response1 = bot.request_openai(question_1)
            response2 = bot.request_openai(question_2)

            return render_template('review.html', answer1=response1, answer2=response2)
    else:
        return render_template('outline.html', job=job)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(debug=True)

