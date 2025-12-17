from hw2latexpypi.latex_gen import generate_latex_table, latex_import_picture

table_for_test = [
    ["Name", "Age", "Sphere"],
    ["Matt", 23, "ML"],
    ["Dan", 22, "Backend"],
    ["Leon", 24, "Analytics"],
    ["Pitt", 22, "Backend"],
    ["Kir", 21, "ML"],
]

with open("result_table_2.tex", "w", encoding="utf-8") as f:
    f.write("\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n")
    f.write(generate_latex_table(table_for_test))
    f.write(latex_import_picture())
    f.write("\n\\end{document}\n")