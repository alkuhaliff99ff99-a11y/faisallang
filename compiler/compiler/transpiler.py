class Transpiler:

    def __init__(self, ast):

        self.ast = ast

    def generate(self):

        output = []

        i = 0

        while i < len(self.ast):

            token = self.ast[i]

            if token.value == "اطبع":

                name = self.ast[i + 1].value

                output.append(f"print({name})")

            i += 1

        return "\n".join(output)
