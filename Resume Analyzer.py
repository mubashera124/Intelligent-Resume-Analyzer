#!/usr/bin/env python
# coding: utf-8

# # Intelligent Resume Analyzer

# **Context:**
# 
# Your company receives hundreds of resumes in varying formats, from scanned documents to stylized PDFs. As part of the recruitment automation initiative, your task is to design a prototype system that can extract structured candidate information from unstructured resumes.
# 
# **Objective:**
# 
# Build a Resume Analyzer system that processes resumes and extracts the following structured information for each candidate:
# 
# Full Name
# 
# Email Address
# 
# Phone Number
# 
# Skills
# 
# Education
# 
# School/College/University Name
# 
# Pass out Year
# 
# Work Experience
# 
# Company/Institute Name
# 
# Starting and Ending Month and Year
# 
# Total months of experience
# 
# Projects
# 
# Certifications (if available)
# 
# 
# 
# ### The system should output the information in JSON format like below:
# 
# json
# 
# {
#   
#   "name": "Jane Doe",
#   
#   "email": "jane.doe@example.com",
#   
#   "phone": "+1-234-567-8901",
#   
#   "skills": ["Python", "Machine Learning", "SQL"],
#   
#   "education": [...],
#   
#   "experience": [...],
#   
#   "projects": [...],
#   
#   "certifications": [...]
#   
# }

# In[13]:


# Import necessary libraries
import pymupdf  # For reading PDF files
import re  # For regular expressions (email, phone extraction)
import pytesseract  # For OCR on image files
from PIL import Image  # For opening image files
import json #To display the output in json format

# Function to analyze resume text and extract structured information
def resume_analyzer(text):

    # Splitting text in to lines
    lines = text.split('\n')

    # defining Function to extract personal details like name, email, and phone
    def extract_personal_info(lines, target_section):
        name = lines[0] if lines else ''  # First line is usually the name
        emails = []
        phones = []

        for line in lines:
            lower_lines = line.lower()

            # Extracting email using regex
            emails += re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', lower_lines)

            # Extracting phone number using regex
            phones += re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', lower_lines)

        # Return the requested section
        if target_section == 'name':
            return name
        elif target_section == 'email':
            return emails
        elif target_section == 'phone':
            return phones
        else:
            return None


    # Defining keywords for each resume section(Generalizing)
    # Because other resumes might have section heading for experience has 'work experience' or education as 'academic background'
    SECTION_HEADERS = {
        'skills': ['skills', 'technical skills', 'abilities'],
        'education': ['education', 'academic background', 'qualifications'],
        'experience': ['experience', 'work experience', 'professional experience'],
        'projects': ['projects', 'academic projects', 'personal projects'],
        'certifications': ['certifications', 'courses', 'licenses'],
        'acheivements': ['achievements', 'accomplished']
    }

    # Defining Function to extract a block of text belonging to a specific section
    def extract_section(lines, target_section):
        collected_lines = []
        collect = False  # Flag to start/stop collecting lines

        for l in lines:
            lower_line = l.lower()

            # Start collecting when section header is found
            if any(header in lower_line for header in SECTION_HEADERS[target_section]):
                collect = True
                continue

            # Stop collecting when another section header is found
            if collect and any(
                any(header in lower_line for header in headers)
                for key, headers in SECTION_HEADERS.items() if key != target_section
            ):
                break

            # If within the target section, collect the line
            if collect:
                collected_lines.append(l.strip())

        return collected_lines


    # Building final structured output in dictionary format
    parsed_data = {
        "name": extract_personal_info(lines, 'name'),
        "email": extract_personal_info(lines, 'email'),
        "phone": extract_personal_info(lines, 'phone'),
        "skills": extract_section(lines, 'skills'),
        "education": extract_section(lines, 'education'),
        "experience": extract_section(lines, 'experience'),
        "projects": extract_section(lines, 'projects'),
        "certifications": extract_section(lines, 'certifications')
    }

    # Printing the extracted structured data in readable JSON format

    print(json.dumps(parsed_data, indent=2, ensure_ascii=False))


# Wrapper function to handle different file types (PDF or image)
def Intelligent_resume_analyzer(file_path):

    file_path_lower = file_path.lower()

    # If the file is an image, extract text using OCR
    if file_path_lower.endswith(('.jpg', '.png', '.jpeg')):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        resume_analyzer(text)

    # If the file is a PDF, extract text using PyMuPDF
    elif file_path_lower.endswith('pdf'):
        doc = pymupdf.open(file_path)
        for page in doc:
            text = page.get_text()  
        resume_analyzer(text)

    else:
        return 'Unknown file'


# ### Let's test this on some sample resumes

# In[14]:


#testing on resume in pdf format
Intelligent_resume_analyzer('sample_resume2.pdf')


# In[15]:


#testing on image resume
Intelligent_resume_analyzer('sample_resume6.jpg')


# ### 🔍 Reflections & Learnings
# 
# - Learned to extract text from both PDFs and scanned images using PyMuPDF and Tesseract.
# - Understood how to use regular expressions to extract emails and phone numbers.
# - Practiced building modular, reusable code.
# - Encountered challenges with section detection and solved them by using generalized section headers.
# 
