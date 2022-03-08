from string import Template
madlib_template_text = open('madlib_template.html').read()
template = Template(madlib_template_text)

madlib_html = template.safe_substitute(
    title="Hallowe'en",
    plural_noun_1 = "pencils",
    plural_noun_2 = "bananas",
    plural_noun_3 = "cigars",
    noun_1 = "grandfather clock",
    noun_2 = "moped",
    noun_3 = "scissors",
    noun_4 = "eraser",
    verb_1 = "dance",
    verb_2 = "cook",
    adverb_1 = "slowly",
)
open('madlib.html', 'w+').write(madlib_html)
