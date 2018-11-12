from Bio import SeqIO, pairwise2
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord


def read_fasta(fp):
    name, seq = None, []
    for line in fp.split():
        # line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line[1:], []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))


def mk_seqrecord(x):
    result = []
    for name, seq in x:
        result.append(SeqRecord(Seq(seq), id=name))
    return result


# with open('f.fasta') as fp:
#     for name, seq in read_fasta(fp):
#         print(name, seq)

def Alignment(target_seq, query_seq):
    '''
    Read template Fasta file: should be ATG to TAG
    '''
    name, seq = None, []
    for line in target_seq.split():
        if line.startswith(">"):
            name, seq = line[1:], []
        else:
            seq.append(line)
    
    target_DNA = SeqRecord(Seq(''.join(seq)), id = name)
    target_Protein = target_DNA.translate()

    # empty dict
    DNA_result = {}
    PRO_result = {}
    result = []
   # simple file write
    with open('static/alignment_result.txt','w') as f:
        f.write('#### Life is short, use python. \n')
        f.write('\n') # add blank line
        # Simple FASTA parsing
        for seq_record in mk_seqrecord(read_fasta(query_seq)):
            # print('#### DNA alignments of {} ####'.format(seq_record.id))
            f.write('#### DNA sequence alignments : {} ####\n'.format(seq_record.id))
            alignments = pairwise2.align.localms(seq_record.seq, target_DNA.seq, 2, -3, -2, -2)
            # print(pairwise2.format_alignment(*alignments[0]))
            f.write(pairwise2.format_alignment(*alignments[0]))
            f.write('\n') # add blank line
            # print('#### Protein alignments of {} ####'.format(seq_record.id))
            f.write('#### Protein sequence alignments :  {} ####\n'.format(seq_record.id))
            f.write('\n') # add blank line
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
                pro_alignments = pairwise2.align.localms(i, target_Protein.seq, 2, -3, -2, -2)
                # print pairwise2.format_alignment(*pro_alignments[0])  # print 1st alignments
                f.write(pairwise2.format_alignment(*pro_alignments[0]))
            f.write('\n') # add blank line

    # DNA alginment
    # for seq_record in mk_seqrecord(read_fasta(query_seq)):
    #     alignments = pairwise2.align.localms(seq_record.seq, target_DNA.seq, 2, -3, -2, -2)
    #     DNA_result[seq_record.id] = pairwise2.format_alignment(*alignments[0])
    #     # Protein seq
    #     forward_1 = seq_record.seq[0::].translate()
    #     forward_2 = seq_record.seq[1::].translate()
    #     forward_3 = seq_record.seq[2::].translate()
    #     reverse_1 = seq_record.seq[:0:-1].translate() # reverse frame
    #     reverse_2 = seq_record.seq[:1:-1].translate()
    #     reverse_3 = seq_record.seq[:2:-1].translate()
    #     # make list for loop
            
    #     protein_seq = [forward_1, forward_2, forward_3, reverse_1, reverse_2, reverse_3]
    #     # # Prtoein sequence alginments
    #     for i in protein_seq:
    #     #     # print frame name?
    #         # alignments = pairwise2.align.localms(i, target_Protein, 2, -3, -2, -2)
    #     #     PRO_result[seq_record.id + '_' + i] = pairwise2.format_alignment(*alignments[0])
    # result.append(DNA_result)
    # return result


