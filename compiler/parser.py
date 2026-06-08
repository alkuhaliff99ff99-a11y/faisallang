class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        ast = [] # هذه هي الخارطة
        while self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            
            if token.type == "LET":
                # نأخذ اسم المتغير والقيمة
                name = self.tokens[self.pos + 1].value
                value = self.tokens[self.pos + 3].value
                ast.append(("LET", name, value))
                self.pos += 4 # نتخطى الكلمات التي قرأناها
            elif token.type == "PRINT":
                value = self.tokens[self.pos + 1].value
                ast.append(("PRINT", value))
                self.pos += 2
            else:
                self.pos += 1
        return ast
