class TextNode():
    
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other_text_node):
        if self.text == other_text_node.text and self.text_type == other_text_node.text_type and self.url == other_text_node.url:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"(TextNode:({self.text}, {self.text_type}, {self.url}))"
    