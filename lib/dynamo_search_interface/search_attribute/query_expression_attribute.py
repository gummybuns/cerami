from .search_attribute import SearchAttribute

class QueryExpressionAttribute(SearchAttribute):
    def __init__(self, name, value=None):
        value = value or []
        super(QueryExpressionAttribute, self).__init__(name, value)

    def add(self, expression):
        self.value.append(expression)

    def build(self):
        return ' and '.join(str(expr) for expr in self.value)
