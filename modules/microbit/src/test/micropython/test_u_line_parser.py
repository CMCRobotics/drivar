from u_line_parser import *

parsed = parse_lineprotocol_message("temperature,location=Paris c=28,f=82 28")
print(parsed[0])
print(parsed[1]["location"])
print(parsed[2]["c"])
print(parsed[2]["f"])
print(parsed[3])

print("=======")
parsed = parse_lineprotocol_message("temperature,location=Paris 28")
print(parsed[0])
print(parsed[1]["location"])
print(parsed[3])

print("=======")
parsed = parse_lineprotocol_message("temperature 28")
print(parsed[0])
print(parsed[3])

print("=======")
parsed = parse_lineprotocol_message("temperature c=28,f=82 28")
print(parsed[0])
print(parsed[1])
print(parsed[2]["c"])
print(parsed[2]["f"])
print(parsed[3])