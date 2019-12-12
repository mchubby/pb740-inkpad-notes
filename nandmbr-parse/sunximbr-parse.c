#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

#include "nand-part-a20.h"

static void printmbrheader(MBR *mbr)
{
	printf("mbr: version 0x%08x, magic %8.8s\n", mbr->version, mbr->magic);
}

static void printmbr(MBR *mbr)
{
	unsigned int part_cnt;
	
	printmbrheader(mbr);
	printf("%d partitions\n", mbr->PartCount);
	for(part_cnt = 0; part_cnt < mbr->PartCount && part_cnt < MAX_PART_COUNT; part_cnt++)
	{
		printf("partition %2d: class = %12s, name = %12s, partition start = %8d, partition size = %8d user_type=%d\n",
					part_cnt + 1,
					mbr->array[part_cnt].classname,
					mbr->array[part_cnt].name,
					mbr->array[part_cnt].addrlo,
					mbr->array[part_cnt].lenlo,
					mbr->array[part_cnt].user_type);
	}
}

#define DEFAULTFILE "SUNXIMBR.bin"

int main(int argc, char**argv)
{
	char buf[MBR_SIZE];
	MBR *mbr = (MBR *)buf;
	const char *input = argc > 1 ? argv[1] : DEFAULTFILE;

	printf("%s\n", input);
	int fd = open(input, O_RDONLY);
	int rdin;
	if((rdin = read(fd,buf,MBR_SIZE)) != MBR_SIZE)
	{
		printf("file: not enough data (%d vs %d) in %s!\n", rdin, MBR_SIZE, input);
		return 1;
	}
	printf("check partition table\n");
	if(strncmp((char *)mbr->magic, MBR_MAGIC, 8))
	{
		printf("magic %8.8s is not %8s\n", mbr->magic, MBR_MAGIC);
		return 1;
	}
	if(mbr->version != MBR_VERSION)
	{
		printf("version 0x%08x is not 0x%08x\n", mbr->version, MBR_VERSION);
		return 1;
	}
/*
	if(*(__u32 *)mbr != calc_crc32((__u32 *)&mymbr + 1,MBR_SIZE - 4))
	{
		printf("BAD CRC!\n");
		return 1;
	}
*/
	printmbr(mbr);

	return 0;
}
