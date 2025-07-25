

How to Use the IMRF-to-SR3 Converter
------------------------------------

Usage:  imrf2sr3.exe -r input (-o output) (-chain)

   input:   pathname to input IRF;  ".irf" is optional.  It is
            assumed that the MRF is in same directory as the IRF
            and has the same basename as the IRF.

   output:  pathname to generated SR3;  ".sr3" is optional.
            "-o output" is optional;  if it is absent, then the
            generated SR3 file appears in the same directory as
            the input IRF.

   -chain:  convert entire restart chain into one SR3 file,
            where "input" is the bottom of the restart chain.
            The IRF at the top of the chain has no PARENT record.
            The parent of each IRF/MRF file set must be accessible
            by the path in its PARENT record.
