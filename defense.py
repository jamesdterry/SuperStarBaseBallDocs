from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import Color
from reportlab.lib import colors
from rotated_text import RotatedText

# Use Double X Option?
doublex = False

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

defData = [
    ["Tot Def", "0-9", "10-13", "14-18", "19-22", "23-27", "28-31", "32-36", "37-40", "41-45", "46-49", "50-54", "55-58", "59-63", "64-67", "68-72", "73-76", "77-81", "82-85", "86-90", "91-94", "95-99", "100-103", "104-108", "109+"],
    ["'D' OUTS", "10,,,,,", ",11,,,,", ",,12,,,", ",,,13,,", ",,,,14,", ",11,12,,,", ",11,,13,,", ",,12,13,,", ",,12,,14,", ",,,13,14,", ",11,12,13,,", ",11,12,,14,", ",11,,13,14,", ",,12,13,14,", ",,12,,14,15", ",,,13,14,15", "10,,12,,14,15", ",11,12,,14,15", ",11,,13,14,15", ",,12,13,14,15", "10,11,,13,14,15", "10,,12,13,14,15", ",11,12,13,14,15", "10,11,12,13,14,15"]
]

sacBuntData = [
    #     10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27    28     29   30    31    32    33   34    35    36    37    38    39    
    ["A", "SH", "SH", "SH", "SH", "1",  "SH", "SH", "SH", "SH", "SH", "SH", "SH", "SH", "FC", "SH", "SH", "SH", "SH", "DP", "SH", "2K", "2K", "2K", "E", "SH", "G",  "F",  "SH", "G",  "SH"],
    ["B", "SH", "SH", "SH", "1",  "SH", "SH", "SH", "SH", "SH", "SH", "SH", "SH", "FC", "SH", "G",  "G",  "E",  "SP", "E",  "G",  "2K", "F",  "F",  "G", "2K", "2K", "2K", "SH", "SH", "SH"],
]

suicideSqueezeData = [
    #     10    11    12    13    14    15    16    17    18    19    20    21    22    23   24   25   26   27    28    29    30    31    32   33    34    35    36    37   38   39    
    ["A", "SH", "SH", "SH", "1",  "1",  "SH", "SH", "SH", "SH", "SH", "SH", "FC", "SH", "-", "-", "-", "-", "SH", "SH", "SH", "E",  "SH", "E", "F",  "2K", "2K", "SH", "G", "G", "-"],
    ["B", "SH", "1",  "1",  "SH", "SH", "SH", "SH", "SH", "SH", "SH", "SH", "-",  "F",  "F", "-", "-", "-", "-",  "SH", "-",  "SH", "E",  "G", "2K", "2K", "2K", "-",  "-", "G", "FC"],
]

pitcherXData = [
    #       10    11     12    13   14    15    16    17    18    19    20    21     22     23     24     25     26     27     28    29    30     31     32     33    34   35    36   37     38     39    
    ["X",   "I",  "I",   "I",  "I", "I",  "I",  "I",  "I",  "I",  "I",  "WP", "WP",  "WP",  "WP",  "BK",  "WP",  "WP",  "BK",  "WP", "I",  "WP",  "WP",  "PB",  "PB", "H", "H", "PB", "WP",  "WP",  "WP"],
    ["Pos", "1B", "1B",  "CF", "C", "SS", "SS", "SS", "1B", "1B", "1B", "CF", "CF",  "3B",  "P",   "2B",  "2B",  "3B",  "3B",  "2B", "1B", "RF",  "RF",  "SS",  "P",  "P", "C",  "C", "LF",  "LF",  "CF"],
    ["Dur", "15", "N/I", "8",  "4", "3",  "2",  "7",  "10", "14", "20", "6",  "N/I", "N/I", "N/I", "N/I", "N/I", "N/I", "N/I", "5",  "12", "N/I", "N/I", "N/I", "0",  "0", "0",  "1", "N/I", "N/I", "9"],
]

if doublex:
    pitcherXData[0][29] = 'XX'

def_inner_table_style = TableStyle([
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # set bold font
    ('FONTSIZE', (0,0), (-1,-1), 9),  # set font size for all cells to 9
    ('TEXTCOLOR', (0,0), (-1,-1), colors.black),  # set text color for all cells to black
    ('LEADING', (0, 0), (-1, -1), 9),  # set leading value
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),  # center text in all cells
])
for col in range(len(defData[0])):
    defData[0][col] = RotatedText(defData[0][col])
    
defData[1][0] = RotatedText(defData[1][0])

for col in range(1, len(defData[1])):
    ddata_1d = defData[1][col].split(",")
    ddata_2d = [[item] for item in ddata_1d]
    ddtable = Table(ddata_2d, colWidths=[28], rowHeights=[8.4,8.4,8.4,8.4,8.4,8.4])
    ddtable.setStyle(def_inner_table_style)
    defData[1][col] = ddtable

keyData = [
    ["1", "Batter Safe and all runners advance 1 base", "F", "Pop out - on squeeze DP"],
    ["SH", "Sacrifice - batter out, all runners advance 1 base", "G", "Routine ground out force"],
    ["FC", "Sacrifice successfull and fielder's choice - batter safe at first", "DP", "Standard DP"],
    ["E", "Sacrifice successfull plus batter safe at first on error", "-", "Missed bunt - runner must attempt to steal home"],
    ["2K", "Two foul bunts - batter may attempt again, but if another 2K batter strikes out and batter must attempt", "", ""],
    ["", "to steal.  If batter chooses not to bunt again, pitcher gets SO on 35 and 36 and rolls to pitch.", "", ""],
]

key2Data = [
    ["BK", "Balk - all runners advance one base"],
    ["H", "Batter hit by pitch and is awarded first base (roll again on 'Dur' table to determine injury effect to batter)"],
    ["PB", "Passed Ball - all runners advance one base"],
    ["WP", "Wild Pitch - all runners advance one base"],
    ["I", "Possible Injury to player in the field, roll again on the 'Pos' chart to determine which player may be injured, the roll on the 'Dur' to determine duration."],
    ["#", "When a number appears for an injury duration, the player is removed from the game and must sit out a number of games equal to that shown."],
    ["0", "When a zero appears for an injury duration, the player is out for the remainder of the game."],
    ["N/I", "When N/I appears there is no injury."],
]

if doublex:
    key2Data.insert(0, ["XX", "Roll on Pitcher XX Chart"])

# Create a PDF with 'names_ages.pdf' as the name
pdf = SimpleDocTemplate("defense.pdf", pagesize=landscape(letter), leftMargin=10, rightMargin=10, topMargin=10, bottomMargin=10)

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

sacBuntData.insert(0, header)
suicideSqueezeData.insert(0, header)
pitcherXData.insert(0, header)

# Create a Table object
defTable = Table(defData, colWidths=[30,30,30,30], rowHeights=[40,60])
sacBuntTable = Table(sacBuntData, colWidths=colwidths, rowHeights=[18,12,12])
suicideSqueezeTable = Table(suicideSqueezeData, colWidths=colwidths, rowHeights=[18,12,12])
pitcherXTable = Table(pitcherXData, colWidths=colwidths, rowHeights=[18,12,12,12])

def_table_style = TableStyle([
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
defTable.setStyle(def_table_style)
sacBuntTable.setStyle(table_style)
suicideSqueezeTable.setStyle(table_style)
pitcherXTable.setStyle(table_style)

# Create a title with a style and center alignment
title_style = ParagraphStyle(
    'Title', 
    parent=getSampleStyleSheet()['Heading1'], 
    fontSize=10,
    alignment=1  # Center alignment
)
defTitle = Paragraph('Automatic Out', title_style)
sacBuntTitle = Paragraph('Sacrifice Bunt (to advance runners to 2nd or 3rd base)', title_style)
suicideSqueezeTitle = Paragraph('Suicide Squeeze Bunt (to advance a runner home)', title_style)
pitcherXTitle = Paragraph('Pitcher X Chart', title_style)

sub_title_style = ParagraphStyle(
    'SubTitle', 
    parent=getSampleStyleSheet()['Heading2'], 
    fontSize=9,
    alignment=1  # Center alignment
)
pitcherXSubTitle = Paragraph('When a pitcher rolls a 38 roll again on the "X" chart above.  Simply roll and crossreference to determine the outcome.', sub_title_style)

story = []

# Defense Chart
story.append(defTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(defTable)

story.append(Spacer(1, 12))

# Sac Bunt
story.append(sacBuntTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(sacBuntTable)

story.append(Spacer(1, 12))

# Suicide Squeeze
story.append(suicideSqueezeTitle)  # Add the title to the story
story.append(Spacer(1, -10))  # Add some space below the title
story.append(suicideSqueezeTable)

# Key Chart
story.append(Spacer(1, 5))  # Add some space below the title
keyTable = Table(keyData, colWidths=[24,320,24,320], rowHeights=[12,12,12,12,12,12])
key_table_style = TableStyle([
    ('GRID', (0,0), (0,4), 1, colors.black),
    ('GRID', (2,0), (2,3), 1, colors.black),
    ('INNERPADDING', (0,0), (-1,-1), 1),
    ('OUTERPADDING', (0,0), (-1,-1), 1),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # set bold font
    ('FONTSIZE', (0,0), (-1,-1), 9),  # set font size for all cells
    ('TEXTCOLOR', (0,0), (-1,-1), colors.black),  # set text color for all cells to black
    ('LEADING', (0, 0), (-1, -1), 9),  # set leading value
    ('ALIGN', (0,0), (0,5), 'CENTER'),
    ('ALIGN', (2,0), (2,4), 'CENTER'),
])
keyTable.setStyle(key_table_style)
story.append(keyTable)

story.append(Spacer(1, 12))

story.append(pitcherXTitle)
story.append(Spacer(1, -10))
story.append(pitcherXTable)
story.append(Spacer(1, -8))
story.append(pitcherXSubTitle)
story.append(Spacer(1, -8))

# Key 2 Chart
k2rowHeights=[12,12,12,12,12,12,12,12]
if doublex:
    k2rowHeights.append(12)

story.append(Spacer(1, 5))  # Add some space below the title
key2Table = Table(key2Data, colWidths=[24,600], rowHeights=k2rowHeights)
key2_table_style = TableStyle([
    ('GRID', (0,0), (0,8), 1, colors.black),
    ('INNERPADDING', (0,0), (-1,-1), 1),
    ('OUTERPADDING', (0,0), (-1,-1), 1),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # set bold font
    ('FONTSIZE', (0,0), (-1,-1), 9),  # set font size for all cells
    ('TEXTCOLOR', (0,0), (-1,-1), colors.black),  # set text color for all cells to black
    ('LEADING', (0, 0), (-1, -1), 9),  # set leading value
    ('ALIGN', (0,0), (0,8), 'CENTER'),
])
key2Table.setStyle(key2_table_style)
story.append(key2Table)

# Build the PDF
pdf.build(story)
