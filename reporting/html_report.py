from jinja2 import Template

HTML_TEMPLATE = """
<html>
<head><title>Migration Report</title></head>
<body>
<h1>Migration Validation Report</h1>
{% for r in results %}
<div>
<h2>{{ r.device }}</h2>
<p>Status: {{ r.status }}</p>
<p>Severity: {{ r.severity }}</p>
</div>
{% endfor %}
</body>
</html>
"""

def generate_html(results):
    template = Template(HTML_TEMPLATE)
    html = template.render(results=results)

    with open("output/reports/report.html", "w") as f:
        f.write(html)
