from typing import Any
import ast

from checkpy import static

def has_syntax_error():
    try:
        compile(static.getSource(), "<your program>", "exec")
    except SyntaxError as error:
        return error.lineno
    return False

def has_string(*forbidden_strings):
    source = static.getSource()
    return any(f in source for f in forbidden_strings)

def has_call(*banned_calls) -> bool:
    found = False

    class Visitor(ast.NodeVisitor):
        def visit_Name(self, node: ast.Name) -> Any:
            if node.id in banned_calls:
                nonlocal found
                found = True

    calls: list[ast.Call] = static.getAstNodes(ast.Call)
    for call in calls:
        Visitor().visit(call)

    return found

def has_import(*banned_imports) -> bool:
    imports: list[ast.Import] = static.getAstNodes(ast.Import)
    for imp in imports:
        names = [alias.name for alias in imp.names]
        for name in names:
            if name in banned_imports:
                return True

    imports_from: list[ast.ImportFrom] = static.getAstNodes(ast.ImportFrom)
    for imp in imports_from:
        for name in imp.names:
            if name in banned_imports:
                return True

    return False

def has_generators() -> bool:
    return static.getAstNodes(ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)
