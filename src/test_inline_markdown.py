import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [link](https://bootdev.com)"
        )
        self.assertListEqual([("link", "https://bootdev.com")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with two links [link](https://bootdev.com) [link2](https://www.youtube.com)"
        )
        self.assertListEqual([("link", "https://bootdev.com"), ("link2", "https://www.youtube.com")], matches)

    def test_mixed_image_link(self):
        matches = extract_markdown_images(
            "This is text with an image and a link ![image](https://i.imgur.com/zjjcJKZ.png) [link](https://bootdev.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_empty_sentence(self):
        matches = extract_markdown_images(
            "This is text with no image or link"
        )
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()