from fpdf import FPDF
import os

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font('DejaVu', '', '/DejaVuSans.ttf', uni=True)

    def header(self):
        self.set_font("DejaVu", '', 12)

def create_translated_pdf(translated_pages, output_pdf_path):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("DejaVu", size=12)
    for page_text in translated_pages:
        pdf.multi_cell(0, 10, page_text)  
    pdf.output(output_pdf_path)

def translate_pdf(input_pdf_path, output_pdf_path):
    translated_pages = ["Translated text for page 1 • Bullet point", "Translated text for page 2"]
    create_translated_pdf(translated_pages, output_pdf_path)

def translate_pdfs_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_pdf_path = os.path.join(input_folder, filename)
            output_pdf_path = os.path.join(output_folder, f"translated_{filename}")F
            translate_pdf(input_pdf_path, output_pdf_path)
            print(f"Translated {filename} and saved as {output_pdf_path}")
input_folder = r"C:\Users\Ingrid\OneDrive\Desktop\UniTue An II Sem I\Web\tobetr"
output_folder = r"C:\Users\Ingrid\OneDrive\Desktop\UniTue An II Sem I\Web\tr"

translate_pdfs_in_folder(input_folder, output_folder)
