## SARAF: Sequence Assembly Refining and Filtering
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


#### Usage
The script accepts a command followed by input and output file options and additional arguments based on the command. The general usage pattern is:

```bash
saraf <command> -i <input_file> -o <output_file> [additional_arguments]
```

#### Commands and Options

1. **Filter by Minimum Length (`-fl <min_length>`)**
   - Filters contigs by a specified minimum length.
   - **Usage:**
     ```bash
     saraf -fl <min_length> -i <input_file> -o <output_file>
     ```
   - Example:
     ```bash
     saraf -fl 500 -i contigs.fasta -o filtered_by_length.fasta
     ```

2. **Filter by Minimum Coverage (`-fc <min_coverage>`)**
   - Filters contigs by a specified minimum coverage.
   - **Usage:**
     ```bash
     saraf -fc <min_coverage> -i <input_file> -o <output_file>
     ```
   - Example:
     ```bash
     saraf -fc 10.0 -i contigs.fasta -o filtered_by_coverage.fasta
     ```

3. **Remove a Specific Contig (`-rm -c <contig_name>`)**
   - Removes a specific contig by name, including its header and sequence.
   - **Usage:**
     ```bash
     saraf -rm -i <input_file> -o <output_file> -c <contig_name>
     ```
   - Example:
     ```bash
     saraf -rm -i contigs.fasta -o contigs_without_node_1.fasta -c NODE_1
     ```

4. **Reverse Complement (`-rc [-c <contig_name>]`)**
   - Generates the reverse complement of the entire assembly or a specific contig.
   - **Usage:**
     ```bash
     saraf -rc -i <input_file> -o <output_file> [-c <contig_name>]
     ```
   - Example (entire assembly):
     ```bash
     saraf -rc -i contigs.fasta -o reverse_complemented.fasta
     ```
   - Example (specific contig):
     ```bash
     saraf -rc -i contigs.fasta -o reverse_complemented_node_1.fasta -c NODE_1
     ```

5. **Concatenate Contigs (`-concat`)**
   - Concatenates all contigs into a single contig, using the input file name as the header.
   - **Usage:**
     ```bash
     saraf -concat -i <input_file> -o <output_file>
     ```
   - Example:
     ```bash
     saraf -concat -i contigs.fasta -o concatenated_contigs.fasta
     ```

6. **Convert Sequences to Uppercase (`-u`)**
   - Converts all sequences to uppercase.
   - **Usage:**
     ```bash
     saraf -u -i <input_file> -o <output_file>
     ```
   - Example:
     ```bash
     saraf -u -i contigs.fasta -o uppercase_contigs.fasta
     ```

7. **Convert Sequences to Lowercase (`-l`)**
   - Converts all sequences to lowercase.
   - **Usage:**
     ```bash
     saraf -l -i <input_file> -o <output_file>
     ```
   - Example:
     ```bash
     saraf -l -i contigs.fasta -o lowercase_contigs.fasta
     ```

8. **Help (`-h` or `--help`)**
   - Displays the help message with usage instructions.
   - **Usage:**
     ```bash
     saraf -h
     ```

### SARAF Installation Instructions

You can easily install SARAF using the provided installation script. Follow the steps below:

1. **Download the installation script using `wget`:**

   Open a terminal and run the following command to download the `install_saraf.sh` script from the SARAF GitHub repository:

   ```sh
   wget wget https://raw.githubusercontent.com/moshtaqtsr/SARAF/main/notebook/install_saraf.sh
   ```

2. **Make the script executable:**

   After downloading the script, you need to make it executable by running:

   ```sh
   chmod +x install_saraf.sh
   ```

3. **Run the installation script:**

   Finally, execute the script to install SARAF:

   ```sh
   ./install_saraf.sh
   ```

These commands will download the `install_saraf.sh` script, give it execution permissions, and run it to complete the installation of SARAF.

