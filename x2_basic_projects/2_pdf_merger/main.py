import PyPDF2

# Create a merger object
merger = PyPDF2.PdfMerger()

# List of PDF files to merge (order matters)
pdf_files = ["file1.pdf", "file2.pdf"]

# Append each PDF to the merger
for pdf in pdf_files:
    merger.append(pdf)

# Save the merged PDF
merger.write("merged_output.pdf")
merger.close()

print("PDFs merged successfully into 'merged_output.pdf'")
