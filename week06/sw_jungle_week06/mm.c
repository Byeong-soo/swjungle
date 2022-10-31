/*
 * 
 * In this naive approach, a block is allocated by simply incrementing
 * the brk pointer.  A block is pure payload. There are no headers or
 * mm-naive.c - The fastest, least memory-efficient malloc package.
 * footers.  Blocks are never coalesced or reused. Realloc is
 * implemented directly using mm_malloc and mm_free.
 *
 * NOTE TO STUDENTS: Replace this header comment with your own header
 * comment that gives a high level description of your solution.
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

#include "mm.h"
#include "memlib.h"

/*********************************************************
 * NOTE TO STUDENTS: Before you do anything else, please
 * provide your team information in the following struct.
 ********************************************************/
team_t team = {
    /* Team name */
    "week06_6",
    /* First member's full name */
    "Yu Byeong Soo",
    /* First member's email address */
    "ubs4939@naver.com",
    /* Second member's full name (leave blank if none) */
    "",
    /* Second member's email address (leave blank if none) */
    ""
};

/*  Basic constants and macros */
#define WSIZE 4 /* Wdrd and header /footer size(bytes)*/
#define DSIZE 8 /* Double word size (byte)*/
#define CHUNKSIZE (1<<12) /* Extend heap by this amount (bytes) */

#define MAX(x,y) ((x) > (y)? (x) : (y))

/* Pack a size and allocated bit into a word */
#define PACK(size, alloc)   ((size) | (alloc))

/* Read and write a word at address p */
#define GET(p) (*(unsigned int *)(p))
#define PUT(p, val) (*(unsigned int *)(p) = (val))

/*  Read the size and allocated fields from address p   */
#define GET_SIZE(p)  (GET(p) & ~0x7)
#define GET_ALLOC(p) (GET(p) & 0x1)

/*  Given block ptr bp, computer address of its header and footer   */
#define HDRP(bp) ((char *)(bp) - WSIZE)
#define FTRP(bp) ((char *)(bp) + GET_SIZE(HDRP(bp)) - DSIZE)

/*  Given block ptr bp, compute address of next and previous blocks */
#define NEXT_BLKP(bp) ((char *)(bp) + GET_SIZE(((char *)(bp) - WSIZE)))
#define PREV_BLKP(bp) ((char *)(bp) - GET_SIZE(((char *)(bp) - DSIZE)))

#define EXPLICIT


/* single word (4) or double word (8) alignment */
#define ALIGNMENT 8

/* rounds up to the nearest multiple of ALIGNMENT */
#define ALIGN(size) (((size) + (ALIGNMENT-1)) & ~0x7)
#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))

#ifdef EXPLICIT
static void * explicit_listp = 0;
static void put_explicit_list(void * ptr);
static void del_explicit_list(void * ptr);
#endif

static char * heap_listp;
static void * extend_heap(size_t size);
static void * coaleasce(void * ptr);
static void * find_fit(size_t size);
// static void * find_fit_next(size_t size);
static void place(void * ptr, size_t size);
/* 
 * mm_init - initialize the malloc package.
 */

int mm_init(void)
{
    /* Create the initial empty heap */
    if ((heap_listp = mem_sbrk(4*WSIZE)) == (void *) -1){
        return -1;
    }
    
    PUT(heap_listp, 0);                             /*  Alignment padding   */
    PUT(heap_listp + (1*WSIZE), PACK(DSIZE, 1));    /*  Prologue header   */
    PUT(heap_listp + (2*WSIZE), PACK(DSIZE, 1));    /*  Prologue footer   */
    PUT(heap_listp + (3*WSIZE), PACK(0, 1));        /*  Epilogue header    */
    heap_listp += (2*WSIZE);

    /* Extend the empty heap with a free block of CHUNKSIZE bytes */
    if (extend_heap(CHUNKSIZE / WSIZE) == NULL){
        return -1;
    }
    return 0;
}

static void *extend_heap(size_t words){
    char *bp;
    size_t size;
    /*  Allocate an even number of words to maintain aligmnet */

    size = (words % 2) ? (words+1) * WSIZE : words * WSIZE;
    if ((long)(bp = mem_sbrk(size)) == -1){
        return NULL;
    }
    
    /*  Initialize free block header/footer and the epilogue header */
    PUT(HDRP(bp), PACK(size,0));            /*  Free block header   */
    PUT(FTRP(bp), PACK(size,0));            /*  Free block footer   */
    PUT(HDRP(NEXT_BLKP(bp)),PACK(0,1));     /*  New epliogue header */

    /*  Coalesce if the previous block was free */
    // printf("extend_hep 에서 coaleasce 들어감\n");
    return coaleasce(bp);

}


/* 
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    // int newsize = ALIGN(size + SIZE_T_SIZE);
    // void *p = mem_sbrk(newsize);
    // if (p == (void *)-1)
	// return NULL;
    // else {
    //     *(size_t *)p = size;
    //     return (void *)((char *)p + SIZE_T_SIZE);
    // }

    size_t asize;   /* Adjusted block size  */
    size_t extendsize; /*   Amount to extend heap if no fit */
    char *ptr;

    /*  Ignore spurious requests    */
    if(size == 0){
        return NULL;
    }
        
    /*  Adjust block size to include overhead and alignment reqs    */
    if (size<= DSIZE)
    {
        asize = 2*DSIZE;
    }
    else
    {
        asize = DSIZE * ((size + (DSIZE) + (DSIZE -1)) / DSIZE);
    }



    /* Search the free list for a fit   */
    if((ptr = find_fit(asize)) != NULL){
        place(ptr,asize);
        return ptr; 
    }

    /* No fit found, Get more memory and place the block */
    extendsize = MAX(asize,CHUNKSIZE);
    if((ptr = extend_heap(extendsize/WSIZE)) == NULL){
         return NULL;
    }
    place(ptr,asize);
    return ptr;
}

/*
 * mm_free - Freeing a block does nothing.
 */
void mm_free(void *ptr)
{
    size_t size = GET_SIZE(HDRP(ptr));
    PUT(HDRP(ptr), PACK(size,0));
    PUT(FTRP(ptr), PACK(size,0));
        // printf("mm_free 에서 coaleasce 들어감\n");
    coaleasce(ptr);
}

#ifdef EXPLICIT
static void put_explicit_list(void * ptr){
    if (explicit_listp == 0)
    {
        explicit_listp = ptr;
        PUT(ptr, 0);
        PUT(ptr + WSIZE, 0);
    
    //    printf("===========처음이 0 임===============\n");
    //         printf("ptr = %p \n",ptr);
    //         printf("ptr prev= %p \n",GET(ptr));
    //         printf("ptr next= %p \n",GET(ptr+ WSIZE));
    //         if(GET(ptr+ WSIZE) != 0){
    //             printf("ptr next 의 prev = %p \n", GET(GET(ptr+ WSIZE)));
    //             printf("ptr next 의 next = %p \n", GET(GET(ptr+ WSIZE)+WSIZE));
    //         }
    //         printf("==================================\n");
    }else
    {
        // 0이 아님. 가용 리스트가 있음.
        // 첫 부분의 연결지점을 새로운 포인터로 함
        PUT(explicit_listp, ptr);
        PUT(ptr + WSIZE, explicit_listp);
        PUT(ptr, 0);
        explicit_listp = ptr;


            //    printf("=============여러개================\n");
            // printf("ptr = %p \n",ptr);
            // printf("ptr prev= %p \n",GET(ptr));
            // printf("ptr next= %p \n",GET(ptr+ WSIZE));
            // if(GET(ptr+ WSIZE) != 0){
            //     printf("ptr next 의 prev = %p \n", GET(GET(ptr+ WSIZE)));
            //     printf("ptr next 의 next = %p \n", GET(GET(ptr+ WSIZE)+WSIZE));
            // }
            // printf("==================================\n");
    }

    

}


static void del_explicit_list(void * delete_ptr){
    // printf("delete 들어옴\n");
    char * deletePtr =delete_ptr;
    char * prePtr;
    char * nextPtr;
    char * cur = explicit_listp;

     while (cur != 0)
        {
            // printf("==================================\n");
            // printf("cur = %p \n",cur);
            // printf("cur prev= %p \n",GET(cur));
            // printf("cur next= %p \n",GET(cur+ WSIZE));
            // if(GET(cur+ WSIZE) != 0){
            //     printf("cur next 의 prev = %p \n", GET(GET(cur+ WSIZE)));
            //     printf("cur next 의 next = %p \n", GET(GET(cur+ WSIZE)+WSIZE));
            // }
            // printf("==================================\n");
            if (cur == deletePtr)
            {   
                //  printf("삭제 ptr = %p \n",deletePtr);
                prePtr =(char*) GET(deletePtr);
                nextPtr =(char*) GET(deletePtr + WSIZE);

                if (prePtr != 0){
                    // prePtr이 존재.
                    if(nextPtr != 0){
                    // printf("삭제 조건 1\n");
                    // nextPtr이 존재.
                    // nextPtr 이전을 pre로 변경
                    PUT(prePtr + WSIZE,nextPtr);
                    // printf("prePtr 다음 = %p\n",GET(prePtr + WSIZE));


                    PUT(nextPtr,prePtr);
                    //  printf("nextPtr 이전 = %p\n",GET(nextPtr));

                    }else{
                        //  printf("삭제 조건 2\n");
                        // nextPtr이 없음 
                        // prePtr의 다음을 0(NULL)로 교체
                        PUT(prePtr+WSIZE,0);
                    }
                }else{
                    // prePtr == 0 처음 블록 이란 소리.

                    if(nextPtr != 0){
                        //  printf("삭제 조건 3\n");
                    // nextPtr이 존재.
                    // 처음이므로 explicit_listp가 nextPtr을 바라보게함.
                    PUT(nextPtr,0);
                    explicit_listp = nextPtr;
                    }else{
                        //  printf("삭제 조건 4\n");
                        // nextPtr이 없음 
                        // prePtr도 없음.
                        explicit_listp = 0;
                    }
                }
            
                break;
            }
            cur =(char*) GET(cur + WSIZE);
        }
// printf("delete 나감\n");
}
#endif


static void * coaleasce(void *ptr)
{
    // printf("coaleasce 들어옴\n");
    size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(ptr)));
    // size_t prev_alloc = GET_ALLOC(ptr - DSIZE);
    size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(ptr)));
    size_t size = GET_SIZE(HDRP(ptr));

    if (prev_alloc && next_alloc) /* case 1 : 둘다 할당 됐을 때*/
    {   
        // printf("coaleasce case1\n");
        #ifdef EXPLICIT
        if(explicit_listp != ptr){
             put_explicit_list(ptr);
        }
        #endif
        return ptr;     /* block ptr 바로 리턴*/
    }
    
    else if (prev_alloc && !next_alloc) /* case 2 : next 미할당 일 경우 */
    {
        // printf("coaleasce case2\n");
        #ifdef EXPLICIT
        del_explicit_list(NEXT_BLKP(ptr));
        #endif
        size += GET_SIZE(HDRP(NEXT_BLKP(ptr)));
        PUT(HDRP(ptr), PACK(size,0));
        PUT(FTRP(ptr), PACK(size,0));
        #ifdef EXPLICIT
        put_explicit_list(ptr);
        #endif
    }
    else if(!prev_alloc && next_alloc) /* case 3 : prev 미할당 일 경우 */ 
    {
        // printf("coaleasce case3\n");
       size += GET_SIZE(HDRP(PREV_BLKP(ptr)));
       PUT(FTRP(ptr), PACK(size,0));
       PUT(HDRP(PREV_BLKP(ptr)), PACK(size, 0));
       ptr = PREV_BLKP(ptr);
    }
    else{        /*  case 4 : 둘다 미할당 일 경우    */
                // printf("coaleasce case4\n");
        #ifdef EXPLICIT
        del_explicit_list(NEXT_BLKP(ptr));
        #endif
        size += GET_SIZE(HDRP(PREV_BLKP(ptr))) + GET_SIZE(FTRP(NEXT_BLKP(ptr)));
        PUT(HDRP(PREV_BLKP(ptr)), PACK(size, 0));
        PUT(FTRP(NEXT_BLKP(ptr)), PACK(size,0));
        ptr = PREV_BLKP(ptr);
    }
    //  printf("coaleasce 나감\n");
    return ptr;
}

/* find_fit (first fit)*/

static void *find_fit(size_t size){
    /*  first-fit search    */
    char * ptr;
    // printf("find 들어옴\n");
    #ifdef EXPLICIT
    // printf("explicit_listp = %p\n",explicit_listp);
    if(explicit_listp != 0){
        // printf("find 에 if 들어옴\n");
        // printf("explicit_listp 값 = %p\n",GET(explicit_listp));
        // printf("explicit_listp next 값 = %p\n",GET(explicit_listp + WSIZE));

        for(ptr = explicit_listp; GET_SIZE(HDRP(ptr)) > 0; ptr = GET(ptr + WSIZE))
        {
            // printf("size = %d\n",size);
            // printf("가진 사이즈 = %d\n",GET_SIZE(HDRP(ptr)));
            // printf("ptr  = %p\n", GET(ptr));
            // printf("next ptr = %p\n", GET(ptr+WSIZE));

            // printf("==================================\n");
            // printf("ptr = %p \n",ptr);
            // printf("ptr prev= %p \n",GET(ptr));
            // printf("ptr next= %p \n",GET(ptr+ WSIZE));
            // if(GET(ptr+ WSIZE) != 0){
            //     printf("ptr next 의 prev = %p \n", GET(GET(ptr+ WSIZE)));
            //     printf("ptr next 의 next = %p \n", GET(GET(ptr+ WSIZE)+WSIZE));
            // }
            // printf("==================================\n");

            if((size <= GET_SIZE(HDRP(ptr))))
            {
                return ptr;
            }
            if(GET(ptr + WSIZE) == 0){
                break;
            }
        }
        // printf("for 나감\n");
    }
    #endif

    #ifndef EXPLICIT

    // Search from next_fit to the end of the heap
    for(ptr = heap_listp; GET_SIZE(HDRP(ptr)) > 0; ptr = NEXT_BLKP(ptr)){
        if(!GET_ALLOC(HDRP(ptr)) && (size <= GET_SIZE(HDRP(ptr))))
        {
            return ptr;
        }
    }
    #endif
    return NULL;
}

static void place(void * ptr, size_t size){
    size_t totalSize = GET_SIZE(HDRP(ptr));
    // printf("place 들어옴\n");
    if ((totalSize - size) >= (2 * DSIZE))
    {
        #ifdef EXPLICIT
        del_explicit_list(ptr);
        #endif
        PUT(HDRP(ptr), PACK(size,1));
        PUT(FTRP(ptr), PACK(size,1));
        ptr = NEXT_BLKP(ptr);
        #ifdef EXPLICIT
        put_explicit_list(ptr);
        #endif
        PUT(HDRP(ptr), PACK(totalSize - size, 0));
        PUT(FTRP(ptr), PACK(totalSize - size, 0));

    }else{
        #ifdef EXPLICIT
        del_explicit_list(ptr);
        #endif
        PUT(HDRP(ptr), PACK(totalSize,1));
        PUT(FTRP(ptr), PACK(totalSize,1));
    }
}
/*
 * mm_realloc - Implemented simply in terms of mm_malloc and mm_free
 */
void *mm_realloc(void *ptr, size_t size)
{
    void *oldptr = ptr;
    void *newptr;
    size_t copySize;
    
    newptr = mm_malloc(size);
    if (newptr == NULL){
        return NULL;
    }   
    // copySize = *(size_t *)((char *)oldptr - (SIZE_T_SIZE + 8));
    copySize = GET_SIZE(HDRP(oldptr));
    if (size < copySize){
         copySize = size;
    }
    memcpy(newptr, oldptr, copySize);
    mm_free(oldptr);
    return newptr;
}













