import re

def highlight_html(text_widget):
    # Remove previous tags
    text_widget.tag_remove("html_tag", "1.0", "end")
    text_widget.tag_remove("html_attr", "1.0", "end")
    text_widget.tag_remove("html_string", "1.0", "end")
    text_widget.tag_remove("html_comment", "1.0", "end")

    content = text_widget.get("1.0", "end-1c")

    # Highlight comments
    for match in re.finditer(r'<!--.*?-->', content, re.DOTALL):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("html_comment", start, end)

    # Highlight tags
    for match in re.finditer(r'</?\w+[^>]*>', content):
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("html_tag", start, end)
        # Highlight attributes inside tag
        tag_content = match.group()
        for attr in re.finditer(r'(\w+)(\s*=\s*)', tag_content):
            attr_start = match.start() + attr.start(1)
            attr_end = match.start() + attr.end(1)
            text_widget.tag_add("html_attr", f"1.0+{attr_start}c", f"1.0+{attr_end}c")
        # Highlight strings inside tag
        for string in re.finditer(r'"[^"]*"|\'[^\']*\'', tag_content):
            str_start = match.start()