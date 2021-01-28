import re

_postcode_splitter = re.compile(r'[\W_]+')

def parse_regex(postcode_input):
    if postcode_input is None:
        return None
        
    # escape and split into chunks
    input_parts = re.split(
        _postcode_splitter, 
        re.escape(postcode_input))

    # trim whitespace
    input_parts = list(map(
        lambda chunk: chunk.strip(),
        input_parts))

    # remove empty
    input_parts = list(filter(
        lambda part: len(part) > 0,
        input_parts))

    if len(input_parts) == 0 or len(input_parts) > 2: 
        return None

    postcode_pattern = ".*%s.*" % '\\s*'.join(input_parts)

    return re.compile(postcode_pattern, re.IGNORECASE)

def postcode_match(postcode_regex, store_postcode):
    if re.match(postcode_regex, store_postcode):
        return True

    squanshed = re.sub(' ', '', store_postcode)
    if re.match(postcode_regex, squanshed):
        return True
    
    return False