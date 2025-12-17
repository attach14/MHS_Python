import subprocess
from hw2latexpypi import generate_latex_table, latex_import_picture

table_for_test = [
    ["Name", "Age", "Sphere"],
    ["Matt", 23, "ML"],
    ["Dan", 22, "Backend"],
    ["Leon", 24, "Analytics"],
    ["Pitt", 22, "Backend"],
    ["Kir", 21, "ML"],
]

tex_name = "temp_table.tex"
pdf_name = "result_file.pdf"

with open(tex_name, "w", encoding="utf-8") as f:
    f.write(
        "\\documentclass{article}\n"
        "\\usepackage{graphicx}\n"
        "\\begin{document}\n"
        + generate_latex_table(table_for_test)
        + latex_import_picture()
        + "\n\\end{document}\n"
    )

subprocess.run(["pdflatex", tex_name], check=True)