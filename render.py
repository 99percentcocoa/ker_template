
import os
from pathlib import Path
from typing import Optional

from weasyprint import HTML, CSS

def generate_pdf(
        template_name: str,
        html_str: str,
        output_path: str | Path,
        stylesheets: Optional[list[str | Path]] = None
) -> bytes:
    """ 
    Render a survey HTML string to a PDF file using a specified template.
    
    Args:
        template_name (str): The name of the template to use for rendering.
        html_str (str): The HTML content to be converted to PDF.
        output_path (str | Path): The file path where the PDF will be saved.
        stylesheets (Optional[list[str | Path]]): Additional CSS stylesheets to apply.
        
    Returns:
        bytes: The binary content of the generated PDF.
    """

    template_html_path = Path(__file__).parent / "templates" / f"{template_name}.html"
    template_css_path = Path(__file__).parent / "templates" / f"{template_name}_style.css"

    output_path = Path(output_path)

    css_objs = []
    if stylesheets:
        for sheet in stylesheets:
            css_objs.append(CSS(filename=str(sheet)))

    print(f"Using template HTML: {template_html_path}")
    print(f"Using template CSS: {template_css_path}")

    html = HTML(string=html_str, base_url=template_html_path.parent.as_uri())
    html.write_pdf(target=str(output_path), stylesheets=[CSS(filename=str(template_css_path))] + css_objs)

if __name__ == "__main__":
    print(generate_pdf(template_name="test", html_str="<h1>hi</h1>", output_path="test.pdf"))