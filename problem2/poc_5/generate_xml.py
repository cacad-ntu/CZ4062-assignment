xml_content = """
<?xml version="1.0"?>
<story>
  <storyinfo>
    <author>John Fleck</author>
    <datewritten>June 2, 2002</datewritten>
    <keyword>example keyword</keyword>
  </storyinfo>
"""
+ " " * 4294967296 + 
"""
  <body>
    <headline>This is the headline</headline>
    <para>This is the body text.</para>
  </body>
</story>
"""

with open("large.xml", 'w') as out_file:
    out_file.write(xml_content)