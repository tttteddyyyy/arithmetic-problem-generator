import os
import random
from fpdf import FPDF

FONT_PATH = os.path.expanduser("~/Library/Fonts/Arial Unicode.ttf")

class MathPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        
        # ✅ Register Unicode font for multilingual support
        self.add_font("ArialUnicode", style="", fname=FONT_PATH, uni=True)
        self.set_font("ArialUnicode", size=14)

    def generate_problems(self, size: int = 10) -> list:
        ret = []
        for i in range(size):
            sign = "+" if random.randint(0,1) == 0 else "-"
            v1, v2 = random.randint(1, 99), random.randint(1, 99)
            if sign == "-":
                ret.append(f"{v1} + {v2} =")
            elif v1 > v2:
                ret.append(f"{v1} - {v2} =")
            else:
                ret.append(f"{v2} - {v1} =")
                
        return ret

    
    def add_math_problems(self, problems):
        """
        Print math problems on A4 size pages with 10 problems arranged in 2 columns
        problems: list of problem strings
        """
        col1_x, col2_x = 10, 110  # Column positions (left, right)
        y_start = 30              # Starting position of the first problem
        y_gap = 30                # Gap between problems
        problems_per_page = 10    # Number of problems per page

        for i, problem in enumerate(problems):
            col_x = col1_x if i % 2 == 0 else col2_x  # Even numbers on left, odd numbers on right
            y_pos = y_start + (i // 2) * y_gap  # Vertical position

            # Add a new page if needed
            if i % problems_per_page == 0 and i != 0:
                self.add_page()
                y_pos = y_start  # Start from the top again on a new page

            self.text(col_x, y_pos, f"{problem}")  # Print the problem

    def save_pdf(self, output_file="math_problems.pdf"):
        self.output(output_file)
        print(f"✅ PDF file created successfully: {output_file}")