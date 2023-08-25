import pyfiglet

def print_all_styles_to_file(text, output_file):
    styles = pyfiglet.Figlet().getFonts()
    with open(output_file, "w") as f:
        for idx, style in enumerate(styles, start=1):
            fig = pyfiglet.Figlet(font=style)
            styled_text = fig.renderText(text)
            f.write(f"{idx}. Style: {style}\n")
            f.write(styled_text)
            f.write("\n\n")

if __name__ == "__main__":
    text_to_display = "SHELL SHARE"
    output_file = "output.txt"
    print_all_styles_to_file(text_to_display, output_file)
    print(f"Output written to {output_file}")



#xttyb, xsansb, xhelv, xhelv, xcour, utopiai, univers, unarmed_, ucf_fan_, type_set, ttyb, 1943____, 3x5, 4x4_offr,5lineoblique,5x7,6x10,6x9,advenger,aquaplan,ascii___,asc_____,assalt_m,asslt__m,atc_gran,banner,banner3,basic,beer_pub,big,bubble_b,c1______,char1___,char3___,clb6x10,coil_cop,com_sen_,demo_m__,digital,doom,drpepper,epic,etcrvs__,funky_dr,future_7,fuzzy,helv,helvi,hyper___,italic,kik_star,lcd,mig_ally,mcg_____,new_asci,ok_beer_,puffy,p_skateb,rad_____,rectangles,rok_____,sansb,sansbi,sbook,sbookb,sbooki,sbookbi,skateord,slant,straight,super_te,taxi____,times,tomahawk,

