class Box:
    pass

box = Box()

# Create a width attribute.
# Useful when you dont now attribute name. In flow. Like object[attribute] in js
setattr(box, "width", 15)

# equal
box.height = 10
