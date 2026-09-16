import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        node = HTMLNode(
            tag="div",
            value="hello",
            props={"class": "greeting"},
        )
        self.assertEqual(node.props_to_html(), ' class="greeting"')

    def test_props_to_html_none(self):
        node = HTMLNode(
            tag="div",
            value="hello",
            props=None,
        )
        self.assertEqual(node.props_to_html(), "")

    def test_missing_node(self):
        node = HTMLNode(
            tag="div",
            value=None,
            props={"class": "greeting"},
        )
        self.assertIsNone(node.value)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_wprops(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_VE(self):
        node = LeafNode("p", None) 
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()