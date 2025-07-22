import os
import json
import fitz  # PyMuPDF
import pdfplumber

pdf_path = r"C:\Users\vanga\OneDrive\Desktop\testline\IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
image_folder = "images"

def extract_text_from_pdf(path):
    content = []
    with pdfplumber.open(path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            content.append({
                "page": page_num,
                "text": text.strip() if text else ""
            })
    return content

def extract_images_from_pdf(path, image_folder="images"):
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    doc = fitz.open(path)
    image_map = {}

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        images = page.get_images(full=True)
        image_paths = []

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_name = f"page{page_index + 1}_image{img_index + 1}.{image_ext}"
            image_path = os.path.join(image_folder, image_name)

            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)

            image_paths.append(image_path)

        image_map[page_index + 1] = image_paths

    return image_map

def save_text_to_json(data, output_path="extracted_content.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    text_data = extract_text_from_pdf(pdf_path)
    image_data = extract_images_from_pdf(pdf_path)

    structured_output = []

    for page in text_data:
        page_num = page["page"]
        structured_output.append({
            "page": page_num,
            "text": page["text"],
            "images": image_data.get(page_num, [])
        })

    save_text_to_json(structured_output)
    print("✅ Extraction complete. Check extracted_content.json and images/")

