def to_rna(dna_strand):
    """Maps a DNA strange to it's corresponding RNA strand.

    dna_strand - The strand you want to convert to an RNA strand.
    """
    nucleotide_mapping = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    output = []
    for nuc in dna_strand:
        try:
            output.append(nucleotide_mapping[nuc])
        except ValueError:
            raise Exception(
                "Provided nucleotide identifier is not one of G, C, T, or A.")
    return "".join(output)
