# faisallang/ast.py

from dataclasses import dataclass, field
from typing import List, Optional


class ASTNode:
    pass


@dataclass
class Program(ASTNode):
    statements: List[ASTNode] = field(default_factory=list)


@dataclass
class Number(ASTNode):
    value: int


@dataclass
class String(ASTNode):
    value: str


@dataclass
class Boolean(ASTNode):
    value: bool


@dataclass
class Variable(ASTNode):
    name: str


@dataclass
class VariableDeclaration(ASTNode):
    name: str
    value: ASTNode


@dataclass
class Assignment(ASTNode):
    name: str
    value: ASTNode


@dataclass
class BinaryOperation(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode


@dataclass
class UnaryOperation(ASTNode):
    operator: str
    operand: ASTNode


@dataclass
class PrintStatement(ASTNode):
    expression: ASTNode


@dataclass
class IfStatement(ASTNode):
    condition: ASTNode
    then_body: List[ASTNode]
    else_body: Optional[List[ASTNode]] = None


@dataclass
class WhileStatement(ASTNode):
    condition: ASTNode
    body: List[ASTNode]


@dataclass
class FunctionDeclaration(ASTNode):
    name: str
    parameters: List[str]
    body: List[ASTNode]


@dataclass
class FunctionCall(ASTNode):
    name: str
    arguments: List[ASTNode]


@dataclass
class ReturnStatement(ASTNode):
    value: Optional[ASTNode]


@dataclass
class ClassDeclaration(ASTNode):
    name: str
    methods: List[FunctionDeclaration]


@dataclass
class ObjectCreation(ASTNode):
    class_name: str


@dataclass
class MethodCall(ASTNode):
    object_name: str
    method_name: str
    arguments: List[ASTNode]


@dataclass
class ImportStatement(ASTNode):
    module_name: str


@dataclass
class Block(ASTNode):
    statements: List[ASTNode]


@dataclass
class ListLiteral(ASTNode):
    elements: List[ASTNode]


@dataclass
class DictionaryLiteral(ASTNode):
    pairs: List[tuple]


@dataclass
class IndexAccess(ASTNode):
    object_expr: ASTNode
    index_expr: ASTNode


@dataclass
class PropertyAccess(ASTNode):
    object_expr: ASTNode
    property_name: str
