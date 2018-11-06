import argparse
# import sys
from Bio import SeqIO, pairwise2
__author__ = 'taeyoon kim'

parser = argparse.ArgumentParser(description='python script for basic sequencing results')
parser.add_argument('-d', '--DNA', help='Fasta file of template DNA', type=str, required=True)
parser.add_argument('-i', '--input', help='Input file', required=True)
parser.add_argument('-o', '--output', help='Output file', required=True)
args = parser.parse_args()

def main():
    '''
    python script for basic sequencing results
    '''
    # Read template DNA
    template_ = SeqIO.read(args.DNA,'fasta')
    template_protein = template_.seq.translate()
    # simple file write
    with open(args.output,'w') as f:
        f.write('#### Life is short, use python. \n')
        # Simple FASTA parsing
        for seq_record in SeqIO.parse(args.input, "fasta"):
            print('#### DNA alignments of {} ####'.format(seq_record.id))
            f.write('#### DNA alignments of {} ####\n'.format(seq_record.id))
            alignments = pairwise2.align.localms(seq_record.seq, template_.seq, 2, -3, -2, -2)
            print(pairwise2.format_alignment(*alignments[0]))
            f.write(pairwise2.format_alignment(*alignments[0]))
            f.write('\n') # add blank line
            print('#### Protein alignments of {} ####'.format(seq_record.id))
            f.write('#### Protein alignments of {} ####\n'.format(seq_record.id))
            # f.write('\n') # add blank line
            # stop codon = *, all frame shift
            forward_1 = seq_record.seq[0::].translate()
            forward_2 = seq_record.seq[1::].translate()
            forward_3 = seq_record.seq[2::].translate()
            reverse_1 = seq_record.seq[:0:-1].translate() # reverse frame
            reverse_2 = seq_record.seq[:1:-1].translate()
            reverse_3 = seq_record.seq[:2:-1].translate()
            # make list for loop
            
            protein_seq = [forward_1, forward_2, forward_3, reverse_1, reverse_2, reverse_3]
            # alginments
            for i in protein_seq:
                # print frame name?
                alignments = pairwise2.align.localms(i, template_protein, 2, -3, -2, -2)
                print(pairwise2.format_alignment(*alignments[0])) # print 1st alignments
                f.write(pairwise2.format_alignment(*alignments[0]))
            f.write('\n') # add blank line

if __name__ == "__main__":
    main()