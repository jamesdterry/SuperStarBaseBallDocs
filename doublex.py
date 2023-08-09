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
doubleXData = [
    #10    11    12     13    14    15      16    17   18     19    20     21    22    23     24   25   26    27    28    29     30    31     32     33     34   35    36   37        38   39    
    ["BE", "PE", "(3)", "RP", "2E", "(HR)", "OI", "BE", "HB", "TP", "RD2", "CS", "C2", "KWP", "RD", "CI", "1-", "RO", "RO", "CC", "2E", "KWP", "RD", "TRB", "-", "-", "-", "-", "-", "KWP"],
]

keyData = [
    ["TP", "Triple Play if 1st & 2nd or bases loaded and no outs, DP otherwise", "RO", "Rain Out (no event if home team has roof)"],
    ["CS", "Collision, Treat as 2, Check SS & LF for injury", "C2", "Collision, Treat as 2, Check 2B & RF for injury"],
    ["CC", "Collision, Treat as 2, Check SS & CF for injury", "-", "No Event"],
    ["(HR)", "Home Run if a hit, otherwise F", "OI", "Check on deck batter for Injury"],
    ["BE", "Batter Ejected", "PE", "Pitcher Ejected"],
    ["CI", "Catchers Interference (Same as Walk)", "TRB", "Trail Runner hit by batted ball, runner out, 1 for hitter"],
    ["2E", "Possible Two Base Error, Teat as 2 or F", "(3)", "Triple, Managers Decision to try for inside park HR"],
    ["RD", "Rain (or other) Delay (both teams must change pitchers)", "HB", "Hidden Ball Trick, Lead Runner picked off"],
    ["RP", "Batter Passes Runner, (1+) but batter out if runner on first", "1-", "Single if 1B empty, runners don't advance, otherwise G"],
    ["KWP", "K but if 1B open or 2 out use Mgr Desc to see if runner reaches first", "RD2", "If runner on 3rd and 1B is empty, runner on third out in run down, any"],
    ["", "Runners advance, catchers arm lowers or raises running rating", "", "runner on 2nd to 3rd, batter to 2nd, otherwise G"],
]

# Create a PDF with 'names_ages.pdf' as the name
pdf = SimpleDocTemplate("doublex.pdf", pagesize=landscape(letter), leftMargin=10, rightMargin=10, topMargin=10, bottomMargin=10)

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

header = []
colwidths = []
for i in range(10, 40):
    header.append(Paragraph(str(i), header_style))
    colwidths.append(23)

doubleXData.insert(0, header)

# Create a Table object
doubleXTable = Table(doubleXData, colWidths=colwidths, rowHeights=[18,12])

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
doubleXTable.setStyle(table_style)

# Create a title with a style and center alignment
title_style = ParagraphStyle(
    'Title', 
    parent=getSampleStyleSheet()['Heading1'], 
    fontSize=10,
    alignment=1  # Center alignment
)
doubleXTitle = Paragraph('Double X Table', title_style)

story = []

# Double X
story.append(doubleXTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(doubleXTable)

# Key Chart
story.append(Spacer(1, 5))  # Add some space below the title
keyTable = Table(keyData, colWidths=[30,320,30,320], rowHeights=[12,12,12,12,12,12,12,12,12,12,12])
key_table_style = TableStyle([
    ('GRID', (0,0), (0,9), 1, colors.black),
    ('GRID', (2,0), (2,9), 1, colors.black),
    ('INNERPADDING', (0,0), (-1,-1), 1),
    ('OUTERPADDING', (0,0), (-1,-1), 1),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # set bold font
    ('FONTSIZE', (0,0), (-1,-1), 9),  # set font size for all cells
    ('TEXTCOLOR', (0,0), (-1,-1), colors.black),  # set text color for all cells to black
    ('LEADING', (0, 0), (-1, -1), 9),  # set leading value
    ('ALIGN', (0,0), (0,7), 'CENTER'),
    ('ALIGN', (2,0), (2,7), 'CENTER'),
])
keyTable.setStyle(key_table_style)
story.append(keyTable)

story.append(Spacer(1, 12))

# Build the PDF
pdf.build(story)
