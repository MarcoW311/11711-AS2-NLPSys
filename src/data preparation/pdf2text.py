from PyPDF2 import PdfReader 
import spacy 

# change path to pdf file
reader = PdfReader("output/2023.acl-long.26.pdf")

# extract all pages
pages = reader.pages
text = ""
for page in pages:
    text += page.extract_text()

text = text.replace("-\n", "")
text = text.replace("\n", " ")


text = ".\n".join(text.split(". "))

# tokenize
nlp = spacy.load("en_core_web_lg")
doc = nlp(text)
output = ""
for sentence in doc.sents:
    output += " ".join([token.text for token in sentence])

with open("tokenizedText26.txt", "w") as f:
    f.write(output)

