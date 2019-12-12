# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class PocketbookPb740DdDump(KaitaiStruct):
    """Layout of the PocketBook device, to allow easier splitting. Dump emmc to ext. SD card (other devices without a slot may try to dump to an sshfs mountpoint) # dd bs=1M if=/dev/mmcblk0 | gzip -c | split -b 4095m - /mnt/ext2/backup/mmcblk0--dd.gz. & # watch -n5 'kill -USR1 $(pgrep ^dd)' You may disable the gzip command if destination supports >4GB files (needs 7 818 182 656; beyond FAT32-max) because the CPU is a reeeeal slug.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_mmc_unmapped_data = self._io.read_bytes(((36 * 1024) * 1024))
        io = KaitaiStream(BytesIO(self._raw_mmc_unmapped_data))
        self.mmc_unmapped_data = self._root.Sunxiemmc(io, self, self._root)
        self.mmc_mmcblk0p2 = self._root.Mmcblk0p2(self._io, self, self._root)
        self.mmc_mmcblk0p3 = self._root.Mmcblk0p3(self._io, self, self._root)
        self.mmc_mmcblk0p1 = self._root.Mmcblk0p1(self._io, self, self._root)

    class Sunxiemmc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mmc_0000_0000 = self._io.read_bytes((384 * 512))
            self.mmc_0003_0000_boot0_emmc3_egon0_1 = self._io.read_bytes((32 * 1024))
            self.mmc_0003_8000 = self._io.read_bytes((32 * 1024))
            self.mmc_0004_0000_boot0_emmc3_backup_egon0_2 = self._io.read_bytes((32 * 1024))
            self.mmc_0004_8000 = self._io.read_bytes((32 * 1024))
            self.mmc_0005_0000 = self._io.read_bytes((23936 * 512))
            self.mmc_00c0_0000_uboot_backup_pkg_padded = self._io.read_bytes((4080 * 1024))
            self.mmc_00ff_c000 = self._io.read_bytes((32 * 1024))
            self.mmc_0100_4000_uboot_pkg_padded = self._io.read_bytes((4080 * 1024))
            self.mmc_0140_0000_pt = self._root.SunxiemmcPartitiontables(self._io, self, self._root)
            self.mmc_0141_0000 = self._io.read_bytes((16320 * 1024))


    class Mmcblk0p3(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mmc_0440_0000_partn_env_raw = self._io.read_bytes(((16 * 1024) * 1024))
            self.mmc_0540_0000_partn_pbenv_raw = self._io.read_bytes(((34 * 1024) * 1024))
            self.mmc_0760_0000_partn_root_ext2 = self._io.read_bytes(((64 * 1024) * 1024))
            self.mmc_0b60_0000_partn_ebrmain_ext2 = self._io.read_bytes(((512 * 1024) * 1024))
            self.mmc_2b60_0000_partn_mntsecure_ext2 = self._io.read_bytes(((128 * 1024) * 1024))


    class Mmcblk0p2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mmc_0240_0000_partn_boot_fat16 = self._io.read_bytes(((32 * 1024) * 1024))


    class SunxiemmcPartitiontables(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mmc_0140_0000_pt1 = self._io.read_bytes((16 * 1024))
            self.mmc_0140_4000_pt2 = self._io.read_bytes((16 * 1024))
            self.mmc_0140_8000_pt3 = self._io.read_bytes((16 * 1024))
            self.mmc_0140_c000_pt4 = self._io.read_bytes((16 * 1024))


    class Mmcblk0p1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mmc_3360_0000_partn_udisk_fat32 = self._io.read_bytes(1)



