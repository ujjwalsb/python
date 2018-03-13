import PyPDF2

pdfFileObj = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


print(pdfReader.isEncrypted)		# To check if it is password protected.
# pdfReader.decrypt('password')		# If thereis a password.

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())