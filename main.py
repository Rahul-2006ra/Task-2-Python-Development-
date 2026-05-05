import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def analyze_data(df):
    """Returns summary statistics."""
    summary = {
        "Total Records": len(df),
        "Average Score": round(df["Score"].mean(), 2),
        "Highest Score": df["Score"].max(),
        "Lowest Score": df["Score"].min()
    }
    return summary


def generate_pdf(input_file, output_pdf):
    # Reading CSV file
    df = pd.read_csv(input_file)
    summary = analyze_data(df)

    # PDF setup
    doc = SimpleDocTemplate(output_pdf, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Title
    title = Paragraph("<b><font size=20>AUTOMATED REPORT</font></b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 20))

    # Summary Section
    elements.append(Paragraph("<b>Summary Report</b>", styles["Heading2"]))
    summary_data = [[key, str(value)] for key, value in summary.items()]

    summary_table = Table(summary_data, colWidths=[200, 200])
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 20))

    # Data Table Section
    elements.append(Paragraph("<b>Dataset</b>", styles["Heading2"]))

    table_data = [list(df.columns)] + df.values.tolist()

    data_table = Table(table_data, colWidths=[150, 100, 100])
    data_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey])
    ]))
    elements.append(data_table)

    # Generate PDF
    doc.build(elements)
    print(f"PDF Report '{output_pdf}' Generated Successfully!")


# Run the script
if __name__ == "__main__":
    generate_pdf("data.csv", "Automated_Report.pdf")
