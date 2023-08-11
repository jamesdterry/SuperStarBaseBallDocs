from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import Color
from reportlab.lib import colors
from rotated_text import RotatedText

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

# Error Determiniation
errorData = [
    #               10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27    28    29    30    31    32    33    34    35    36    37    38    39    
    ["Batting",     "LF", "LF", "LF", "CF", "CF", "RF", "C",  "C",  "LF", "LF", "RF", "RF", "2B", "P",  "1B", "2B", "3B", "P",  "LF", "P",  "P",  "2B", "1B", "3B", "SS", "SS", "SS", "3B", "3B", "CF"],
    ["Mgrs Dec",    "CF", "CF", "CF", "CF", "CF", "CF", "CF", "CF", "CF", "CF", "IF", "IF", "IF", "IF", "IF", "IF", "IF", "IF", "IF", "IF", "OF", "OF", "OF", "OF", "RF", "RF", "RF", "LF", "LF", "LF"],
    ["Steal (2,3)", "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "IF", "IF", "IF", "IF", "IF", "IF", "IF", "IF", "IF", "IF", "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C"],
    ["Steal (H)",   "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "P",  "P",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C",  "C"],
    ["Bunt",        "SS", "SS", "SS", "SS", "1B", "2B", "2B", "2B", "2B", "2B", "3B", "3B", "3B", "3B", "1B", "1B", "3B", "3B", "3B", "3B", "C",  "C",  "C",  "C",  "C",  "P",  "C",  "C",  "C",  "C"],
]

errorKeyData = [
    ["Results of IF apply to the following fielders:", "", "", "Results of OF apply to the following fielders:", ""],
    ["Steal of 2nd , right handed batter (or switch-hitter vs LHP)", "2B", "", "Left-handed batter", "RF"],
    ["Steal of 2nd , left handed batter (or switch-hitter vs RHP)", "SS", "", "Right-handed batter", "LF"],
    ["Steal of 3rd", "3B", "", "", ""],
    ["Manager's Decision at Second Base, Right handed batter", "2B", "", "", ""],
    ["Manager's Decision at Second Base, Left handed batter", "SS", "", "", ""],
    ["Manager's Decision at Third Base", "3B", "", "", ""],
    ["Manager's Decision at Home", "C", "", "", ""],
]

errorRatingData = [
    ["Letter->",                     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
    ["Defensive Dice Error Numbers", "",  "",  "",  "",  "",  "",  "1", "1", "",  "",  "1", "1", "",  "1", "",  "1", "",  "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["",                             "",  "",  "",  "",  "",  "2", "",  "",  "",  "2", "",  "",  "2", "",  "",  "",  "",  "2", "",  "",  "2", "2", "2", "2", "2", "2"],
    ["",                             "",  "",  "",  "3", "3", "",  "",  "",  "",  "",  "",  "",  "3", "3", "",  "3", "",  "",  "3", "3", "",  "",  "3", "3", "3", "3"],
    ["",                             "",  "4", "4", "",  "",  "",  "",  "",  "",  "4", "4", "4", "",  "",  "",  "",  "",  "",  "4", "4", "4", "4", "",  "",  "4", "4"],
    ["",                             "5", "",  "5", "",  "5", "",  "",  "5", "",  "",  "",  "5", "",  "",  "",  "S", "",  "",  "",  "5", "",  "5", "",  "5", "",  "5"],
]

fieldingDeterminationData = [
    #      10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27    28    29    30    31    32    33    34    35    36    37    38    39    
    ["G",  "2B", "2B", "C",  "C",  "C",  "1B", "1B", "2B", "2B", "2B", "2B", "2B", "2B", "3B", "3B", "P",  "P",  "2B", "SS", "P",  "2B", "3B", "SS", "IC", "IM", "IM", "SS", "IM", "P",  "P"],
    ["F",  "CF", "CF", "1B", "C",  "CF", "1B", "1B", "CF", "CF", "CF", "CF", "2B", "2B", "SS", "RF", "RF", "RF", "RF", "CF", "RF", "CF", "3B", "CF", "CF", "LF", "OF", "OF", "LF", "CF", "P"],
    ["D",  "1B", "P",  "C",  "C",  "CF", "1B", "1B", "CF", "C",  "C",  "RF", "2B", "SS", "3B", "2B", "CF", "SS", "2B", "2B", "LF", "1B", "3B", "RF", "CF", "RF", "LF", "LF", "1B", "CF", "P"],
    ["SH", "SS", "SS", "SS", "SS", "1B", "2B", "2B", "2B", "2B", "2B", "3B", "3B", "3B", "1B", "1B", "1B", "1B", "3B", "3B", "3B", "C",  "C",  "C",  "C",  "P",  "P",  "C",  "C",  "C",  "C"],
]

keyData = [
    ["IC", "(corner infielder) - for Left handed batter, 1B. For Right handed batter, 3B"],
    ["IM", "(middle infielder) - for Left handed batter, 2B. For Right handed batter, SS"],
    ["OF", "(outfielder) - for Left handed batter, RF. For Right handed batter, LF"],
]

# Create a PDF with 'names_ages.pdf' as the name
pdf = SimpleDocTemplate("errors.pdf", pagesize=landscape(letter), leftMargin=10, rightMargin=10, topMargin=10, bottomMargin=10)

# Define a style for the table
table_text_style = ParagraphStyle(
    'Table', 
    parent=getSampleStyleSheet()['BodyText'], 
    fontSize=8,  # set font size
    textColor=colors.black,  # set font color
    fontName='Helvetica',  # set font
    alignment=1
)

errorRatingData[1][0] = Paragraph(str(errorRatingData[1][0]), table_text_style)
errorRatingData[1][9] = RotatedText("N/A")
errorRatingData[1][15] = RotatedText("N/A")
errorRatingData[1][17] = RotatedText("N/A")

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

header = [Paragraph('Errors', header_style)]
colwidths = [50]
for i in range(10, 40):
    header.append(Paragraph(str(i), header_style))
    colwidths.append(23)

errorData.insert(0, header)
fieldingDeterminationData.insert(0, header)

# Create a Table object
errorTable = Table(errorData, colWidths=colwidths, rowHeights=[18,12,12,12,12,12])
errorRatingTable = Table(errorRatingData, colWidths=colwidths, rowHeights=[14,12,12,12,12,12])
fieldingDeterminationTable = Table(fieldingDeterminationData, colWidths=colwidths, rowHeights=[18,12,12,12,12])

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
errorTable.setStyle(table_style)

error_rating_table_style = TableStyle([
    ('GRID', (0,0), (0,5), 1, colors.black),
    ('SPAN', (0,1), (0,5)),
    ('GRID', (1,0), (-1,-1), 1, colors.black),
    ('SPAN', (9,1), (9,5)),
    ('SPAN', (15,1), (15,5)),
    ('SPAN', (17,1), (17,5)),
    ('BACKGROUND', (0, 0), (-1, 0), hex_to_color("#CCCCCC")),
    ('INNERPADDING', (0,0), (-1,-1), 1),
    ('OUTERPADDING', (0,0), (-1,-1), 1),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # set bold font
    ('FONTSIZE', (0,0), (-1,-1), 9),  # set font size for all cells to 9
    ('TEXTCOLOR', (0,0), (-1,-1), colors.black),  # set text color for all cells to black
    ('LEADING', (0, 0), (-1, -1), 9),  # set leading value
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),  # center text in all cells
])
errorRatingTable.setStyle(error_rating_table_style)
fieldingDeterminationTable.setStyle(table_style)

# Create a title with a style and center alignment
title_style = ParagraphStyle(
    'Title', 
    parent=getSampleStyleSheet()['Heading1'], 
    fontSize=10,
    alignment=1  # Center alignment
)
errorTitle = Paragraph('Error Determination (Optional Rule)', title_style)
errorRatingTitle = Paragraph('Error Rating Chart (letter grade, optional rule)', title_style)
fieldingDeterminationTitle = Paragraph('Fielding Determination (Optional Rule)', title_style)

error_explain_style = ParagraphStyle(
    'CustomStyle',
    fontSize=8,
    textColor='black',
    alignment=1,
    leftIndent=100,
    rightIndent=100,
)
errorExplainTitle = Paragraph("To determine which position may have made an error (whenever an error occurs during the game), choose the most appropriate row above and roll to determine the fielder involved. Then, check that fielder's error rating at his position (a letter from A through Z).  Consult the error rating chart by rolling and summing the red and green (defensive) dice.  If the numbers rolled is one of that letters error numbers, the error occurs.  Batted-ball errors where the error is negated should be considered a result of 'F'", error_explain_style)

fieldingDetExplain = Paragraph("For the truly fanatical player, who wants to track fielding statistics use this table for all batted outs (grounders or fly outs) to determine the player whom the ball was hit.  Assume normal baseball effects (e.g. G* to SS with a runner on first base would be scored '6-3' rather than some odd resut like '6-1'). For ther outs (e.g. stolen bases), use practical baseball sense to determine the fielders in question.", error_explain_style)

story = []

# Error Determiniation
story.append(errorTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(errorTable)
story.append(Spacer(1, 4))
story.append(errorExplainTitle)

story.append(Spacer(1, 4))

# Error Key Chart
story.append(Spacer(1, 5))  # Add some space below the title
errorKeyTable = Table(errorKeyData, colWidths=[320,24,30,220,24], rowHeights=[12,12,12,12,12,12,12,12])
error_key_table_style = TableStyle([
    ('INNERPADDING', (0,0), (-1,-1), 1),
    ('OUTERPADDING', (0,0), (-1,-1), 1),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # set bold font
    ('FONTSIZE', (0,0), (-1,-1), 9),  # set font size for all cells
    ('TEXTCOLOR', (0,0), (-1,-1), colors.black),  # set text color for all cells to black
    ('LEADING', (0, 0), (-1, -1), 9),  # set leading value
    ('ALIGN', (0,0), (0,1), 'LEFT'),
    ('ALIGN', (0,1), (0,-1), 'RIGHT'),
    ('ALIGN', (3,1), (3,-1), 'RIGHT'),
])
errorKeyTable.setStyle(error_key_table_style)
story.append(errorKeyTable)

# Error Rating Chart
story.append(Spacer(1, 18))
story.append(errorRatingTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(errorRatingTable)

story.append(Spacer(1, 18))
story.append(fieldingDeterminationTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(fieldingDeterminationTable)
story.append(Spacer(1, 4))
story.append(fieldingDetExplain)

# Key Chart
story.append(Spacer(1, 6))
keyTable = Table(keyData, colWidths=[24,320], rowHeights=[12,12,12])
key_table_style = TableStyle([
    ('GRID', (0,0), (0,2), 1, colors.black),
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

# Build the PDF
pdf.build(story)
