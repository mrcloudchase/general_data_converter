import xml.etree.ElementTree as ET

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Convert the XML tree to a dictionary
    data = {}
    for child in root:
        data[child.tag] = child.text

    return data

def write_xml(data, file_path):
    root = ET.Element('root')

    for key, value in data.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(file_path)
