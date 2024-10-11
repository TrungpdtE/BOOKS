import pypandoc
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document

def convert_docx_to_pdf(input_path, output_path):
    """
    Chuyen doi tep DOCX sang PDF chat luong cao.

    :param input_path: Duong dan den tep DOCX dau vao.
    :param output_path: Duong dan de luu tep PDF dau ra.
    """
    # Chuyen doi DOCX sang HTML su dung pypandoc
    html_content = pypandoc.convert_file(input_path, 'html')

    # Tao tai lieu PDF su dung reportlab
    pdf = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Them noi dung HTML vao PDF
    pdf.drawString(30, height - 30, html_content)

    # Luu PDF
    pdf.save()

# Vi du su dung
input_docx = "image.docx"
output_pdf = "/ / /.pdf"
convert_docx_to_pdf(input_docx, output_pdf)