from pypdf import PdfReader, PdfWriter

# --- read the existing PDF ---
reader = PdfReader("CTQ Rev7.pdf")
writer = PdfWriter()

# --- copy original pages ---
for page in reader.pages:
    writer.add_page(page)

# --- determine blank‐page size from the first page ---
first_page = reader.pages[0]
media = first_page.mediabox
width = float(media.width)
height = float(media.height)

# --- append 50 blank pages ---
for _ in range(1):
    writer.add_blank_page(width=width, height=height)

# --- write out the modified PDF ---
with open("modified.pdf", "wb") as out_f:
    writer.write(out_f)

print("Done! See modified.pdf")
