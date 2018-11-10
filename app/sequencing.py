from Bio import SeqIO, pairwise2

def FunctionName(args):
    template_ = SeqIO.read(args.DNA,'fasta')
    template_protein = template_.seq.translate()
    pass