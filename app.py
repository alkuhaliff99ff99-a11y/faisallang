# app.py
import gradio as ui
import sys
import io
import os
from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.memory_analyzer import GhostMemoryAnalyzer
from compiler.transpiler import Transpiler

def run_faisal_lang(code):
    """المحرك المركزي لتشغيل الشفرة وتدقيقها"""
    if not code.strip():
        return "⚠️ الرجاء كتابة شفرة برمجية.", "مستقر"

    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()

    try:
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse_program()
        analyzer = GhostMemoryAnalyzer()
        analyzer.analyze(ast)
        transpiler = Transpiler()
        python_code = transpiler.transpile(ast)

        exec_globals = {}
        exec(python_code, exec_globals)

        sys.stdout = old_stdout
        output = redirected_output.getvalue()
        return output if output else "✅ تم التنفيذ بنجاح.", "🟢 آمن ومستقر"

    except Exception as e:
        sys.stdout = old_stdout
        return f"❌ خطأ تنفيذ:\n{str(e)}", "🔴 تم رصد تضارب!"

# بناء الواجهة
with ui.Blocks(theme=ui.themes.Soft(primary_hue="green")) as demo:
    ui.Markdown("# 🚀 FaisalLang Playground")
    
    with ui.Row():
        with ui.Column(scale=2):
            code_input = ui.Code(label="📝 محرر شفرة فيصل", language="python", lines=12, value="دع س = ٥\nاطبع(س)")
            run_btn = ui.Button("⚡ تشغيل", variant="primary")
        
        with ui.Column(scale=1):
            output_display = ui.Textbox(label="🖥️ المخرجات", lines=8, interactive=False)
            status_display = ui.Label(label="🛡️ الحالة")

    run_btn.click(fn=run_faisal_lang, inputs=code_input, outputs=[output_display, status_display])

# التكوين النهائي لإطلاق التطبيق (جاهز للرفع)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    
    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        show_error=True
    )
