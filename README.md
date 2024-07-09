SARAF: Sequence Assembly Refining and Filtering
Overview
SARAF is a versatile tool designed for processing and refining genome assemblies in FASTA format. It provides several options for filtering, manipulating, and transforming contigs based on specified criteria.

Dependencies
Python 3
Biopython library (Bio.Seq, Bio.SeqIO, Bio.SeqRecord)
Usage
The script accepts a command followed by input and output file options and additional arguments based on the command. The general usage pattern is:

bash
Copy code
saraf <command> -i <input_file> -o <output_file> [additional_arguments]
## Authors

- [@moshtaqtsr](https://github.com/moshtaqtsr)


## License

[MIT](https://choosealicense.com/licenses/mit/)

Commands and Options
Filter by Minimum Length (-fl <min_length>)

Filters contigs by a specified minimum length.
Usage:
bash
Copy code
saraf -fl <min_length> -i <input_file> -o <output_file>
Example:
bash
Copy code
saraf -fl 500 -i contigs.fasta -o filtered_by_length.fasta
Filter by Minimum Coverage (-fc <min_coverage>)

Filters contigs by a specified minimum coverage.
Usage:
bash
Copy code
saraf -fc <min_coverage> -i <input_file> -o <output_file>
Example:
bash
Copy code
saraf -fc 10.0 -i contigs.fasta -o filtered_by_coverage.fasta
Remove a Specific Contig (-rm -c <contig_name>)

Removes a specific contig by name, including its header and sequence.
Usage:
bash
Copy code
saraf -rm -i <input_file> -o <output_file> -c <contig_name>
Example:
bash
Copy code
saraf -rm -i contigs.fasta -o contigs_without_node_1.fasta -c NODE_1
Reverse Complement (-rc [-c <contig_name>])

Generates the reverse complement of the entire assembly or a specific contig.
Usage:
bash
Copy code
saraf -rc -i <input_file> -o <output_file> [-c <contig_name>]
Example (entire assembly):
bash
Copy code
saraf -rc -i contigs.fasta -o reverse_complemented.fasta
Example (specific contig):
bash
Copy code
saraf -rc -i contigs.fasta -o reverse_complemented_node_1.fasta -c NODE_1
Concatenate Contigs (-concat)

Concatenates all contigs into a single contig, using the input file name as the header.
Usage:
bash
Copy code
saraf -concat -i <input_file> -o <output_file>
Example:
bash
Copy code
saraf -concat -i contigs.fasta -o concatenated_contigs.fasta
Convert Sequences to Uppercase (-u)

Converts all sequences to uppercase.
Usage:
bash
Copy code
saraf -u -i <input_file> -o <output_file>
Example:
bash
Copy code
saraf -u -i contigs.fasta -o uppercase_contigs.fasta
Convert Sequences to Lowercase (-l)

Converts all sequences to lowercase.
Usage:
bash
Copy code
saraf -l -i <input_file> -o <output_file>
Example:
bash
Copy code
saraf -l -i contigs.fasta -o lowercase_contigs.fasta
Help (-h or --help)

Displays the help message with usage instructions.
Usage:
bash
Copy code
saraf -h
