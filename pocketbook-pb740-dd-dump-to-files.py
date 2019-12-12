#!/usr/bin/env python
"""A splitter script leveraging the kaitai-struct parser framework.

* Create the needed files with the java program:

    $ kaitai-struct-compiler -t python pocketbook-pb740-dd-dump.ksy

* Use the generated directory as a pseudo package:

    $ `echo 'from .pocketbook_pb740_dd_dump import PocketbookPb740DdDump' > python/__init__.py

"""


import argparse
from kaitaistruct import KaitaiStruct

# import from subdirectory
from python import PocketbookPb740DdDump


EXTENT_SIZE = 1024 * 1024


def dump(fname: str):
    """Process input `fname` through the generated PocketbookPb740DdDump kaitai-struct parser and writes results to files.

    Args:
        fname: path of device dump file, made with dd or similar
    """
    # Instanciate the KaitaiStruct-derived object
    ksyparsing = PocketbookPb740DdDump.from_file(fname)
    dump_attributes_to_file(0, ksyparsing)


def dump_attributes_to_file(level: int, ksobj: KaitaiStruct):
    """Recursively process KS attribute fields and Writes matching properties to individual files.

    Args:
        level: number expressing how deep in the file structures we are
        ksobj: a PocketbookPb740DdDump (KaitaiStruct-derived) object
    """
    for subattr in dir(ksobj):
        # handle special tail case
        if subattr.startswith('mmc_3360_0000'):
            print(level * ' ' + "- {}".format(subattr))
            ksobj._io.seek(0x33600000)
            to_read = ksobj._io.size() - ksobj._io.pos()
            with open(subattr, "wb") as out_file:
                while to_read > 0:
                    intended_count = min(EXTENT_SIZE, to_read)
                    # raises EOFError if cannot read enough for some reason
                    out_file.write(ksobj._io.read_bytes(intended_count))
                    to_read = to_read - intended_count
        elif subattr.startswith('mmc_'):
            # recurse and increase depth/level
            if isinstance(getattr(ksobj, subattr), KaitaiStruct):
                print(level * ' ' + "{}".format(subattr))
                dump_attributes_to_file(level + 1, getattr(ksobj, subattr))
            else:
                print(level * ' ' + "- {}".format(subattr))
                with open(subattr, "wb") as out_file:
                    out_file.write(getattr(ksobj, subattr))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Split a dd dump file from a PocketBook 740 Inkpad 3 device EMMC dump")
    parser.add_argument("inputfile", help="the dd input dump file")

    args = parser.parse_args()

    dump(args.inputfile)
