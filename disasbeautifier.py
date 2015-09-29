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

def parse_line(line):
    m = re.search(' +(0x[a-f0-9]+)(?: <\+[0-9]+>)?: +([a-zA-Z0-9]+)(?: +(.*))?', line)
    if m:
        return {
            'address': m.group(1),
            'instruction': m.group(2),
            'parameters': m.group(3)
        }
    return None

def get_max_len(f):
    line_sizes = []
    for line in f:
        line_sizes.append(len(line))
    max_line_size = (max(line_sizes)/4)*4 +4
    f.seek(0)
    return max_line_size

def generate_line(line, max_len):
    jumps = ['JO', 'JNO', 'JS', 'JNS', 'JE', 'JZ', 'JNE', 'JNZ', 'JB', 'JNAE', 'JC', 'JNB', 'JAE', 'JNC', 'JBE', 'JNA', 'JA', 'JNBE', 'JL', 'JNGE', 'JGE', 'JNL', 'JLE', 'JNG', 'JG', 'JNLE', 'JP', 'JPE', 'JNP', 'JPO', 'JCXZ', 'JECXZ']
    diff = max_len - len(line)
    line_content = parse_line(line)
    
    new_line = line[:-1] + " "*diff + "; "
        
    if line_content:
        print ":" + line_content['instruction'] + ":"
        if line_content['instruction'] == 'call':
                m = re.search('<(.*)(?:@(.*))?>', line)
                if m:
                    new_line += m.group(1) + "()"

        if (line_content['instruction'].upper() in jumps
            or line_content['instruction'] == "int3"):
            new_line += "\n"

        if line_content['instruction'] == "ret":
            new_line += "\n\n " + "*"*(max_len-3) + " ; \n"
    return new_line

def generate_file(input_filename, output_filename):

    input_file  = open(input_filename, 'r')
    output_file = open(output_filename, 'w+')
    max_line_size = get_max_len(input_file)

    for line in input_file:
        new_line = generate_line(line, max_line_size)
        output_file.write(new_line + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage : %s input output\n" % sys.argv[0])
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.isfile(input_filename):
        sys.stderr.write("%s not found\n" % input_filename)
        sys.exit(1)

    generate_file(input_filename, output_filename)
