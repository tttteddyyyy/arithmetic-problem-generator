from math_pdf import MathPDF

def main():
    # ✅ Create PDF and add math problems
    pdf = MathPDF()
    pdf.add_math_problems(pdf.generate_problems())
    pdf.save_pdf("math_problems.pdf")

if __name__ == "__main__":
    main()