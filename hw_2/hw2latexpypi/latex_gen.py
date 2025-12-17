def generate_latex_table(rows):
    col_num = max(len(r) for r in rows)
    header = "\\begin{tabular}{" + " | ".join(["c"]*col_num) + "}\n\\hline\n"

    lines = [
        " & ".join(map(str, r)) + " \\\\ \\hline"
        for r in rows
    ]
    body = "\n".join(lines) + "\n"
    footer = "\\end{tabular}"

    res = header + body + footer

    return res

def latex_import_picture(path="hw_2_image.jpg"):
    return (
        "\\begin{figure}[h!]\n"
        "\\centering\n"
        f"\\includegraphics[width={10}cm]{{\"{path}\"}}\n"
        "\\end{figure}\n"
    )