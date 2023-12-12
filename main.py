#!/usr/bin/env python3

from brain_module import ChatGPT
from prompt import q
from read_doc import read_docx, read_profile
import os

url = './resources/{0}'

if  __name__ == "__main__":
    profile_path = os.path.abspath(url.format('job_description.txt'))
    resume_path = os.path.abspath(url.format('resume.docx'))

    profile = read_profile(profile_path)
    resume = read_docx(resume_path)

    question_1 = q["sumarize_resume"].format(resume = resume)
    question_2 = q["qualify_resume"].format(job = profile, resume = resume)

    bot = ChatGPT()
    response = bot.request_openai(question_1)
    print(response)
    response = bot.request_openai(question_2)
    print(response)

