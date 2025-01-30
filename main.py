import pdfplumber
import csv
import os

# Function to extract text and table data from a PDF file
def extract_data_from_pdf(pdf_path):
    data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract text content
            text = page.extract_text()
            if text:
                # Optionally extract specific information like invoice date or supplier name here
                print("Extracted text:", text)

            # Extract tables
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    # Filter out empty rows
                    if any(cell for cell in row):
                        data.append(row)
    return data

# Function to save extracted data to a CSV file
def save_to_csv(data, output_path):
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Directory containing the PDF files
pdf_directory = "/Users/ramonbarahona/Sites/analysis-material-price/invoices/capitalelectric"  # Replace with the path to your PDF folder
output_csv = "/Users/ramonbarahona/Sites/analysis-material-price/invoices/extracted_data.csv"

# Process each PDF file in the directory
all_data = []

for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, filename)
        print(f"Processing {filename}...")
        pdf_data = extract_data_from_pdf(pdf_path)
        all_data.extend(pdf_data)

# Save all extracted data to a single CSV
if all_data:
    save_to_csv(all_data, output_csv)
    print(f"Data saved to {output_csv}")
else:
    print("No data extracted.")
