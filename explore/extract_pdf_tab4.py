import PyPDF2

# Đường dẫn file PDF
pdf_path = '../model/tab4_guideline.pdf'

# Đọc nội dung PDF
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'

# Hiển thị một phần nội dung để kiểm tra
print(text[:2000])  # In ra 2000 ký tự đầu tiên