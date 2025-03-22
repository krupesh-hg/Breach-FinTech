# import fitz  # PyMuPDF

# def extract_text_from_pdf(pdf_path):
#     text = ""
#     with fitz.open(pdf_path) as doc:
#         for page in doc:
#             text += page.get_text("text") + "\n"
#     return text.strip()

# user_compliance_text = extract_text_from_pdf("uploaded_file.pdf")
# print("User Compliance Rules:", user_compliance_text)

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text.strip()
