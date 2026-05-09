import os

# The titles from your handwritten note
sections = {
    "books.html": "كتب",
    "articles.html": "مقالات",
    "studies.html": "دراسات",
    "biographies.html": "سير وتراجم",
    "poems.html": "قصائد",
    "prose.html": "أعمال نثرية",
    "reviews.html": "مراجعات",
    "lectures.html": "محاضرات",
    "podcast.html": "بودكاست",
    "travels.html": "رحلات"
}

template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="sub-page">
    <header>
        <h1>{title}</h1>
        <a href="index.html" class="back-link">🏠 العودة للرئيسية</a>
    </header>
    <main>
        <div class="grid">
            <!-- Add your items here -->
            <div class="card">
                <h3>قريباً...</h3>
                <p>سيتم إضافة المحتوى هنا قريباً.</p>
            </div>
        </div>
    </main>
</body>
</html>"""

for filename, title in sections.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(template.format(title=title))

print("Successfully created 10 HTML files!")