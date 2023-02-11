from PyPDF2 import PdfReader
from pathlib import Path



#define a path
pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "Pride_and_Prejudice.pdf"
)

pdf_path = (
    Path('H:\Downloads')
    / '388-receita-federal-analise-preliminar-homologados_com-anexo.pdf' 
)

#print(type(pdf_path))

#print(pdf_path.is_file())

# open pdf
pdf = PdfReader(pdf_path)


# number of pages
print('Páginas', len(pdf.pages))

# pdf info
print('Dados: \n', pdf.metadata)

# titulo
print('Titulo: ', pdf.metadata.title)

print('Outro: ', pdf.metadata.creator)





l1 = 'Auditor-Fiscal da Receita Federal do Brasil'
l2 = ''

# get a page by the number
#first_page = pdf.pages[0]

#print(type(first_page))



#print(first_page.extract_text())

conta1 = 0
conta2 = 0

#for page in pdf.pages:
for i in range(1, len(pdf.pages)):
    
    page = pdf.pages[i]
    
    print(page.extract_text())
    break


