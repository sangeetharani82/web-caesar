markup = """
<!doctype html>
<html>
    <head>
        <title>{0}</title>
        <textarea>{0}</textarea>
    </head>
    <body>
        <h1>{1}</h1>
    </body>
</html>
"""

markup = markup.format('My page title', 'Page heading')
print(markup)