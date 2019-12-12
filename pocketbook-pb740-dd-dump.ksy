meta:
  id: pocketbook_pb740_dd_dump
  title: PocketBook device dump layout for Inkpad 3 (740)
  encoding: ASCII
  endian: le

doc: >
    Layout of the PocketBook device, to allow easier splitting.
    Dump emmc to ext. SD card (other devices without a slot may try to dump to an sshfs mountpoint)
    # dd bs=1M if=/dev/mmcblk0 | gzip -c | split -b 4095m - /mnt/ext2/backup/mmcblk0--dd.gz. &
    # watch -n5 'kill -USR1 $(pgrep ^dd)'
    You may disable the gzip command if destination supports >4GB files (needs 7 818 182 656; beyond FAT32-max)
    because the CPU is a reeeeal slug.

seq:
  - id: mmc_unmapped_data
    -orig-id: unmapped_data
    size: 36 * 1024 * 1024
    type: sunxiemmc
  - id: mmc_mmcblk0p2
    -orig-id: mmcblk0p2
    type: mmcblk0p2
    doc: /boot in FAT16
  - id: mmc_mmcblk0p3
    -orig-id: mmcblk0p3
    type: mmcblk0p3
    doc: |
      extended [protective?] partition, 754MB
  - id: mmc_mmcblk0p1
    -orig-id: mmcblk0p1
    type: mmcblk0p1
    doc: /mnt/ext1 in FAT32

types:
  sunxiemmc:
    seq:
      - id: mmc_0000_0000
        size: 384 * 512
        doc: |
          (UNKNOWN) @ofs 0 LEN=196608
      - id: mmc_0003_0000_boot0_emmc3_egon0_1
        size: 32 * 1024
        doc: egon.bt0 image at sector 384
      - id: mmc_0003_8000
        size: 32 * 1024
        doc: |
          (Possible PADDING) @ofs 229376 LEN=32768
      - id: mmc_0004_0000_boot0_emmc3_backup_egon0_2
        size: 32 * 1024
        doc: egon.bt0 image at sector 512
      - id: mmc_0004_8000
        size: 32 * 1024
        doc: |
          (Possible PADDING) @ofs 294912 LEN=32768
      - id: mmc_0005_0000
        size: 23936 * 512
        doc: |
          (UNKNOWN) @ofs 327680 LEN=12255232
      - id: mmc_00c0_0000_uboot_backup_pkg_padded
        size: 4080 * 1024
        doc: |
          uboot (stage 1) image at sector 24576
      - id: mmc_00ff_c000
        size: 32 * 1024
        doc: |
          (Possible PADDING) @ofs 16760832 LEN=32768
      - id: mmc_0100_4000_uboot_pkg_padded
        size: 4080 * 1024
        doc: uboot (stage 1) image at sector 32800
      - id: mmc_0140_0000_pt
        type: sunxiemmc_partitiontables
      - id: mmc_0141_0000
        size: 16320 * 1024
        doc: |
          (Possible PADDING) @ofs 21037056 LEN=16711680
  sunxiemmc_partitiontables:
    seq:
      - id: mmc_0140_0000_pt1
        size: 16 * 1024
        doc: sunxi 'nand-part-a20' partition table (softw411 magic)
      - id: mmc_0140_4000_pt2
        size: 16 * 1024
        doc: sunxi 'nand-part-a20' partition table (softw411 magic)
      - id: mmc_0140_8000_pt3
        size: 16 * 1024
        doc: sunxi 'nand-part-a20' partition table (softw411 magic)
      - id: mmc_0140_c000_pt4
        size: 16 * 1024
        doc: sunxi 'nand-part-a20' partition table (softw411 magic)
  mmcblk0p2:
    seq:
      - id: mmc_0240_0000_partn_boot_fat16
        size: 32 * 1024 * 1024
        doc: The /boot (ro) partition
  mmcblk0p3:
    seq:
      - id: mmc_0440_0000_partn_env_raw
        -orig-id: mmcblk0p5
        size: 16 * 1024 * 1024
        doc: may contain temporary reboot data such as an ANDROID! bootimage (abootimg) for recovery
      - id: mmc_0540_0000_partn_pbenv_raw
        -orig-id: mmcblk0p6
        size: 34 * 1024 * 1024
        doc: may contain temporary reboot data such as an ANDROID! bootimage (abootimg) for recovery
      - id: mmc_0760_0000_partn_root_ext2
        -orig-id: mmcblk0p7
        size: 64 * 1024 * 1024
        doc: The / partition
      - id: mmc_0b60_0000_partn_ebrmain_ext2
        -orig-id: mmcblk0p8
        size: 512 * 1024 * 1024
        doc: The /ebrmain (ro) partition, which itself has a cramfs.img file later mounted on /ebrmain/cramfs
      - id: mmc_2b60_0000_partn_mntsecure_ext2
        -orig-id: mmcblk0p9
        size: 128 * 1024 * 1024
        doc: The /mnt/secure partition
  mmcblk0p1:
    seq:
      - id: mmc_3360_0000_partn_udisk_fat32
        size: 1
        doc: The /mnt/ext1 partition. (Stub size to prevent reading all the way to eos.)
