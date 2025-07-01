const fs = require('fs');
const { PDFDocument } = require('pdf-lib');

async function createValidBlankPage(pdfDoc, width, height) {
  const blankPage = pdfDoc.addPage([width, height]);
  return blankPage;
}

async function main() {
  const existingPdfBytes = fs.readFileSync('original.pdf');
  const pdfDoc = await PDFDocument.load(existingPdfBytes);

  const copiedPages = await pdfDoc.copyPages(pdfDoc, pdfDoc.getPageIndices());
  //copiedPages.forEach(page => pdfDoc.addPage(page));

  const { width: firstPageWidth, height: firstPageHeight } = pdfDoc.getPage(0).getSize();

  for (let i = 0; i < 25; i++) {
    createValidBlankPage(pdfDoc, firstPageWidth, firstPageHeight);
  }

  const modifiedPdfBytes = await pdfDoc.save();
  fs.writeFileSync('modified.pdf', modifiedPdfBytes);

  console.log('PDF creation successful.');
}

main();
