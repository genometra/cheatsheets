#! /usr/bin/python
# -*- coding: utf-8 -*-
# Compila el ficheros LaTeX R-cheatsheet y genera un fichero PDF correspondiente.
# Si la plantilla LaTeX da error de compilación, pulsar intro varias veces.

print "Running ...\n============================\n"

# Invocar al terminal
import commands
from commands import *
import os
import subprocess

def process_command(cmd):
	subprocess.call(cmd, stdout=open(os.devnull, 'wb'), shell=True)

# R CHEATSHEET
##########################################

process_command(str("pdflatex " + "R-cheatsheet.tex")) # compila el fichero LaTeX a pdf

process_command(str("rm *.aux *.log *.synctex.gz")) # elimina ficheros aux, log y gz

print "\nR cheatsheet have been successfully generated!" #control
