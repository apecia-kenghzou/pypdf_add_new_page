from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    NameObject,
    DictionaryObject,
    ArrayObject,
    NumberObject,
    StreamObject
)

def create_valid_blank_page(writer, width, height):
    """Create a PDF-me compatible blank page using add_blank_page"""
    # First create a blank page using the standard method
    blank_page = writer.add_blank_page(width=width, height=height)
    
    # Now ensure it has all required elements
    if "/Contents" not in blank_page:
        # Create empty content stream
        stream = StreamObject()
        stream._data = b""
        stream[NameObject("/Length")] = NumberObject(0)
        content_ref = writer._add_object(stream)
        blank_page[NameObject("/Contents")] = ArrayObject([content_ref])
    
    # Ensure resources exist
    if "/Resources" not in blank_page:
        blank_page[NameObject("/Resources")] = DictionaryObject({
            NameObject("/ProcSet"): ArrayObject([
                NameObject("/PDF"),
                NameObject("/Text"),
                NameObject("/ImageB"),
                NameObject("/ImageC"),
                NameObject("/ImageI")
            ]),
            NameObject("/Font"): DictionaryObject(),
            NameObject("/XObject"): DictionaryObject()
        })
    
    # Explicitly set page type if missing
    if "/Type" not in blank_page:
        blank_page[NameObject("/Type")] = NameObject("/Page")
    
    return blank_page

def main():
    # Initialize reader and writer
    reader = PdfReader("original.pdf")
    writer = PdfWriter()

    # Add existing pages
    for page in reader.pages:
        writer.add_page(page)

    # Create and add new blank page
    media_box = reader.pages[0].mediabox
  #  blank_page = create_valid_blank_page(writer, 
  #                                    float(media_box.width),
  #                                    float(media_box.height))
    for _ in range(25):
        create_valid_blank_page(writer, 
                                      float(media_box.width),
                                      float(media_box.height))
    # Write output
    with open("modified.pdf", "wb") as f:
        writer.write(f)

    print("PDF creation successful. Safe to use with pdfme.")

if __name__ == "__main__":
    main()