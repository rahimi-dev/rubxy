from enum import Enum

class AutoName(str, Enum):
    def _generate_next_value_(self, *args):
        return ''.join(word.capitalize() for word in self.split('_'))
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        return super().__eq__(other)
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"'{self.value}'"
    
    def __hash__(self):
        return hash(self.value)