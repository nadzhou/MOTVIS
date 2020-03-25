#!/usr/bin/env python3.7

from Bio.Blast.Applications import NcbipsiblastCommandline
import subprocess

def psi_blaster(in_file):
    """Perform a PSI-BLAST via the refseq-protein.00
    database available locally and then get XML output. 
    
    Args: 
        in_file [str]: Path to the input file for BLAST search. 
        
    Returns: 
        out_psi.xml [file]: Tell the user operation is done 
    
    """
    
    in_file = str(in_file)
    print("Initiating PSI-BLAST...")

    cline = NcbipsiblastCommandline(query = in_file, outfmt = 5, 
                                db = "refseq_protein.00", 
                                out="/home/nadzhou/Desktop/out_psi.xml")

    cmd = str(cline)
    cmd = cmd.split(" ")
    cmd = list(cmd)
    r = subprocess.Popen(cmd)
    
    if r.communicate(): 
        return ("PSI-BLAST done. File written out_psi.xml")
        
