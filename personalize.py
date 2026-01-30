import argparse
from pathlib import Path
from models import SheetMeta
from render import generate_pdf
import questions as questions_text

def load_template(template_name: str) -> str:
    """
    Load the HTML template for the given template name.

    Args:
        template_name (str): The name of the template to load.

    Returns:
        str: The content of the HTML template.
    """
    template_html_path = Path(__file__).parent / "templates" / f"{template_name}.html"

    with open(template_html_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    
    return html_content

def generate_questions_html(sheet_meta: SheetMeta) -> str:
    """
    Generate HTML for the questions section based on student metadata.

    Args:
        sheet_meta (SheetMeta): Metadata of the sheet containing student information.
    
    Returns:
        str: HTML string for the questions section (table).
    """
    questions_html = ""

    for question_idx in range(0, len(questions_text.questions)):
        tag_url = Path(__file__).parent.parent / "assets" / "tags" / "25h9" / f"tag25_09_{str(question_idx).zfill(5)}.svg"
        questions_html += "<tr>\n"
        questions_html += f'    <td class="question">{questions_text.questions[question_idx]}</td>\n'
        questions_html += '    <td class="bubble"><span class="circle"></span></td>\n'
        questions_html += '    <td class="bubble"><span class="circle"></span></td>\n'
        questions_html += '    <td class="bubble"><span class="circle"></span></td>\n'
        questions_html += '    <td class="bubble"><span class="circle"></span></td>\n'
        questions_html += "</tr>\n"

    return questions_html


def personalize_sheet(sheet_meta: SheetMeta) -> str:
    """
    Generate survey HTML string for a student based on their metadata.

    Args:
        sheet_meta (SheetMeta): Metadata of the sheet containing student information.
    
    Returns:
        str: Personalized HTML string for the student.
    """
    template_html = load_template(sheet_meta.template_name)

    # questions_html (table)
    questions_html = generate_questions_html(sheet_meta)

    # add name and other metadata
    template_html = template_html.replace("{{phoneNumber}}", "+91 9876543210" or "")
    template_html = template_html.replace("{{student_name}}", sheet_meta.student_name or "")
    template_html = template_html.replace("{{student_grade}}", str(sheet_meta.student_grade) if sheet_meta.student_grade is not None else "")
    template_html = template_html.replace("{{student_school}}", sheet_meta.student_school or "")
    template_html = template_html.replace("{{student_tfi_id}}", sheet_meta.student_tfi_id or "")
    template_html = template_html.replace("{{survey_id}}", str(sheet_meta.sheet_id))

    final_html = template_html.replace("{{questions}}", questions_html)

    return final_html

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a personalized survey sheet PDF for a student."
    )
    
    parser.add_argument(
        "--sheet-id",
        type=int,
        required=True,
        help="Unique identifier for the sheet"
    )
    parser.add_argument(
        "--student-name",
        type=str,
        required=True,
        help="Name of the student"
    )
    parser.add_argument(
        "--student-grade",
        type=int,
        required=True,
        help="Grade/class of the student"
    )
    parser.add_argument(
        "--student-school",
        type=str,
        required=True,
        help="School name of the student"
    )
    parser.add_argument(
        "--student-tfi-id",
        type=str,
        required=True,
        help="TFI ID of the student"
    )
    parser.add_argument(
        "--template-name",
        type=str,
        required=True,
        help="Name of the template to use (e.g., 'v1', 'test_template')"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="personalized_survey.pdf",
        help="Output PDF file path (default: personalized_survey.pdf)"
    )
    
    args = parser.parse_args()
    
    # Create SheetMeta object from CLI arguments
    sheet_meta = SheetMeta(
        sheet_id=args.sheet_id,
        student_name=args.student_name,
        student_grade=args.student_grade,
        student_school=args.student_school,
        student_tfi_id=args.student_tfi_id,
        template_name=args.template_name
    )
    
    # Generate personalized HTML
    personalized_html = personalize_sheet(sheet_meta)
    
    # Generate PDF
    generate_pdf(
        template_name=sheet_meta.template_name,
        html_str=personalized_html,
        output_path=args.output
    )
    
    print(f"✓ Successfully generated personalized survey: {args.output}")
    print(f"  Student: {args.student_name} (Grade {args.student_grade})")
    print(f"  School: {args.student_school}")
    print(f"  TFI ID: {args.student_tfi_id}")