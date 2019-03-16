# Author : Macauley Scullion
# symtable.py 

# Symbol class - Name, Type, and Attribute
class Symbol:
    def __init__(self, name, type, value = None):
        self.name = name
        self.type = type
        self.value = value

# Symbol table array
symbol_table = []

# Operations of symbol table 
# Free - remove all entries and free storage 
def free():
    symbol_table.clear()
    print("Symbol table cleared")

# Lookup - search for a name and return pointer to entry
def lookup(name):
    # Check if the symbol table is empty
    if len(symbol_table) == 0:
            print("Symbol table empty")
            return False
    # For each symbol in the symbol table, check if the parameter name matches the symbol name
    else:
        for sym in symbol_table:
            if sym.name == name:
                print("symbol found: name - " + name)
                return sym
        return


# Insert - insert a name and return pointer to entry
def insert(name, type, value = None):
    # Lookup function call to check for matches 

    ## Must implement if true or false for lookup
        new_entry = Symbol(name, type, value)
        symbol_table.append(new_entry)
        print("Symbol appended: " + name)


# Set_attribute - associate an attribute with a given entry
def set_attribute(sym, value):
    sym.value = value

# Get_attribute - get an attribute associated with an entry
def get_attribute(sym):
    return sym.value