## 🧠 **Intelligent Resume Analyzer**

The Intelligent Resume Analyzer is a prototype system that extracts structured candidate information from unstructured resumes, including PDFs and image-based files. It aims to automate the resume screening process by identifying key details such as name, contact, skills, education, experience, and more.

**📌 Features**

**✅ Extracts data from both PDF and image (JPG/PNG) resumes**

🔍 Uses **PyMuPDF** for PDF parsing and **pytesseract** for OCR on images

🧾 Retrieves:

Full Name

Email Address

Phone Number

Skills

Education

Experience

Projects

Certifications

**📦 Outputs clean and structured data in JSON format**

## 🧠 My Thought Process: A Creative Walkthrough

Building the Intelligent Resume Analyzer wasn’t just about writing code — it was about thinking like a detective, decoding clues hidden in messy formats, and crafting a system that **sees the unseen**. Here’s how I approached the challenge:

---

### 🕵️‍♀️ 1. The Mystery Begins: Understanding the Challenge

Resumes don’t come in neat little boxes — they’re creative, scattered, and sometimes even scanned like treasure maps. My first task? **Map the chaos**. I imagined the resume as a puzzle and my job as stitching it together into clean, structured data.

---

### 🧪 2. File Forensics: Decoding Resume Types

Every resume had its own story — some whispered in `.pdf`, others shouted in `.jpg` and `.png`. I created a smart gatekeeper that knew which path to take — **OCR for images**, **text scraping for PDFs**.

---

### 🧼 3. Raw Material: Extracting the Uncut Text

Text is like unrefined gold — messy, noisy, unstructured. I used `pytesseract` to pull words out of pixels and `PyMuPDF` to grab words hidden inside PDFs. What I got was a **raw dump** of potential waiting to be shaped.

---

### 🪄 4. From Chaos to Clarity: Line-by-Line Alchemy

I split the soup of text into clean lines, preparing it for the next phase: **intelligent extraction**. This gave me precise control — like flipping through the pages of a diary instead of skimming a novel.

---

### 🎯 5. Sherlock Mode: Extracting Key Personal Details

Armed with **regex**, I became a digital detective:
- Sniffed out emails like a spam filter on steroids  
- Tracked phone numbers hiding in different formats  
- Assumed the top line held the candidate’s name — like a resume’s opening line in a play

---

### 🧱 6. Blueprint Builder: Structuring Sectional Data

Instead of relying on fixed positions, I let the **data speak**. I taught my analyzer to recognize signals like “Skills” or “Education” and **dynamically capture content** until the next clue appeared. Think of it like a smart reader that knows when one chapter ends and another begins.

---

### 📦 7. The Grand Reveal: Packaging the Insight

All my detective work came together in a neat JSON box — **structured, clean, and easy to read**. A résumé no longer just looked good — it **spoke clearly**.

---

### 💡 Beyond Code: The Bigger Idea

This wasn’t just a Python script — it was a **mini AI agent**, built to make sense of real-world chaos. It blended vision (OCR), logic (regex), and understanding (section detection) — all in a compact and practical tool.  
That’s the kind of thinking I bring to the table.

## 📊 Resume Parsing Flow

                ┌────────────────────┐
                │  Resume File Input │
                └────────┬───────────┘
                         │
       ┌────────────────┴───────────────┐
       │                                │



📘 Modular and well-commented code for easy understanding

**🛠️ Tech Stack**
Python 🐍

PyMuPDF – For PDF text extraction

pytesseract – For OCR from images

Pillow – For image processing

Regular Expressions – For extracting emails, phone numbers, etc.
