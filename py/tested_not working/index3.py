import fitz  # PyMuPDF

doc = fitz.open("CTQ Rev7.pdf")

# Add a blank page
doc.new_page(width=doc[0].rect.width, height=doc[0].rect.height)

# Save
doc.save("modified.pdf")
