from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)


OUTPUT_FILE = "OOPs_Layman_Analogies_and_Examples.pdf"
DOWNLOAD_DIR = "oops_downloads"


topics = [
    {
        "title": "1. Class",
        "simple": "A class is a blueprint or plan for creating objects.",
        "analogy": "Think of a house blueprint. The blueprint is not a real house, but it tells us how to build many houses.",
        "example": "A Car class can describe common things every car has: color, brand, speed, and actions like start or stop.",
        "code": """class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color""",
    },
    {
        "title": "2. Object",
        "simple": "An object is a real thing created from a class.",
        "analogy": "If the class is a house blueprint, an object is the actual house built from it.",
        "example": "Toyota red car and Honda black car can both be objects of the Car class.",
        "code": """car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Black")""",
    },
    {
        "title": "3. Encapsulation",
        "simple": "Encapsulation means keeping data and related actions together, and protecting direct access when needed.",
        "analogy": "Think of a TV remote. You press buttons to change channels, but you do not touch the inner circuit directly.",
        "example": "A BankAccount can keep balance private and allow deposit or withdraw through methods.",
        "code": """class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount""",
    },
    {
        "title": "4. Abstraction",
        "simple": "Abstraction means showing only what is necessary and hiding the complicated details.",
        "analogy": "When you drive a car, you use steering, brakes, and accelerator. You do not need to know every engine detail.",
        "example": "A payment app shows a Pay button, but hides banking, verification, and server work.",
        "code": """class Payment:
    def pay(self, amount):
        print("Payment processed")""",
    },
    {
        "title": "5. Inheritance",
        "simple": "Inheritance means one class can reuse features of another class.",
        "analogy": "A child may inherit traits from parents. Similarly, a class can inherit properties and methods from another class.",
        "example": "Dog and Cat can inherit common features from an Animal class.",
        "code": """class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")""",
    },
    {
        "title": "6. Polymorphism",
        "simple": "Polymorphism means the same action can behave differently for different objects.",
        "analogy": "The word 'speak' is the same, but a human speaks words, a dog barks, and a cat meows.",
        "example": "Different classes can have the same method name, but each gives its own behavior.",
        "code": """class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")""",
    },
    {
        "title": "7. Constructor",
        "simple": "A constructor is a special method that runs automatically when an object is created.",
        "analogy": "When you buy a new phone, basic setup starts before you use it. A constructor does initial setup for an object.",
        "example": "In Python, __init__ sets starting values like name, age, or brand.",
        "code": """class Student:
    def __init__(self, name):
        self.name = name""",
    },
    {
        "title": "8. Method",
        "simple": "A method is a function that belongs to a class or object.",
        "analogy": "A mobile phone has actions like call, message, and take photo. These actions are like methods.",
        "example": "A Car object can have methods like start(), stop(), and accelerate().",
        "code": """class Car:
    def start(self):
        print("Car started")""",
    },
    {
        "title": "9. Attribute",
        "simple": "An attribute is a value or property that belongs to an object.",
        "analogy": "A person has name, age, height, and address. These are like attributes.",
        "example": "A Student object can have name, roll_number, and marks.",
        "code": """student.name = "Asha"
student.marks = 90""",
    },
    {
        "title": "10. Overriding",
        "simple": "Overriding means a child class changes the behavior of a method inherited from a parent class.",
        "analogy": "A family recipe may be inherited, but a child can prepare it in their own style.",
        "example": "Animal has sound(), but Dog can override it to say Bark.",
        "code": """class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")""",
    },
]


def make_styles():
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=23,
        leading=28,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1F3A5F"),
        spaceAfter=14,
    )
    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["BodyText"],
        fontSize=11,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#444444"),
        spaceAfter=18,
    )
    h2_style = ParagraphStyle(
        "TopicHeading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.white,
        backColor=colors.HexColor("#1F3A5F"),
        borderPadding=7,
        spaceBefore=8,
        spaceAfter=8,
    )
    label_style = ParagraphStyle(
        "Label",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#1F3A5F"),
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=10.5,
        leading=15,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#222222"),
    )
    code_style = ParagraphStyle(
        "Code",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#222222"),
        backColor=colors.HexColor("#F3F6F8"),
        borderPadding=6,
    )
    return {
        "title": title_style,
        "subtitle": subtitle_style,
        "h2": h2_style,
        "label": label_style,
        "body": body_style,
        "code": code_style,
    }


def topic_name(item):
    return item["title"].split(". ", 1)[1]


def slugify(value):
    return value.lower().replace(" ", "_")


def topic_filename(item):
    number = item["title"].split(".", 1)[0].zfill(2)
    return f"{number}_{slugify(topic_name(item))}_oops_layman.pdf"


def make_topic_table(item, pdf_styles):
    rows = [
        [Paragraph("Simple answer", pdf_styles["label"]), Paragraph(item["simple"], pdf_styles["body"])],
        [Paragraph("Analogy", pdf_styles["label"]), Paragraph(item["analogy"], pdf_styles["body"])],
        [Paragraph("Example", pdf_styles["label"]), Paragraph(item["example"], pdf_styles["body"])],
        [
            Paragraph("Python", pdf_styles["label"]),
            Paragraph(item["code"].replace("\n", "<br/>"), pdf_styles["code"]),
        ],
    ]
    table = Table(rows, colWidths=[1.25 * inch, 6.1 * inch])
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#C8D2DC")),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EDF3F7")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawRightString(A4[0] - 0.55 * inch, 0.4 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.6 * inch,
    )

    pdf_styles = make_styles()

    story = [
        Paragraph("OOPs in Layman Terms", pdf_styles["title"]),
        Paragraph(
            "Simple answers, everyday analogies, and tiny Python examples for Object-Oriented Programming.",
            pdf_styles["subtitle"],
        ),
    ]

    overview_rows = [["Concept", "Layman Meaning"]]
    for item in topics:
        overview_rows.append([topic_name(item), item["simple"]])

    overview_table = Table(overview_rows, colWidths=[1.55 * inch, 5.8 * inch])
    overview_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCE8F2")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1F3A5F")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("LEADING", (0, 0), (-1, -1), 12),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#B8C6D1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )

    story.append(overview_table)
    story.append(PageBreak())

    for item in topics:
        story.append(Paragraph(item["title"], pdf_styles["h2"]))
        story.append(make_topic_table(item, pdf_styles))
        story.append(Spacer(1, 0.18 * inch))

    story.append(Spacer(1, 0.2 * inch))
    story.append(
        Paragraph(
            "<b>Quick memory trick:</b> Class is the plan, object is the real item, encapsulation protects data, abstraction hides complexity, inheritance reuses features, and polymorphism allows different behavior through the same action.",
            pdf_styles["body"],
        )
    )

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


def build_topic_pdfs():
    import os

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    pdf_styles = make_styles()
    created_files = []

    for item in topics:
        filename = topic_filename(item)
        output_path = os.path.join(DOWNLOAD_DIR, filename)
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=0.55 * inch,
            leftMargin=0.55 * inch,
            topMargin=0.65 * inch,
            bottomMargin=0.6 * inch,
        )
        story = [
            Paragraph(f"OOPs: {topic_name(item)}", pdf_styles["title"]),
            Paragraph(
                "Simple answer, layman analogy, and a tiny Python example.",
                pdf_styles["subtitle"],
            ),
            Paragraph(item["title"], pdf_styles["h2"]),
            make_topic_table(item, pdf_styles),
        ]
        doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
        created_files.append(filename)

    return created_files


def build_download_page(created_files):
    import html
    import os

    cards = []
    for item, filename in zip(topics, created_files):
        name = topic_name(item)
        cards.append(
            f"""
            <article class="card">
                <h2>{html.escape(name)}</h2>
                <p>{html.escape(item["simple"])}</p>
                <a href="{html.escape(filename)}" download>Download PDF</a>
            </article>
            """
        )

    page = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>OOPs PDF Downloads</title>
    <style>
        body {{
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            color: #172033;
            background: #f5f7fb;
        }}
        header {{
            padding: 32px 24px 20px;
            background: #1f3a5f;
            color: white;
        }}
        main {{
            max-width: 980px;
            margin: 0 auto;
            padding: 24px;
        }}
        h1 {{
            margin: 0 0 8px;
            font-size: 30px;
            letter-spacing: 0;
        }}
        header p {{
            margin: 0;
            color: #dce8f2;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 14px;
        }}
        .card {{
            background: white;
            border: 1px solid #d7e0ea;
            border-radius: 8px;
            padding: 16px;
        }}
        h2 {{
            margin: 0 0 8px;
            font-size: 18px;
            letter-spacing: 0;
        }}
        .card p {{
            min-height: 64px;
            margin: 0 0 14px;
            line-height: 1.45;
            color: #3c4658;
        }}
        a {{
            display: inline-block;
            padding: 9px 12px;
            border-radius: 6px;
            background: #1f3a5f;
            color: white;
            text-decoration: none;
            font-weight: 700;
            font-size: 14px;
        }}
        .all {{
            margin-bottom: 18px;
        }}
    </style>
</head>
<body>
    <header>
        <h1>OOPs PDF Downloads</h1>
        <p>Each concept has its own beginner-friendly PDF.</p>
    </header>
    <main>
        <a class="all" href="../{html.escape(OUTPUT_FILE)}" download>Download Complete Guide</a>
        <section class="grid">
            {"".join(cards)}
        </section>
    </main>
</body>
</html>
"""
    path = os.path.join(DOWNLOAD_DIR, "index.html")
    with open(path, "w", encoding="utf-8") as file:
        file.write(page)
    return path


if __name__ == "__main__":
    build_pdf()
    files = build_topic_pdfs()
    build_download_page(files)
