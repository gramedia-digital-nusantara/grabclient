import re


def snake_to_camel(text: str) -> str:
    return re.sub('_([a-zA-Z0-9])', lambda m: m.group(1).replace('url', 'URL').upper(), text)
