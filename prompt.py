q = {
    "sumarize_resume": """Return a summary from the bellow curriculum information. \
Provide your response as a JSON object with the following schema: \
{{"Name", "Email", "Phone number", "LinkedInUrl", "Year", "Seniority", \
"Years of experience", "English Level", "experience": ["", "", ...], \
"Programing Languages": ["", "", ... ], "Education": ["", "", ...], \
"Other skills": ["", "", ...], "Additional information": ["", "", ...], \
"Willing to relocate"}}:

{resume}""",

"qualify_resume": """I looking for a Java software engineer with the following skills: 

{job}
    
How well the following profile matches, from 1 to 10 what score you assign to this profile \
and if we should continue/reject with the process review:

{resume}"""
}