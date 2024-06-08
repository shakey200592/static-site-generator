class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        to_html = ""
        for key,value in self.props.items():
            to_html += f' {key}="{value}"'
        print(to_html)
        
    def __repr__(self):
        return f"HTMLNode: ({self.tag}, {self.value}, children: {self.children}, {self.props})"
        
        
node = HTMLNode("p", "this is a paragraph", "" ,{"style": "color:red", "class": "paragraph-class"})
print(node)