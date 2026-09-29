import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestInline_Markdown(unittest.TestCase):
    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_invalidMarkdown(self):
        with self.assertRaises(Exception):
            node = TextNode("This is text with a `code block word", TextType.TEXT)
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_inline_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_nontexttype(self):
        node = TextNode("This is text with an _italic_ word", TextType.ITALIC)
        node_list = [node]
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
                    node_list,
                    new_nodes,
                )


if __name__ == "__main__":
    unittest.main()