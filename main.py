from grammar_parser import tokenize, parse
modes = ["parse_expression", "parse_program"]

code = '''
begin 
    v := not(-(+2.4 + 3/2)) <> not (100.0/(a + b)-28*0.001);
    a:=2/4;
    b :=a;
    c := not (100.0/(25 + 46)-28*0.001);
end
'''

if __name__ == '__main__':
    tokens = tokenize(code)
    print(tokens)
    parse(modes[1], tokens)
