#!/usr/bin/env python3.5

from matplotlib import pyplot as plt
import numpy as np
# %matplotlib inline
import pandas as pd
import csv
import sys
import re
import os

# subs
def trg_obj(line):
    line_mod = re.sub(r"\.o$", "", line)
    line_fname = re.sub(r"^.*/", "", line_mod)
    line_dir = re.match(r"^.*/", line).group()
    line_dir = re.sub(r"^ *", "", line_dir)
    files = os.listdir(line_dir)
    out = ""
    # print("##" + line_dir + " : " + line_fname)
    # print(files)
    for ff in files:        
        if ff.startswith(line_fname + "."):
            if not re.match(r".*\.h$", ff):
                # print("OBJ: " + line_dir + ff)
                out = line_dir + ff
    return out

    # print("OBJ: " + line_fname)

def trg_inc(line):
    line_mod = re.sub(r"^ -I../", "", line)
    # print("INC: " + line_mod)
    return line_mod


def trg_prcsr(line):
    cmds = re.findall(r"'.+?'", line)
    out = ""
    for cc in cmds:
        # print("# " + cc.replace("'", ""))
        out += cc.replace("'", "") + " "
    # print(out)
    return out

def trg_flags(line):
    out = line.replace(" ", "")
    return out


# keywords:
keywords = ["OBJECTS +=", "INCLUDE_PATHS +=", "LIBRARY_PATHS :=", "LIBRARIES :=", "LINKER_SCRIPT ?=", "AS      =", "CC      =", "CPP     =", "LD      =", "ELF2BIN =", "PREPROC =", "C_FLAGS +=", "CXX_FLAGS +=", "ASM_FLAGS +=", "LD_FLAGS :=", "LD_SYS_LIBS :="]


# Cmake lists
SRCS = []

INCS = []

C_FS = []
CXX_FS = []
ASM_FS = []

out_cmd_asm = ""
out_cmd_c = ""
out_cmd_cxx = ""
out_cmd_ld = ""
out_cmd_elf = ""
out_cmd_prep = ""

out_path_linker_script = ""




#パラメータ関係
if(len(sys.argv) != 2):
    print("Usage: %s filename" % sys.argv[0])
    quit()

#Makefileの読み込み
f_makefile = open(sys.argv[1], 'r')

for line in f_makefile:
    #print("line: " + line)
    for kwrd in keywords:
        # print(kwrd)
        if line.startswith(kwrd):
            #print("OK")
            line = line.rstrip()
            if kwrd == "OBJECTS +=":
                # OBJECTのとき
                src = trg_obj(line.replace(kwrd, ""))
                #print("OBJ: " + src)
                SRCS.append(src)
            elif kwrd == "INCLUDE_PATHS +=":
                # INCLUDE PATHのとき
                # print("INC: " + line.replace(kwrd, ""))
                incd = trg_inc(line.replace(kwrd, ""))
                if not incd == "":
                    #print("INC: " + incd)
                    INCS.append(incd)

            elif kwrd == "AS      =":
                print("AS: " + trg_prcsr(line.replace(kwrd, "")))
                out_cmd_asm = trg_prcsr(line.replace(kwrd, ""))

            elif kwrd == "CC      =":
                print("CC: " + trg_prcsr(line.replace(kwrd, "")))
                out_cmd_c = trg_prcsr(line.replace(kwrd, ""))

            elif kwrd == "CPP     =":
                print("CPP: " + trg_prcsr(line.replace(kwrd, "")))
                out_cmd_cxx = trg_prcsr(line.replace(kwrd, ""))

            elif kwrd == "LD      =":
                print("LD: " + trg_prcsr(line.replace(kwrd, "")))
                out_cmd_ld = trg_prcsr(line.replace(kwrd, ""))

            elif kwrd == "ELF2BIN =":
                print("ELF: " + trg_prcsr(line.replace(kwrd, "")))
                out_cmd_elf = trg_prcsr(line.replace(kwrd, ""))

            elif kwrd == "PREPROC =":
                print("PRO: " + trg_prcsr(line.replace(kwrd, "")))
                out_cmd_prep = trg_prcsr(line.replace(kwrd, ""))

            elif kwrd == "C_FLAGS +=":
                cf = trg_flags(line.replace(kwrd, ""))
                C_FS.append(cf)
                #print("C_F: " + cf)

            elif kwrd == "CXX_FLAGS +=":
                cxxf = trg_flags(line.replace(kwrd, ""))
                CXX_FS.append(cxxf)
                #print("CXX_F: " + cxxf)

            elif kwrd == "ASM_FLAGS +=":
                asmf = trg_flags(line.replace(kwrd, ""))
                ASM_FS.append(asmf)
                #print("ASM_F: " + asmf)

            elif kwrd == "LD_FLAGS :=":
                print("LD_F: " + trg_flags(line.replace(kwrd, "")))

            elif kwrd == "LD_SYS_LIBS :=":
                print("LD_SYS_F: " + trg_flags(line.replace(kwrd, "")))

            elif kwrd == "LIBRARY_PATHS :=":
                print("L_P: " + trg_flags(line.replace(kwrd, "")))

            elif kwrd == "LIBRARIES :=":
                print("LIBS: " + trg_flags(line.replace(kwrd, "")))

            elif kwrd == "LINKER_SCRIPT ?=":
                print("LS: " + trg_flags(line.replace(kwrd + " ../", "")))
                out_path_linker_script = re.sub(r"^\.", "${PROJECT_SOURCE_DIR}",trg_flags(line.replace(kwrd + " ../", "")))

            else:
                pass

#print(SRCS)
out_srcs = "SET(SRCS"
for s in SRCS:
    out_srcs += " " + re.sub(r"^\.", "${PROJECT_SOURCE_DIR}", s)
out_srcs += ")"
print("######################################")
print(out_srcs)

# print(INCS)
out_include_dir = "SET(INCDIR"
for s in INCS:
    out_include_dir += " " + re.sub(r"^\.", "${PROJECT_SOURCE_DIR}", s)
out_include_dir += ")"
print("######################################")
print(out_include_dir)

# print(C_FS)
out_c_flags = "SET(CFLGS \""
for s in C_FS:
    out_c_flags += " " + s
out_c_flags += "\")"
print("######################################")
print(out_c_flags)


# print(CXX_FS)
out_cxx_flags = "SET(CXXFLGS \""
for s in CXX_FS:
    out_cxx_flags += " " + s
out_cxx_flags += "\")"
print("######################################")
print(out_cxx_flags)


# print(ASM_FS)
out_asm_flags = "SET(ASMFLGS \""
for s in ASM_FS:
    out_asm_flags += " " + s
out_asm_flags += "\")"
print("######################################")
print(out_asm_flags)


print("######################################")
print("SET(ASM_CMD \"" + out_cmd_asm.replace("arm-none-eabi-gcc", "") + "\")")

print("######################################")
print("SET(C_CMD \"" + out_cmd_c.replace("arm-none-eabi-gcc", "") + "\")")

print("######################################")
print("SET(CXX_CMD \"" + out_cmd_cxx.replace("arm-none-eabi-g++", "") + "\")")

print("######################################")
print("SET(LD_CMD " + out_cmd_ld + ")")

print("######################################")
print("SET(ELF_CMD " + out_cmd_elf + ")")

print("######################################")
print("SET(PREP_CMD " + out_cmd_prep + ")")

print("######################################")
print("SET(LINKER_SCRIPT_PATH " + out_path_linker_script + ")")


f_makefile.close()


