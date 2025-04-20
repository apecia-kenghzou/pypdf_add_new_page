# Add after writing
from pypdf import PdfReader
test_reader = PdfReader("modified.pdf")
test_reader.pages[2].extract_text()  # Shouldn't throw errors