
# Table of Contents

# How to test the project:

This projects uses chatGPT to evaluate if a Resume fits with a Job description.

First, you need to define as environment vaiable the chatGPT token in `OPENAI_API_KEY` var.

To execute, you need to run bellow commants
```
    source venv/bin/activate
    pip install -r requirements.txt
    export FLASK_APP=app
    export FLASK_ENV=development
    flask --debug run
```

