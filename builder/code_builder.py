class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.field_value = {}

    def add_field(self, field, value):
        self.field_value.update({field: value})
        return self

    def __str__(self):
        constructor_body_line = '\n    self.{field} = {value}'
        constructor_body = ''
        for field, value in self.field_value.items():
            constructor_body += constructor_body_line.format(field=field, value=value)
        init_function_declaration = '\n  def __init__(self):'
        class_declaration = f'class {self.root_name}:'
        final_constructed = class_declaration +\
        ((init_function_declaration + constructor_body) if constructor_body else '\n  pass')
        return final_constructed
