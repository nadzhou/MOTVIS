from Bio.Emboss.Applications import WaterCommandline
import subprocess


def emboss_water(seq_a_file: str, seq_b_file: str, out_file: str):
    """ Do a global pairwise alignment using EMBOSS

        Args: 
            seq_a_file: First sequence
            seq_b_file: second sequence
            out_file: Output file

        Returns: 
            r [subprocess object]: Execute the commandline command for EMBOSS
        
    """
    water_cline = WaterCommandline(asequence=seq_a_file,
                                        bsequence=seq_b_file,
                                        outfile=out_file,
                                        verbose=True,
                                        gapextend=1,
                                        gapopen=10)

    cmd = str(water_cline)
    cmd = cmd.split(" ")
    cmd.append("-aformat=msf")

    return subprocess.run(cmd, check=True)


def main():
    seq_a = "/home/nadzhou/SEQs/tb/dummy_1.fasta"
    seq_b = "/home/nadzhou/SEQs/tb/dummy_2.fasta"
    out_file = "/home/nadzhou/SEQs/tb/dummy_needle.fasta"

    emboss_water(seq_a, seq_b, out_file)


if __name__ == '__main__':
    main()
