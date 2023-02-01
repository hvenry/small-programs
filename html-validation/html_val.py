# Validates a string of html tag formatting with a stack called opening_tags
def Validate_html(html: str) -> str:
    # keep track of opening tags, current tag, and if we are inside a tag
    opening_tags = []
    curr_tag = ""
    in_tag = False

    # iterate through all of the chars in the html line
    for i in range(len(html)):        
        # if current char is a '<' we are inside a tag
        if html[i] == '<':
            in_tag = True
        
        # if current char is a '>' we have completed the tag
        if html[i] == '>':
            # if the curr_tag is not a closing tag, add it to our opening_tags stack
            if curr_tag[0] != '/':
                opening_tags.append(curr_tag)
            # if curr_tag is a closing tag, we then see if it is in the top of the stack
            else:
                # if the closing tag is not on the top of the stack, the tag formatting is incorrect
                if not opening_tags or '/' + opening_tags[-1] != curr_tag:
                    # return the tag that should have been changed (the first tag in the stack)
                    return opening_tags[-1]
                # if the closing tag is on top of the stack, pop the opening tag off it
                else:
                    opening_tags.pop()

            # set curr_tag back to empty and in_tag to false
            curr_tag = ""
            in_tag = False
        
        # if we are in the tag, add the current letter to it
        if in_tag and (html[i] != '<' and html[i] != '>'):
                curr_tag += html[i]
    
    # return empty string if html tags are formatted correctly
    return ""


def main():
    # returns nothing
    # html_string = "<div><b><p>hello world</p></b></div>"

    # returns div

    # function gets to </b>, removes <b> from stack,
    # then gets to </div>, removes <div> from stack,
    # then gets to </p>, returns div
    html_string = "<div><div><b></b></div></p>"

    # returns i
    # html_string = "<div>abc</div><p><em><i>test test test</b></em></p>"
    print(Validate_html(html_string))


main()