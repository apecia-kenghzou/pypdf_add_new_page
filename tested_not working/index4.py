from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, DictionaryObject, ArrayObject, ByteStringObject, NumberObject

reader = PdfReader("CTQ Rev7.pdf")
writer = PdfWriter()

# Copy existing pages
for page in reader.pages:
    writer.add_page(page)

# Get size from first page
first_page = reader.pages[0]
media = first_page.mediabox
width = float(media.width)
height = float(media.height)

# Add blank page with proper content stream and resources
blank_page = writer.add_blank_page(width=width, height=height)

# Create a proper content stream (empty but valid)
content_stream = ByteStringObject(b"")
content_ref = writer._add_object(content_stream)

# Set up proper page dictionary
blank_page[NameObject("/Contents")] = ArrayObject([content_ref])

# Add resources
resources = DictionaryObject({
    NameObject("/ProcSet"): ArrayObject([
        NameObject("/PDF"),
        NameObject("/Text"),
        NameObject("/ImageB"),
        NameObject("/ImageC"),
        NameObject("/ImageI"),
    ]),
    NameObject("/Font"): DictionaryObject(),
    NameObject("/XObject"): DictionaryObject(),
})

blank_page[NameObject("/Resources")] = resources

# Ensure MediaBox is properly set (though add_blank_page should do this)
blank_page[NameObject("/MediaBox")] = ArrayObject([
    NumberObject(0), 
    NumberObject(0),
    NumberObject(width), 
    NumberObject(height)
])

# Write modified file
with open("modified.pdf", "wb") as out_f:
    writer.write(out_f)

print("Done! File saved as modified.pdf")