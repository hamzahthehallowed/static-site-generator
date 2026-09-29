from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = list()
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("Invalid Markdown Syntax")
            else: 
                for i, part in enumerate(parts):
                    if part != "":
                        if i % 2 == 0:
                            new_list.append(TextNode(part, TextType.TEXT))
                        else:
                            new_list.append(TextNode(part, text_type))
    return new_list