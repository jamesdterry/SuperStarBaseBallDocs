from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import Color
from reportlab.lib import colors

def hex_to_color(hex_value):
    """
    Convert a hex color value to a ReportLab Color object.

    Args:
    - hex_value (str): The hex color value, e.g., "#RRGGBB".

    Returns:
    - A ReportLab Color object.
    """
    hex_value = hex_value.lstrip("#")
    r, g, b = tuple(int(hex_value[i:i+2], 16)/255.0 for i in (0, 2, 4))
    return Color(r, g, b)

# Prepare data for the table
secondData = [
    #     10   11   12   13   14   15   16   17   18   19    20   21   22   23   24   25   26   27   28      29     30   31     32   33     34   35   36   37   38   39    
    ["0", "O", "O", "O", "P", "E", "O", "O", "O", "O", "BK", "O", "O", "O", "O", "O", "O", "O", "O", "S",    "S+E", "O", "O",   "O", "S",   "S", "S", "O", "S", "S", "S+E"],
    ["1", "BK", "O", "S", "P", "E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S+E",  "O",   "O", "O",   "S", "S",   "S", "S", "S", "S", "S", "S+E"],
    ["2", "O", "BK", "S", "P", "E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "S", "S", "S",    "S",   "S", "S+E", "S", "S",   "S", "S", "S", "S", "S", "S"],
    ["3", "O", "O", "S", "P", "E", "O", "S", "O", "O", "O",  "O", "O", "O", "O", "O", "S", "S", "S", "S",    "S+E", "S", "S+E", "S", "S",   "S", "S", "S", "S", "S", "BK"],
    ["4", "O", "BK", "S", "P", "E", "O", "O", "O", "O", "BK", "O", "O", "O", "O", "S", "S", "S", "S", "S+E", "S",   "S", "S+E", "S", "S",   "S", "S", "S", "S", "S", "S"],
    ["5", "O", "O", "O", "P", "E", "S", "O", "S", "O", "S",  "O", "O", "O", "S", "S", "S", "S", "S", "BK",    "S",  "S", "S",   "S", "S+E", "S", "S", "S", "S", "S", "S"],
]

thirdData = [
    #     10    11   12    13   14   15   16   17   18   19    20   21   22   23   24   25   26   27   28     29     30   31     32   33   34   35   36   37   38   39    
    ["0", "O",  "E", "O",  "O", "O", "O", "O", "P", "O", "BK", "O", "O", "O", "O", "O", "O", "O", "O", "O",   "O",   "O", "O",   "O", "S", "S", "S", "O", "S", "S", "S+E"],
    ["1", "O",  "E", "O",  "O", "O", "O", "O", "P", "O", "BK", "O", "O", "O", "O", "O", "O", "O", "O", "O",   "S+E", "O", "O",   "S", "S", "S", "S", "S", "S", "S", "S+E"],
    ["2", "BK", "E", "O",  "O", "O", "O", "O", "P", "O", "S",  "O", "O", "O", "O", "O", "O", "O", "S", "S+E", "S",   "S", "S",   "S", "S", "S", "S", "S", "S", "S", "S+E"],
    ["3", "BK", "E", "O",  "O", "O", "O", "O", "P", "O", "O",  "O", "O", "O", "O", "O", "S", "S", "S", "S",   "S",   "S", "S+E", "S", "S", "S", "S", "S", "S", "S", "S"],
    ["4", "O",  "E", "O",  "S", "O", "O", "O", "P", "O", "O",  "O", "O", "O", "O", "S", "S", "S", "S", "S",   "S+E", "S", "S+E", "S", "S", "S", "S", "S", "S", "S", "BK"],
    ["5", "O",  "E", "BK", "O", "O", "O", "O", "P", "O", "O",  "O", "O", "O", "S", "S", "S", "S", "S", "S+E", "S",   "S", "S+E", "S", "S", "S", "S", "S", "S", "S", "O"],
]

homeData = [
    #     10   11    12    13     14   15   16   17   18    19   20   21   22   23   24   25   26   27   28     29     30   31   32   33   34   35   36   37   38     39    
    ["0", "P", "O",  "O",  "S",   "O", "O", "O", "O", "BK", "E", "O", "O", "O", "O", "O", "O", "O", "O", "O",   "O",   "O", "O", "O", "O", "O", "O", "O", "O", "O",   "S+E"],
    ["1", "P", "S",  "O",  "O",   "O", "S", "S", "S", "BK", "E", "O", "O", "O", "O", "O", "O", "O", "O", "O",   "O",   "O", "O", "O", "O", "O", "O", "O", "O", "O",   "S+E"],
    ["2", "P", "O",  "O",  "O",   "S", "S", "S", "S", "BK", "O", "O", "O", "O", "O", "O", "O", "S", "S", "S+E", "E",   "O", "O", "O", "O", "O", "O", "O", "O", "O",   "O"],
    ["3", "P", "BK", "S",  "O",   "O", "O", "O", "O", "E",  "O", "O", "O", "O", "O", "O", "O", "O", "O", "S",   "S+E", "S", "S", "O", "O", "O", "O", "S", "S", "S",   "S+E"],
    ["4", "P", "BK", "S",  "O",   "O", "O", "O", "E", "S",  "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",   "O",   "O", "O", "O", "O", "S", "S", "S", "S", "S+E", "O"],
    ["5", "P", "E",  "BK", "S+E", "O", "O", "O", "O", "O",  "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",   "S+E", "S", "S", "O", "O", "S", "S", "S", "S", "0",   "O"],
]

managerData = [
    #     10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39    
    ["0", "O", "O", "E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["1", "O", "O+", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["2", "S", "O+", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["3", "O+", "E", "E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["4", "O", "E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
    ["5", "O+", "E", "S", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "S", "S", "O"],
]

keyData = [
    ["S", "Stolen Base", "O", "Runner thrown out, other runners attemping to steal advance 1 base"],
    ["S+E", "Stolen Base plus Error - All Runners advance another base on the error", "P", "Runner picked off, other runners hold"],
    ["E", "Runner safe on Error - Other runners attemping to steal advance 1 base", "BK", "Balk - All runners advance one base"],
]

key2Data = [
    ["S", "Runner Safe - All runners not trying to advance hold", "E", "Runner safe on Error - All runners not trying to advance hold"],
    ["S+E", "Stolen Safe PLUS error - All runners advance an extra base on the error", "O+", "Runner out - All runners behind the runner advance 1 base"],
    ["S+", "Runner Safe - All runners behind the runner advance 1 base", "O", "Runner out - All runners not trying to advance hold"],
]

# Create a PDF with 'names_ages.pdf' as the name
pdf = SimpleDocTemplate("running.pdf", pagesize=landscape(letter), leftMargin=10, rightMargin=10, topMargin=10, bottomMargin=10)

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
    leading=12,
    parent=getSampleStyleSheet()['Heading1'], 
    fontSize=9,  # set font size
    textColor=colors.black,  # set font color
)

header = [Paragraph('Rating', header_style)]
colwidths = [40]
for i in range(10, 40):
    header.append(Paragraph(str(i), header_style))
    colwidths.append(23)

secondData.insert(0, header)
thirdData.insert(0, header)
homeData.insert(0, header)
managerData.insert(0, header)

# Create a Table object
secondTable = Table(secondData, colWidths=colwidths, rowHeights=[18,12,12,12,12,12,12])
thirdTable = Table(thirdData, colWidths=colwidths, rowHeights=[18,12,12,12,12,12,12])
homeTable = Table(homeData, colWidths=colwidths, rowHeights=[18,12,12,12,12,12,12])
managerTable = Table(managerData, colWidths=colwidths, rowHeights=[18,12,12,12,12,12,12])

table_style = TableStyle([
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), hex_to_color("#CCCCCC")),
    ('INNERPADDING', (0,0), (-1,-1), 1),
    ('OUTERPADDING', (0,0), (-1,-1), 1),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # set bold font
    ('FONTSIZE', (0,0), (-1,-1), 9),  # set font size for all cells to 9
    ('TEXTCOLOR', (0,0), (-1,-1), colors.black),  # set text color for all cells to black
    ('LEADING', (0, 0), (-1, -1), 9),  # set leading value
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),  # center text in all cells
])
secondTable.setStyle(table_style)
thirdTable.setStyle(table_style)
homeTable.setStyle(table_style)
managerTable.setStyle(table_style)

# Create a title with a style and center alignment
title_style = ParagraphStyle(
    'Title', 
    parent=getSampleStyleSheet()['Heading1'], 
    fontSize=10,
    alignment=1  # Center alignment
)
secondTitle = Paragraph('Steal of Second Base', title_style)
thirdTitle = Paragraph('Steal of Third Base', title_style)
homeTitle = Paragraph('Steal of Home', title_style)
managerTitle = Paragraph("Manager's Decision Chart (referred to by results including parenthesis)", title_style)


story = []

# Steal of Second
story.append(secondTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(secondTable)

story.append(Spacer(1, 12))

# Steal of Third
story.append(thirdTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(thirdTable)

story.append(Spacer(1, 12))

# Steal of Home
story.append(homeTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(homeTable)

# Key Chart
story.append(Spacer(1, 5))  # Add some space below the title
keyTable = Table(keyData, colWidths=[24,320,24,320], rowHeights=[12,12,12])
key_table_style = TableStyle([
    ('GRID', (0,0), (0,2), 1, colors.black),
    ('GRID', (2,0), (2,2), 1, colors.black),
    ('INNERPADDING', (0,0), (-1,-1), 1),
    ('OUTERPADDING', (0,0), (-1,-1), 1),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # set bold font
    ('FONTSIZE', (0,0), (-1,-1), 9),  # set font size for all cells
    ('TEXTCOLOR', (0,0), (-1,-1), colors.black),  # set text color for all cells to black
    ('LEADING', (0, 0), (-1, -1), 9),  # set leading value
    ('ALIGN', (0,0), (0,2), 'CENTER'),
    ('ALIGN', (2,0), (2,2), 'CENTER'),
])
keyTable.setStyle(key_table_style)
story.append(keyTable)

story.append(Spacer(1, 12))

story.append(managerTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(managerTable)

# Key 2 Chart
story.append(Spacer(1, 5))  # Add some space below the title
key2Table = Table(key2Data, colWidths=[24,320,24,320], rowHeights=[12,12,12])
key2Table.setStyle(key_table_style)
story.append(key2Table)

# Build the PDF
pdf.build(story)
