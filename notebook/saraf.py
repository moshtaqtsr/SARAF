#!/usr/bin/env python3

import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def filter_by_length(input_file, output_file, min_length):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for record in SeqIO.parse(f_in, 'fasta'):
            if len(record.seq) >= min_length:
                SeqIO.write(record, f_out, 'fasta')
    print(f"Filtered contigs shorter than {min_length} bp saved to {output_file}")

def filter_by_coverage(input_file, output_file, min_coverage):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for record in SeqIO.parse(f_in, 'fasta'):
            # Extract coverage from header
            coverage = float(record.id.split('_')[-1].split('_')[0])
            if coverage >= min_coverage:
                SeqIO.write(record, f_out, 'fasta')
    print(f"Filtered contigs with coverage less than {min_coverage} saved to {output_file}")

def remove_contig(input_file, output_file, contig_name):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        removed = False
        for record in SeqIO.parse(f_in, 'fasta'):
            if record.id != contig_name:
                SeqIO.write(record, f_out, 'fasta')
            else:
                removed = True
        
        if removed:
            print(f"Removed contig '{contig_name}' from '{input_file}', saved to '{output_file}'")
        else:
            print(f"Contig '{contig_name}' not found in '{input_file}', output file unchanged")

def reverse_complement(input_file, output_file, contig_name=None):
    records = []
    with open(input_file, 'r') as f_in:
        for record in SeqIO.parse(f_in, 'fasta'):
            if contig_name is None or record.id == contig_name:
                reversed_seq = record.seq.reverse_complement()
                reversed_record = SeqRecord(reversed_seq, id=record.id, description=record.description)
                records.append(reversed_record)
            else:
                records.append(record)

    with open(output_file, 'w') as f_out:
        SeqIO.write(records, f_out, 'fasta')

    print(f"Reverse complement {'entire assembly' if contig_name is None else contig_name} saved to {output_file}")

def concatenate_contigs(input_file, output_file):
    contigs = []
    with open(input_file, 'r') as f_in:
        for record in SeqIO.parse(f_in, 'fasta'):
            contigs.append(record.seq)
    
    concatenated_seq = ''.join(str(seq) for seq in contigs)
    concatenated_record = SeqRecord(Seq(concatenated_seq), id="concatenated_contig", description="Concatenated contig")
    
    with open(output_file, 'w') as f_out:
        SeqIO.write(concatenated_record, f_out, 'fasta')
    
    print(f"All contigs concatenated into {output_file}")

def convert_to_uppercase(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for record in SeqIO.parse(f_in, 'fasta'):
            record.seq = record.seq.upper()
            SeqIO.write(record, f_out, 'fasta')
    print(f"Converted all sequences in {input_file} to uppercase and saved to {output_file}")

def convert_to_lowercase(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for record in SeqIO.parse(f_in, 'fasta'):
            record.seq = record.seq.lower()
            SeqIO.write(record, f_out, 'fasta')
    print(f"Converted all sequences in {input_file} to lowercase and saved to {output_file}")

def print_help():
    print("""
Usage: saraf <command> -i <input_file> -o <output_file> [additional_arguments]

Commands:
  -fl <min_length>
    Filter contigs by minimum length (Only for SPAdes assemblies).
  
  -fc <min_coverage>
    Filter contigs by minimum coverage (Only for SPAdes assemblies).
  
  -rm <contig_name>
    Remove a specific contig by name.
  
  -rc [contig_name]
    Reverse complement either the entire assembly or a specific contig.
  
  -concat
    Concatenate all contigs into a single contig.

  -u
    Convert all sequences to uppercase.

  -l
    Convert all sequences to lowercase.

  -h, --help
    Print this help message.
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command in ('-h', '--help'):
        print_help()
        sys.exit(0)
    
    if len(sys.argv) < 6 and command not in ('-u', '-l', '-concat'):
        print("Usage: saraf <command> -i <input_file> -o <output_file> [additional_arguments]")
        sys.exit(1)

    input_index = sys.argv.index('-i') if '-i' in sys.argv else sys.argv.index('--input')
    output_index = sys.argv.index('-o') if '-o' in sys.argv else sys.argv.index('--output')
    input_file = sys.argv[input_index + 1]
    output_file = sys.argv[output_index + 1]

    contig_name = None
    if command == '-rm':
        if '-c' not in sys.argv:
            print("Usage: saraf -rm -c <contig_name>")
            sys.exit(1)
        contig_index = sys.argv.index('-c')
        contig_name = sys.argv[contig_index + 1]

    if command == '-rc':
        if len(sys.argv) > 2 and '-c' in sys.argv:
            contig_index = sys.argv.index('-c')
            contig_name = sys.argv[contig_index + 1]

    if command == '-fl':
        if len(sys.argv) < 4:
            print("Usage: saraf -fl <min_length>")
            sys.exit(1)
        min_length = int(sys.argv[2])
        filter_by_length(input_file, output_file, min_length)
    
    elif command == '-fc':
        if len(sys.argv) < 4:
            print("Usage: saraf -fc <min_coverage>")
            sys.exit(1)
        min_coverage = float(sys.argv[2])
        filter_by_coverage(input_file, output_file, min_coverage)
    
    elif command == '-rm':
        remove_contig(input_file, output_file, contig_name)
    
    elif command == '-rc':
        reverse_complement(input_file, output_file, contig_name)
    
    elif command == '-concat':
        concatenate_contigs(input_file, output_file)
    
    elif command == '-u':
        convert_to_uppercase(input_file, output_file)
    
    elif command == '-l':
        convert_to_lowercase(input_file, output_file)
    
    else:
        print(f"Unknown command: {command}")
        print_help()
        sys.exit(1)
