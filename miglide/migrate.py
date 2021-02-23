import argparse
import re
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def move_images(slide_name):
    destination_root = Path("docs") / "_images" / slide_name
    destination_root.mkdir(parents=True, exist_ok=True)

    images_root = Path(slide_name) / "assets" / "images"
    for image_path in images_root.glob("*.png"):
        destination_path = destination_root / image_path.name
        shutil.copyfile(image_path, destination_path)


def load_slide_template():
    script_dir = Path(__file__).resolve(strict=True).parent
    file_loader = FileSystemLoader(script_dir / "templates")
    environment = Environment(loader=file_loader)
    return environment.get_template("revealjs_slide.html.jinja")


def rewrite_contents(contents, slide_name):
    rewritten_lines = []
    font_awesome_pattern = r"@fa\[([a-z]*)\]"
    images_pattern = f"{slide_name}/assets/images"
    for line in contents.split("\n"):
        if m := re.search(font_awesome_pattern, line):
            line = re.sub(
                font_awesome_pattern, f'<i class="fab fa-{m[1]}"></i>', line
            )
        line = re.sub(images_pattern, f"../_images/{slide_name}", line)
        rewritten_lines.append(line)

    return "\n".join(rewritten_lines)


def migrate_slide(slide_name):
    source = Path(slide_name) / "PITCHME.md"
    destination = Path("docs") / slide_name / "slide.html"

    source_contents = source.read_text()
    slide_contents = rewrite_contents(source_contents.rstrip(), slide_name)

    template = load_slide_template()
    output = template.render(slide_contents=slide_contents)
    with destination.open("w") as f:
        f.write(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("slide")
    args = parser.parse_args()

    slide_name = args.slide.rstrip("/")

    move_images(slide_name)

    migrate_slide(slide_name)
