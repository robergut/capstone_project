#!/usr/bin/env python3

from brain_module import ChatGPT
from prompt import q
from read_doc import read_docx, read_profile

if  __name__ == "__main__":
    profile = read_profile('job_description.txt')
    resume = read_docx('resume.docx')

    question_1 = q["sumarize_resume"].format(resume = resume)
    question_2 = q["qualify_resume"].format(job = profile, resume = resume)

    bot = ChatGPT()
    response = bot.request_openai(question_1)
    print(response)
    response = bot.request_openai(question_2)
    print(response)

