def insert_values(input_table, values):
    for name, entry in input_table.inputs.items():
        entry.delete(0, 'end')
        entry.insert(0, values[name])


def get_values(input_table):
    values = {}
    for name, entry in input_table.inputs.items():
        values[name] = entry.get()
    return values
