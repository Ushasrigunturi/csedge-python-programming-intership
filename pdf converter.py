import PyPDF2

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text
from pdf2image import convert_from_path

def pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image_path = f"{output_folder}/page_{i+1}.png"
        image.save(image_path, 'PNG')
        print(f"Saved: {image_path}")
from docx import Document

def pdf_to_word(pdf_path, output_docx_path):
    text = pdf_to_text(pdf_path)
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_docx_path)
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Convert PDF files to different formats.")
    parser.add_argument('pdf_path', help="Path to the PDF file")
    parser.add_argument('--text', help="Output path for text file")
    parser.add_argument('--images', help="Output folder for images")
    parser.add_argument('--word', help="Output path for Word document")

    args = parser.parse_args()

    if args.text:
        text = pdf_to_text(args.pdf_path)
        with open(args.text, 'w') as file:
            file.write(text)
        print(f"Text saved to {args.text}")

    if args.images:
        if not os.path.exists(args.images):
            os.makedirs(args.images)
        pdf_to_images(args.pdf_path, args.images)

    if args.word:
        pdf_to_word(args.pdf_path, args.word)
        print(f"Word document saved to {args.word}")

if __name__ == "__main__":
    main()