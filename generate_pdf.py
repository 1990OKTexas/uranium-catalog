import os
import sys
from weasyprint import HTML

def compile_catalog_pdf(input_file="catalog.html", output_file="uranium_glass_horology_catalog.pdf"):
    # Fallback to index.html if catalog.html isn't present
    if not os.path.exists(input_file):
        if os.path.exists("index.html"):
            input_file = "index.html"
        else:
            print(f"Error: Neither '{input_file}' nor 'index.html' was found.")
            sys.exit(1)

    print(f"Rendering '{input_file}' to '{output_file}'...")
    
    # Generate the PDF
    HTML(filename=input_file, base_url=os.path.abspath(".")).write_pdf(output_file)
    
    file_size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"Catalog PDF generated successfully: {output_file} ({file_size_mb:.2f} MB)")

if __name__ == "__main__":
    compile_catalog_pdf()
  
