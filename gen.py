from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

names = {
    "base.html": "index.html",
    "product1.html": "product1.html"
}

for src, dest in names.items():
    template = env.get_template(src)
    output_from_parsed_template = template.render()

    with open(dest, "w") as fh:
        fh.write(output_from_parsed_template)
