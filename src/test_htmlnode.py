import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("i", "Click Me!")
        node = ParentNode("a", [child_node], {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com"><i>Click Me!</i></a>',
        )

    def test_emptylist_children(self):
        node = ParentNode("a", [], None)
        self.assertEqual(node.to_html(), '<a></a>')

    def test_empty_children(self):
        node = ParentNode("a", None, None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()