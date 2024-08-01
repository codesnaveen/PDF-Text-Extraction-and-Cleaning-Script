import re
import PyPDF2

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    full_text = []
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        full_text.append(text)
    return '\n'.join(full_text)

def remove_figures_tables(text):
    # Use regex or other text processing techniques to remove figures and tables
    # Example regex pattern: r'\[Figure \d+\]|Table \d+'
    cleaned_text = re.sub(r'\[Figure \d+\]|Table \d+', '', text)
    return cleaned_text

def remove_in_text_citations(text):
    # Use regex to remove in-text citations
    # Example regex pattern: r'\(\w+ \d+\)'
    cleaned_text = re.sub(r'\(\w+ \d+\)', '', text)
    return cleaned_text

# Example usage
pdf_file_path = '/content/drive/MyDrive/Publications/1_Ramırez-Duque_.pdf'
extracted_text = extract_text_from_pdf(pdf_file_path)
cleaned_text = remove_figures_tables(extracted_text)
final_text = remove_in_text_citations(cleaned_text)

# Save final_text to a clean text file
with open('cleaned_text.txt', 'w') as file:
    file.write(final_text)
    print(final_text)
