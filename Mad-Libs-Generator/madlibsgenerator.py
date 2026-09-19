import string

templates = {
    "wildlife": "The {adjective} {noun} decided to {verb} the {food} at the {place}.",
    "mystery": "The {adjective1} Detective {noun1} found a {adjective2} {noun2} lying on the {object} at the {place}.",
    "adventure": "In the {adjective} jungle, the {noun} had to {verb} for {object} to survive.",
    "romance": "The {adjective} {noun} met his {adjective2} {noun2} at the {place}, and he decided to {verb1} {noun3} until she {verb2}."
}

print("Choose a theme:")
for theme in templates:
    print(f"- {theme}")

chosen_theme = input("Which theme do you choose? ").lower()
if chosen_theme not in templates:
    print("No template with that theme exists.")

elif chosen_theme in templates:
    template = templates[chosen_theme]
    
    """creating the tool: formatter, that'll parse the template and extract the field names"""
    """ string.Formatter: builds a new formatter object in the memory, with abilities of Formatter class attached to it (like the method: .parse()).
        same pattern from list() or dict() — calling them (list()) constructs an actual empty list/dict object.
    """
    formatter = string.Formatter()

    """string.Formatter().parse() is built to scan a string looking for the text inside the {}
       it returns a sequence of 4-item tuples, one per chunk of the template:
       (literal_text, field_name, format_spec, conversion) in this exact order, where literal_text is the text between the fields, field_name is the name of the field, format_spec is any formatting instructions, and conversion is any conversion flags."""
    """ if field: checks if the field is not None or empty, and if so, it adds it to the list of field names."""
    """ The number and order of names has to match the shape of what is being unpacked, 
        and _ is used instead of a real name as a signal that those particular values are being deliberately ignored."""
    """ list comprehension general syntax: [expression for item in iterable if condition]
        expression: what to put in the new list (here: field("noun,..)) """
    
    field_names = [field for _, field, _, _ in formatter.parse(template) if field]

    """DEBUGging: print the field names and template to verify they are correct."""
    """ print("DEBUG field_names:", field_names)
        print("DEBUG template:", template)"""


    """ answers is a dict because each value needs to be tagged with which blank it fills, 
        and .format(**answers) specifically requires that tagging to be in key-value for"""

    answers = {}

    for field in field_names:
        answers[field] = input(f"Enter a word for {field}: ")

    """ .format() is a string method that fills in {} placeholders — an older sibling of f-strings,
        used specifically because f-strings need the values available inline at string-creation time, 
        but the other's filling in a template that already exists as plain text, using a dict of answers gathered separately."""
    """ **answers: unpacks the dict, turning {"adjective": "silly", "noun": "cat"} into the equivalent of writing adjective="silly", noun="cat" directly as arguments to .format()"""

    story = template.format(**answers)
    print("Your story:")
    print(story)
