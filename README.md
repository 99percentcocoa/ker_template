# Survey Sheet Generator

This tool generates personalized survey sheets as PDF files for students based on their information.

## Usage

### Command Line Interface

Run the `personalize.py` script with the following required arguments:

```bash
python3 personalize.py \
  --sheet-id <SHEET_ID> \
  --student-name "<STUDENT_NAME>" \
  --student-grade <GRADE> \
  --student-school "<SCHOOL_NAME>" \
  --student-tfi-id "<TFI_ID>" \
  --template-name <TEMPLATE_NAME> \
  --output <OUTPUT_FILE>
```

### Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `--sheet-id` | int | Yes | Unique identifier for the sheet |
| `--student-name` | str | Yes | Name of the student |
| `--student-grade` | int | Yes | Grade/class of the student |
| `--student-school` | str | Yes | School name of the student |
| `--student-tfi-id` | str | Yes | TFI ID of the student |
| `--template-name` | str | Yes | Name of the template to use (e.g., 'v1', 'test_template') |
| `--output` | str | No | Output PDF file path (default: `personalized_survey.pdf`) |

### Example

```bash
python3 personalize.py \
  --sheet-id 1 \
  --student-name "Saarang" \
  --student-grade 6 \
  --student-school "Ahilyadevi Holkar EMS" \
  --student-tfi-id "TFI12345" \
  --template-name "v1" \
  --output "survey_saarang.pdf"
```

This will generate a personalized survey PDF file named `survey_saarang.pdf` for the student Saarang.

### Output

Upon successful execution, the script will:
1. Generate a personalized survey sheet based on the provided student information
2. Save it as a PDF file at the specified output path
3. Display a confirmation message with the student details

Example output:
```
✓ Successfully generated personalized survey: survey_saarang.pdf
  Student: Saarang (Grade 6)
  School: Ahilyadevi Holkar EMS
  TFI ID: TFI12345
```

## Project Structure

- `personalize.py` - Main script for generating personalized surveys
- `models.py` - Data models (SheetMeta, etc.)
- `render.py` - PDF rendering functionality
- `questions.py` - Survey questions content
- `templates/` - HTML and CSS templates for different survey versions

## Available Templates

Templates are stored in the `templates/` directory. Current available templates:
- `v1` - Version 1 template
- `test_template` - Test template

Each template consists of:
- `{template_name}.html` - HTML structure
- `{template_name}_style.css` - Styling
