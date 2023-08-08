from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Prepare data for the table
data = [
    ["0", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["1", "O", "S+E", "BK", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["2", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["3", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["4", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["5", "O", "S", "S", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
]

# Create a PDF with 'names_ages.pdf' as the name
pdf = SimpleDocTemplate("names_ages.pdf", pagesize=landscape(letter))

# Define a style for the table
table_text_style = ParagraphStyle(
    'Table', 
    parent=getSampleStyleSheet()['BodyText'], 
    fontSize=8,  # set font size
    textColor=colors.black,  # set font color
    fontName='Helvetica',  # set font
)

# Convert all data to Paragraphs with the table text style
#for i in range(0, len(data)):
#    data[i] = [Paragraph(str(cell), table_text_style) for cell in data[i]]

# Define a style for the header
styles = getSampleStyleSheet()
header_style = ParagraphStyle(
    'Header', 
    parent=getSampleStyleSheet()['Heading1'], 
    fontSize=9,  # set font size
    textColor=colors.black,  # set font color
)

header = [Paragraph('Rating', header_style)]
colwidths = [None]
for i in range(10, 40):
    header.append(Paragraph(str(i), header_style))
    colwidths.append(23)

data.insert(0, header)

# Create a Table object
table = Table(data, colWidths=colwidths)

table_style = TableStyle([
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('INNERPADDING', (0,0), (-1,-1), 0),  # reduce cell padding to 1 point
    ('FONTSIZE', (0,0), (-1,-1), 9),  # set font size for all cells to 14
    ('TEXTCOLOR', (0,0), (-1,-1), colors.black),  # set text color for all cells to black
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),  # center text in all cells
])
table.setStyle(table_style)

# Create a title with a style and center alignment
title_style = ParagraphStyle(
    'Title', 
    parent=getSampleStyleSheet()['Heading1'], 
    fontSize=16,
    alignment=1  # Center alignment
)
title = Paragraph('Steal of Second Base', title_style)

# Add the Table object to the PDF
story = []
story.append(title)  # Add the title to the story
story.append(Spacer(1, 8))  # Add some space below the title
story.append(table)

# Build the PDF
pdf.build(story)
