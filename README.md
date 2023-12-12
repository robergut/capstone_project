
# Table of Contents

# How to test the project:

1. Change the content of the `job_description.txt` file in the resources directory, for a different job description
2. Change the `resume.docx` for another file to test
3. Run the following code
```
    source venv/bin/activate
    pip install -r requirements.txt
export FLASK_APP=app
export FLASK_ENV=development
flask --debug run
```

