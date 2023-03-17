// book Simplifying 3D printing, chapter 5, page 125
display_text="AB";
text_len = len(display_text);
echo(text_len);
font = "Courier New:style=Regular";
linear_extrude(5)
    text(display_text, font=font);

cube([text_len*8.3,9,2]);