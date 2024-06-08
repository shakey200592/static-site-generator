import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    
    def test_eq(sef):
        node = TextNode("This is a text node", TextNode.text_types["bold"])
        node2 = TextNode("This is a text node", TextNode.text_types["bold"])
        sef.assertEqual(node, node2)
        
    def test_url_equal(self):
        node = TextNode("This is a text node", TextNode.text_types["large_heading"], "www.test.com")
        node2 = TextNode("This is another text node", TextNode.text_types["small_heading"], "www.test.com")
        self.assertEqual(node.url, node2.url)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", TextNode.text_types["large_heading"])
        node2 = TextNode("This is another text node", TextNode.text_types["small_heading"])
        self.assertNotEqual(node, node2)
        
    def test_not_eq_2(self):
        node = TextNode("This is a text node", TextNode.text_types["large_heading"])
        node2 = TextNode("This is another text node", TextNode.text_types["large_heading"])
        self.assertNotEqual(node,node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", TextNode.text_types["large_heading"], "www.test.com")
        self.assertEqual("TextNode: (This is a text node, large-heading, www.test.com)", repr(node))
        
    def test_repr2(self):
        node = TextNode("This is a text node", TextNode.text_types["large_heading"])
        self.assertEqual("TextNode: (This is a text node, large-heading, None)", repr(node))
if __name__ == "__main__":
    unittest.main()