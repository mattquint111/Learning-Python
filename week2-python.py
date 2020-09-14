# CLasses & Objects

# Create Class: table

class Table:
    
    def __init__(self, width, height, material):
        self.width = width
        self.height = height
        self.material = material

table1 = Table('100', '50', 'oak')
table2 = Table('150', '65', 'steel')

print(table1.material)
print(table2.material)