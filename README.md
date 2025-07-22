📘 PDF Content Analyzer and Question Generator
Welcome to PDF-Content-Analyzer-and-Question-Generator, a Python project that automates the extraction of textual and visual content from educational PDFs and simulates AI-powered question generation using image-based templates.

This tool was developed as part of an AI/Python internship assignment and is tailored for use in digitizing educational content, especially for Olympiad-style exam papers.

🧠 Project Objectives
Extract all text and images from a structured PDF (e.g., Class 1 Maths Olympiad)
Organize extracted content in a structured JSON format
Use basic AI logic (template-based) to generate questions from images
Save the generated questions in a format that can be reused or evaluated

🛠️ Technologies Used
Component	Description
Python 3.x	Core language used for scripting
pdfplumber	Text extraction from PDF pages
PyMuPDF (fitz)	Image extraction from PDF pages
Pillow	Image manipulation and saving
json	Data structure to store and export results


📂 Project Structure
PDF-Content-Analyzer-and-Question-Generator/
│
├── extract_pdf.py                # Script for text + image extraction
├── generate_questions.py         # Script for AI-style question generation
├── extracted_content.json        # Structured text + image paths per page
├── generated_questions.json      # Output MCQs generated from image logic
├── images/                       # Folder containing extracted images
│   ├── page1_image1.png
│   ├── page2_image3.png
│   └── ... (few key images only)


🔍 How It Works
1️⃣ extract_pdf.py
Loads the PDF file

Extracts text from each page using pdfplumber

Extracts images from each page using fitz (PyMuPDF)

Saves everything to extracted_content.json in the format:
{
  "page": 1,
  "text": "Page text here...",
  "images": ["images/page1_image1.png", "images/page1_image2.png"]
}

2️⃣ generate_questions.py
Takes labeled images (e.g., "clock", "pattern", "money")

Applies template logic to generate questions

Outputs to generated_questions.json:
{
  "question": "What time is shown on the clock?",
  "image": "images/page3_image1.png",
  "options": ["4:00", "4:30", "5:00", "5:30"],
  "answer": "4:30"
}

🧠 Sample Use Cases
Create practice worksheets for school exams

Build datasets for educational AI systems

Help teachers generate visual-based MCQs

Use structured content for further ML/NLP training

🚀 Getting Started
🔧 1. Install dependencies
pip install pdfplumber pymupdf pillow
📄 2. Run PDF Extraction
Make sure the PDF is in your working folder, then run:
python extract_pdf.py
This generates:

extracted_content.json

images/ folder with visuals

🧠 3. Generate Questions
Label the image types in image_labels inside generate_questions.py, then run:
python generate_questions.py
This creates:

generated_questions.json with MCQs

📊 Example Output
From extracted_content.json

{
  "page": 2,
  "text": "Complete the number pattern...",
  "images": ["images/page2_image1.png"]
}
From generated_questions.json

{
  "question": "What is the next figure in the pattern?",
  "image": "images/page2_image1.png",
  "options": ["A", "B", "C", "D"],
  "answer": "D"
}
✅ Features
📄 Multi-page PDF parsing

🖼️ Accurate image detection and cropping

🤖 AI-style template-based MCQ generation

🔁 Fully reusable and modular



🙋‍♀️ Author
👩‍💻 Varsha Vangasam



