import os
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import landscape, letter
from PIL import Image

# Configuration
PAGE_SIZE = (1080, 1080)  # Square size in points
BG_COLOR = colors.HexColor("#1A1A1A")  # Dark theme
TEXT_COLOR = colors.HexColor("#FFFFFF")
SUBTEXT_COLOR = colors.HexColor("#AAAAAA")
ACCENT_COLOR = colors.HexColor("#4F46E5")  # Indigo/Blue accent

IMAGES_DIR = r"c:\Users\mahes\OneDrive\Documents\personal-docs\mahesh-blog\assets\images"
OUTPUT_PDF = r"c:\Users\mahes\OneDrive\Documents\personal-docs\mahesh-blog\linkedin_carousel.pdf"

slides = [
    {
        "type": "cover",
        "title": ["Changing UX Patterns in the", "world of Agentic AI systems"],
        "subtitle": "Why \"Faster\" is Not Always Better for AI Trust"
    },
    {
        "type": "image",
        "title": "Speed vs. Trust in Agentic AI",
        "image": "boss_comic_strip.png"
    },
    {
        "type": "image",
        "title": "Trust is Built on Visible Reasoning",
        "image": "medical_ai_thinking_state.png"
    },
    {
        "type": "image",
        "title": "The UX of \"Visible Thinking\"",
        "image": "ai_response_comparison_ui.png"
    },
    {
        "type": "image",
        "title": "Domain Matters: Speed vs. Substance",
        "image": "fast_vs_deliberative_ai_domains.png"
    },
    {
        "type": "image",
        "title": "The Power of Asynchronous AI Responses",
        "image": "deep_thought_comic.png"
    },
    {
        "type": "image",
        "title": "Designing Async Workflows",
        "image": "async_answer_ux.png"
    },
    {
        "type": "cta",
        "title": "Read the full article",
        "subtitle": "Changing UX Patterns in the world of Agentic AI",
        "url": "https://maheshmad.github.io/blog/ai/2026/03/25/changing-ux-patterns-in-the-world-of-agentic-ai-systems.html"
    }
]

def create_carousel_safe():
    c = canvas.Canvas(OUTPUT_PDF, pagesize=PAGE_SIZE)
    width, height = PAGE_SIZE

    for i, slide in enumerate(slides):
        # 1. Background
        c.setFillColor(BG_COLOR)
        c.rect(0, 0, width, height, fill=1)

        # 2. Page Counter
        c.setFillColor(SUBTEXT_COLOR)
        c.setFont("Helvetica", 20)
        c.drawRightString(width - 50, 40, f"{i + 1} / {len(slides)}")

        if slide["type"] == "cover":
            # Accent bar
            c.setFillColor(ACCENT_COLOR)
            c.rect(0, height - 15, width, 15, fill=1)

            # Title - Support Multi-line
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 46)
            lines = slide["title"] if isinstance(slide["title"], list) else [slide["title"]]
            
            line_height = 60
            total_h = len(lines) * line_height
            start_y = height / 2 + (total_h / 2) - 10
            
            for line in lines:
                w = c.stringWidth(line, "Helvetica-Bold", 46)
                c.drawString((width - w) / 2, start_y, line)
                start_y -= line_height

            # Subtitle
            c.setFillColor(SUBTEXT_COLOR)
            c.setFont("Helvetica", 32)
            text = slide["subtitle"]
            w = c.stringWidth(text, "Helvetica", 32)
            c.drawString((width - w) / 2, (height / 2) - 50, text)

            # Prompt
            c.setFillColor(ACCENT_COLOR)
            c.setFont("Helvetica-Bold", 26)
            text = "Swipe to continue ->"
            w = c.stringWidth(text, "Helvetica-Bold", 26)
            c.drawString((width - w) / 2, 120, text)

        elif slide["type"] == "image":
            # Title
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 42)
            text = slide["title"]
            w = c.stringWidth(text, "Helvetica-Bold", 42)
            c.drawString((width - w) / 2, height - 100, text)

            # Image
            img_name = slide["image"]
            img_path = os.path.join(IMAGES_DIR, img_name)

            if os.path.exists(img_path):
                img = Image.open(img_path)
                img_w, img_h = img.size

                max_w = width - 120
                max_h = height - 260 
                
                aspect = img_w / img_h
                render_w = max_w
                render_h = render_w / aspect
                
                if render_h > max_h:
                    render_h = max_h
                    render_w = render_h * aspect

                x = (width - render_w) / 2
                y = (height - render_h) / 2 - 10

                # Draw frame
                c.setStrokeColor(colors.HexColor("#333333"))
                c.setLineWidth(2)
                c.rect(x - 2, y - 2, render_w + 4, render_h + 4, stroke=1, fill=0)

                c.drawImage(img_path, x, y, width=render_w, height=render_h, preserveAspectRatio=True)
            else:
                c.setFillColor(colors.red)
                c.drawString(width/2 - 50, height/2, f"Missing: {img_name}")

        elif slide["type"] == "cta":
            # Title
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 48)
            text = slide["title"]
            w = c.stringWidth(text, "Helvetica-Bold", 48)
            c.drawString((width - w) / 2, height / 2 + 120, text)

            # Subtitle
            if "subtitle" in slide:
                c.setFillColor(SUBTEXT_COLOR)
                c.setFont("Helvetica", 28)
                text = slide["subtitle"]
                w = c.stringWidth(text, "Helvetica", 28)
                c.drawString((width - w) / 2, height / 2 + 50, text)

            # Box/Button
            btn_w = 640
            btn_h = 80
            btn_x = (width - btn_w) / 2
            btn_y = height / 2 - 80

            c.setFillColor(ACCENT_COLOR)
            c.rect(btn_x, btn_y, btn_w, btn_h, fill=1)

            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 28)
            btn_text = "Click here to read"
            w = c.stringWidth(btn_text, "Helvetica-Bold", 28)
            c.drawString((width - w) / 2, btn_y + (btn_h - 28) / 2 + 4, btn_text)

            # URL text (smaller below button)
            c.setFillColor(SUBTEXT_COLOR)
            c.setFont("Helvetica", 18)
            url_text = slide["url"]
            w = c.stringWidth(url_text, "Helvetica", 18)
            # if too long, maybe wrap? url is pretty long.
            # let's just draw it
            c.drawString((width - w) / 2, btn_y - 40, url_text)

            # PDF Link
            c.linkURL(slide["url"], (btn_x, btn_y, btn_x + btn_w, btn_y + btn_h), relative=0)

        c.showPage()

    c.save()
    print(f"PDF Carousel created successfully at: {OUTPUT_PDF}")

if __name__ == "__main__":
    create_carousel_safe()
