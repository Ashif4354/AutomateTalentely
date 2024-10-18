import clex
import ply

def check_c_syntax(code):
  """Checks the syntax of a C program and prints any error messages.

  Args:
    code: A string containing the C code to be checked.
  """

  lexer = clex.lex()
  lexer.input(code)

  parser = ply.yacc.parser()
  try:
    parser.parse(lexer.token())
  except ply.lex.LexError as e:
    print(e)
  except ply.yacc.YaccError as e:
    print(e)

if __name__ == '__main__':
  code = """
    int main() {
      printf("Hello, world!\n");
      return 0;
    }
  """

  check_c_syntax(code)
