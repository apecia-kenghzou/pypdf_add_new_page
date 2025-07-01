from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# --- create the new page ---
packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFont("Helvetica", 14)
can.drawString(72, 720, "This is my newly added page!")
can.showPage()
can.save()
packet.seek(0)
new_page_pdf = PdfReader(packet)

# --- read the existing PDF ---
reader = PdfReader("CTQ Rev7.pdf")
writer = PdfWriter()

# --- copy original pages ---
for page in reader.pages:
    writer.add_page(page)

# --- append new page ---
writer.add_page(new_page_pdf.pages[0])

# --- write out ---
with open("modified.pdf", "wb") as out_f:
    writer.write(out_f)

print("Done! See modified.pdf")
