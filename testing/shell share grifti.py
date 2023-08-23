import pyfiglet

def print_all_styles_to_file(text, output_file):
    styles = pyfiglet.Figlet().getFonts()
    with open(output_file, "w") as f:
        for style in styles:
            fig = pyfiglet.Figlet(font=style)
            styled_text = fig.renderText(text)
            f.write(f"Style: {style}\n")
            f.write(styled_text)
            f.write("\n\n")

if __name__ == "__main__":
    text_to_display = "SHELL SHARE"
    output_file = "output.txt"
    print_all_styles_to_file(text_to_display, output_file)
    print(f"Output written to {output_file}")

xttyb, xsansb, xhelv, xhelv, xcour, utopiai, univers, unarmed_, ucf_fan_, type_set, ttyb, 

