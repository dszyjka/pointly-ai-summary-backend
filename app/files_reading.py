import filetype
import fitz
import docx
import io


async def _check_file_type(file):
    header_bytes = await file.read(256)
    kind = filetype.guess(header_bytes)
    await file.seek(0)
    return kind
    
async def extract_text(file):
    kind = await _check_file_type(file)

    if kind is None:
        text = await _read_txt(file)

    elif kind.mime == 'application/pdf':
        text = await _read_pdf(file)

    elif kind.mime in [
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        ]:
        text = await _read_docx(file)

    return text

async def _read_txt(file):
    text = await file.read()
    return text.decode('utf-8')

async def _read_docx(file):
    content = await file.read()
    doc = docx.Document(io.BytesIO(content))
    return "\n".join([para.text for para in doc.paragraphs])

async def _read_pdf(file):
    content = await file.read()

    doc = fitz.open(stream=content, filetype='pdf')
    text = ''
    for page in doc:
        text += page.get_text()
    return text