import sys

if __name__ == '__main__':
  filename = sys.argv[1]
	lexer = BasicLexer()
	parser = BasicParser()
	env = {}
	
	while True:
		
		try:
      with open(f'{codefile}', 'r') as f:
			  text = f.read()
		
		except EOFError:
			break
		
		if text:
			tree = parser.parse(lexer.tokenize(text))
			BasicExecute(tree, env)
