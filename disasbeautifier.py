#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import os.path
import re

"""

disasbeautifier.py

Author : hackndo
Version : 1.0
Description : Take disas ouput from gdb (either intel or at&t syntax), parse it and write it in output_file
Usage : ./disasbeautifier.py input_file output_file

"""
arch = 32
jumps = ['JMP', 'JO', 'JNO', 'JS', 'JNS', 'JE', 'JZ', 'JNE', 'JNZ', 'JB', 'JNAE', 'JC', 'JNB', 'JAE', 'JNC', 'JBE', 'JNA', 'JA', 'JNBE', 'JL', 'JNGE', 'JGE', 'JNL', 'JLE', 'JNG', 'JG', 'JNLE', 'JP', 'JPE', 'JNP', 'JPO', 'JCXZ', 'JECXZ']

def parse_line(line):
    if (line[-1:] != "\n"): line += "\n"
    m = re.search(' +(0x[a-f0-9]+)(?: <\+[0-9]+>)?: +([a-zA-Z0-9]+)(?: +([^,]*)(?:,([^,]*))?)?\n', line)
    if m:
        return {
            'address': parse_address(m.group(1)),
            'instruction': m.group(2),
            'parameters': [m.group(3), m.group(4)]
        }
    return None

def parse_address(address):
    address = address.split("x")
    if arch == 32:
        address = "0x%08x" % int(address[1], 16)
    elif arch == 64:
        address = "0x%016x" % int(address[1], 16)
    return address

def cmp_addr(addr1, addr2):
    if int(addr1, 16) < int(addr2, 16):
        return -1
    elif int(addr1, 16) == int(addr2, 16):
        return 0
    else:
        return 1

def get_max_len(f):
    line_sizes = []
    for line in f:
        line_sizes.append(len(line))
    max_line_size = (max(line_sizes)/4)*4 +4
    f.seek(0)
    return max_line_size

def generate_line(line, max_len):
    lines = []
    diff = max_len - len(line)
    line_content = parse_line(line)
    
    # Add comments at end of line
    new_line = line[:-1] + " "*diff + "; "

    # If line is not blank
    if line_content:

        # If it's a call
        if line_content['instruction'] == 'call':
                m = re.search('<([a-zA-Z0-9_\-]*)(?:@(.*))?>', line)
                if m:
                    # Comment with function name is added
                    new_line += m.group(1) + "()"
        lines.append({'line': new_line, 'line_content': line_content})
        # If it's a jump or an int3
        if (line_content['instruction'].upper() in jumps
            or line_content['instruction'] == "int3"):
            # We add a new line (visual bloc)
            lines.append({'line': '', 'line_content': None})

        # If it's a ret
        if line_content['instruction'] == "ret":
            # It's a function end so we add a separation
            lines.append({'line': '', 'line_content': None})
            lines.append({'line': '   ***************', 'line_content': None})
            lines.append({'line': '', 'line_content': None})
    else:
        lines.append({'line': new_line, 'line_content': line_content})

    return lines

def parse(input_filename):
    input_file  = open(input_filename, 'r')
    max_line_size = get_max_len(input_file)
    lines = []
    jumps_end = {}
    for line in input_file:
        generated_lines = generate_line(line, max_line_size)
        for generated_line in generated_lines:
            lines.append(generated_line)
    jmp = {}
    for line in lines:
        if line['line_content'] and line['line_content']['instruction'].upper() in jumps:
            origin = line['line_content']['address']
            destination = line['line_content']['parameters'][0].split(" ", 1)[0]
            jmp[origin] = parse_address(destination)

    padding = 5 + len(jmp) - 1

    for line in lines:
        line['line'] = " "*padding  + line["line"]

    arrows = {}
    i = 0
    for o, d in jmp.items():
        is_jumping = False
        occurences = []
        for l, line in enumerate(lines):
            if lines[l]['line_content']:
                if lines[l]['line_content']['address'] == o:
                    is_jumping = True
                elif lines[l]['line_content']['address'] == d:
                    is_jumping = False
                elif is_jumping:
                    occurences.append(lines[l]['line'][0:padding].count('|'))
            elif is_jumping:
                occurences.append(lines[l]['line'][0:padding].count('|'))

        is_jumping = False

        i = max(occurences)+1
        invert = False
        if cmp_addr(o, d) > 0:
            invert = True
        if invert:
            lines.reverse()
        
        for l, line in enumerate(lines):
            if lines[l]['line_content']:
                if lines[l]['line_content']['address'] == o:
                    lines[l]['line'] = " "*(padding - 3 - i) + "+" + "-"*i + "- " + lines[l]["line"][padding:]
                    is_jumping = True
                elif lines[l]['line_content']['address'] == d:
                    lines[l]['line'] = " "*(padding - 3 - i) + "+" + "-"*i + "> " + lines[l]["line"][padding:]
                    is_jumping = False
                elif is_jumping:
                    lines[l]['line'] = " "*(padding - 3 - i) + "|" + lines[l]["line"][padding-2-i:]
            elif is_jumping:
                lines[l]['line'] = " "*(padding - 3 - i) + "|" + lines[l]["line"][padding-2-i:]
        if invert:
            lines.reverse()
    leading_spaces = []
    for line in lines:
        leading_spaces.append(len(line['line']) - len(line['line'].lstrip(' ')))
    first_char = min(leading_spaces)
    for line in lines:
        line['line'] = line['line'][first_char:]
    return lines


def write_file(output_filename, lines):
    output_file = open(output_filename, 'w+')
    for line in lines:
        output_file.write(line['line'] + '\n')

def generate_file(input_filename, output_filename):
    lines = parse(input_filename)
    write_file(output_filename, lines)

if __name__ == "__main__":
    sys.argv.append("/home/romain/Desktop/trap.asm")
    sys.argv.append("./outputfile.asm")
    
    if len(sys.argv) != 3:
        sys.stderr.write("Usage : %s input output\n" % sys.argv[0])
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.isfile(input_filename):
        sys.stderr.write("%s not found\n" % input_filename)
        sys.exit(1)

    generate_file(input_filename, output_filename)
