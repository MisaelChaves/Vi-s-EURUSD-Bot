import fitz  # PyMuPDF
from coletor import coletar_cpi

def analisar_pdf(filepath):
    doc = fitz.open(filepath)
    texto = ""
    for page in doc:
        texto += page.get_text()

    dados_cpi = coletar_cpi()
    resposta = f"🧠 Análise baseada no PDF enviado:\n\nResumo do texto:\n{texto[:500]}...\n\n📈 Dados CPI atuais:\n{dados_cpi}"
    return resposta
