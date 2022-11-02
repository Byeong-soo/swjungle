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
// 주석을 아무것도 안풀면 기본 implicit - first_find 로 동작합니다.
// 기본 - impicit - first_find
/**********************************************************************/
// EXPLICIT 으로 변경! 아래의 주석을 풀어주세요
// #define EXPLICIT
// EXPLICIT OPTION 주소 방식으로 정렬입니다. 위의 주석과 아래의 주석을 같이 풀어주세요
// #define EXPLICIT_ADDRESS
/**********************************************************************/ 
// SIMPLE_SEGREGATED 방식입니다. 주석을 풀어주세요 위의 주석과 함꼐 풀면 오류!
// #define SIMPLE_SEGREGATED

/**********************************************************************/ 


// Results for mm malloc: implicit
// trace  valid  util     ops      secs  Kops
//  0       yes   99%    5694  0.009156   622
//  1       yes   99%    5848  0.008809   664
//  2       yes   99%    6648  0.013978   476
//  3       yes  100%    5380  0.010668   504
//  4       yes   66%   14400  0.000168 85868
//  5       yes   92%    4800  0.010135   474
//  6       yes   92%    4800  0.009203   522
//  7       yes   55%   12000  0.241498    50
//  8       yes   51%   24000  0.457143    53
//  9       yes   27%   14401  0.121926   118
// 10       yes   34%   14401  0.003640  3957
// Total          74%  112372  0.886323   127

// Perf index = 44 (util) + 8 (thru) = 53/100


/**********************************************************************/ 
// Results for mm malloc: EXPLICIT
// trace  valid  util     ops      secs  Kops
//  0       yes   88%    5694  0.000345 16514
//  1       yes   93%    5848  0.000265 22101
//  2       yes   95%    6648  0.000476 13958
//  3       yes   97%    5380  0.000362 14854
//  4       yes   66%   14400  0.000248 58018
//  5       yes   89%    4800  0.001494  3213
//  6       yes   88%    4800  0.001484  3235
//  7       yes   55%   12000  0.010079  1191
//  8       yes   51%   24000  0.054598   440
//  9       yes   27%   14401  0.122231   118
// 10       yes   30%   14401  0.003973  3625
// Total          71%  112372  0.195554   575

// Perf index = 42 (util) + 38 (thru) = 81/100

/**********************************************************************/ 

// esults for mm malloc: EXPLICIT_ADDRESS
// trace  valid  util     ops      secs  Kops
//  0       yes   99%    5694  0.000290 19634
//  1       yes   99%    5848  0.000255 22924
//  2       yes   99%    6648  0.000402 16546
//  3       yes  100%    5380  0.000355 15142
//  4       yes   66%   14400  0.000245 58896
//  5       yes   92%    4800  0.004724  1016
//  6       yes   91%    4800  0.004793  1001
//  7       yes   55%   12000  0.083117   144
//  8       yes   51%   24000  0.472008    51
//  9       yes   27%   14401  0.124432   116
// 10       yes   30%   14401  0.003947  3649
// Total          74%  112372  0.694569   162

// Perf index = 44 (util) + 11 (thru) = 55/100

/**********************************************************************/ 

// Results for mm malloc: SIMPLE_SEGREGATED
// trace  valid  util     ops      secs  Kops
//  0       yes   18%    5694  0.000960  5932
//  1       yes   15%    5848  0.000407 14369
//  2       yes   24%    6648  0.000438 15195
//  3       yes   32%    5380  0.000353 15224
//  4        no   ERROR: mem_sbrk failed. Ran out of memory...
//  5        no   ERROR [trace 5, line 139]: Payload (0xf6b0ba90:0xf6b0c2a8) lies outside heap
//  6        no   ERROR [trace 6, line 377]: Payload (0xf6e785e8:0xf6e78e05) lies outside heap (0xf68be010:0xf6e78def)
//  7       yes    7%   12000  0.000785 15291
//  8        no    ERROR: mem_sbrk failed. Ran out of memory...
//  9        no    mm_realloc did not preserve the data from old block
// 10        no    mm_realloc did not preserve the data from old block
// Total            -       -         -     -
/**********************************************************************/ 

/*  Basic constants and macros */
#define WSIZE 4 /* Wdrd and header /footer size(bytes)*/
#define DSIZE 8 /* Double word size (byte)*/
#ifndef SIMPLE_SEGREGATED
#define CHUNKSIZE (1<<12) /* Extend heap by this amount (bytes) */
#endif
#ifdef SIMPLE_SEGREGATED
#define CHUNKSIZE ((1<<12) + DSIZE) /* Extend heap by this amount (bytes) */
#endif

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






/* single word (4) or double word (8) alignment */
#define ALIGNMENT 8

/* rounds up to the nearest multiple of ALIGNMENT */
#define ALIGN(size) (((size) + (ALIGNMENT-1)) & ~0x7)
#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))

#ifdef EXPLICIT
// EXPLICIT 에서만 사용하는 함수 입니다.
static void * explicit_listp = 0;
static void put_explicit_list(void * ptr);
static void del_explicit_list(void * ptr);
#endif
#ifdef SIMPLE_SEGREGATED
// SIMPLE_SEGREGATED 에서만 사용하는 함수들 입니다.
static char * start_ptr;
static int get_offset(size_t size);
static void* split_block(void * ptr,size_t need_size);
static size_t get_size_with_position(char * ptr);
static void put_explicit_list(void * ptr);
static void del_explicit_list(void * ptr);
static void *extend_heap(size_t words,size_t need_size);
static size_t size_changer(size_t size);
#endif
static char * heap_listp;
#ifndef SIMPLE_SEGREGATED
static void * extend_heap(size_t size);
static void * coaleasce(void * ptr);
#endif
static void * find_fit(size_t size);
// static void * find_fit_next(size_t size);
static void place(void * ptr, size_t size);
/* 
 * mm_init - initialize the malloc package.
 */

int mm_init(void)
{
    /* Create the initial empty heap */
    #ifndef SIMPLE_SEGREGATED
    if ((heap_listp = mem_sbrk(4*WSIZE)) == (void *) -1){
        return -1;
    }
    #endif
    
    #ifdef SIMPLE_SEGREGATED
    // 각각 분류의 포인터를 저장하기 위해서 프롤로그 블럭의 크기를 늘려줍니다.
     if ((heap_listp = mem_sbrk(8*WSIZE)) == (void *) -1){
        return -1;
    }
    #endif

    #ifndef SIMPLE_SEGREGATED
    PUT(heap_listp, 0);                             /*  Alignment padding   */
    PUT(heap_listp + (1*WSIZE), PACK(DSIZE, 1));    /*  Prologue header   */
    PUT(heap_listp + (2*WSIZE), PACK(DSIZE, 1));    /*  Prologue footer   */
    PUT(heap_listp + (3*WSIZE), PACK(0, 1));        /*  Epilogue header    */
    heap_listp += (2*WSIZE);
    #endif
        #ifdef SIMPLE_SEGREGATED
        // 각 크기의 경우의 수 입니다. SIMPLE_SEGREGATED 는 남은 블럭을 합치지 않기때문에
        // 최적의 수를 찾아야 할꺼 같은데... 찾지못했습니다... 메모리 부족!      
        PUT(heap_listp, 0);                     
        PUT(heap_listp + (1*WSIZE), PACK(6*WSIZE, 1));                       
        // PUT(heap_listp + (2*WSIZE), 0);                     /*  2의 0승  1 */  
        // PUT(heap_listp + (3*WSIZE), 0);                     /*  2의 1승  2 */  
        // PUT(heap_listp + (4*WSIZE), 0);                     /*  2의 2승  3~4 */  
        // PUT(heap_listp + (5*WSIZE), 0);                     /*  2의 3승  5~8 */  
        // PUT(heap_listp + (2*WSIZE), 0);                     /*  2의 4승  1~16 */  
        // PUT(heap_listp + (2*WSIZE), 0);                     /*  2의 5승  17~32 */  
        PUT(heap_listp + (2*WSIZE), 0);                     /*  2의 6승  32~64 */ 
        // PUT(heap_listp + (3*WSIZE), 0);                     /*  2의 7승  65~128 */ 
        PUT(heap_listp + (3*WSIZE), 0);                     /*  2의 8승   256*/ 
        // PUT(heap_listp + (5*WSIZE), 0);                     /*  2의 9승   */ 
        PUT(heap_listp + (4*WSIZE), 0);                     /*  2의 10승  1024*/ 
        // PUT(heap_listp + (7*WSIZE), 0);                     /*  2의 11승  */ 
        // PUT(heap_listp + (6*WSIZE), 0);                     /*  2의 12승  */ 
        PUT(heap_listp + (5*WSIZE), 0);                     /*  2의 12승 이상인애들  */ 
        PUT(heap_listp + (6*WSIZE), PACK(6*WSIZE, 1));     /*  Prologue header   */
        PUT(heap_listp + (7*WSIZE), PACK(0, 1));     /*  Prologue header   */
        start_ptr = heap_listp + (7*WSIZE);
        heap_listp += (2*WSIZE);
    
        #endif

    #ifndef SIMPLE_SEGREGATED         
    /* Extend the empty heap with a free block of CHUNKSIZE bytes */
    if (extend_heap(CHUNKSIZE / WSIZE) == NULL){
        return -1;
    }
    #endif
    return 0;
}
#ifndef SIMPLE_SEGREGATED 
static void *extend_heap(size_t words){
#endif
#ifdef SIMPLE_SEGREGATED
//SIMPLE_SEGREGATED 에서는 블럭들을 모두 잘라줘야하기 떄문에 블럭을 잘를 크기를 함께 인자로 넘겨줍니다.
static void *extend_heap(size_t words,size_t need_size){
#endif
    char *bp;
    size_t size;
    /*  Allocate an even number of words to maintain aligmnet */
    
    size = (words % 2) ? (words+1) * WSIZE : words * WSIZE;
    if ((long)(bp = mem_sbrk(size)) == -1){
        return NULL;
    }
    #ifndef SIMPLE_SEGREGATED 
    /*  Initialize free block header/footer and the epilogue header */
    PUT(HDRP(bp), PACK(size,0));            /*  Free block header   */
    PUT(FTRP(bp), PACK(size,0));            /*  Free block footer   */
    PUT(HDRP(NEXT_BLKP(bp)),PACK(0,1));     /*  New epliogue header */
    #endif

    #ifdef SIMPLE_SEGREGATED 

    // 청크 사이즈가 2^12 + 8 이기 떄문에 사이즈만 판별하기 위해 8을 뺴줍니다.
    if (size <= (CHUNKSIZE) -DSIZE)
    {   
        // 할당을 받고 난뒤에는 큰 페이즈의 헤더에 사이즈를 넣어주고, 풋터에는 자리는 경계표시인 1을 넣어주고
        // 에필로그 블록을 생성합니다.
        PUT(HDRP(bp), need_size);           
        PUT(bp + (CHUNKSIZE) - DSIZE, 1); 
        PUT(bp + (CHUNKSIZE)-WSIZE, PACK(0,1));          
    }else{
        // 청크 사이즈 보다 클 경우에는 무조건 한덩이만 생성되기 때문에, 전체 사이즈에서 헤더 풋터 값을
        // 뺸 값만 사이즈로 집어 넣습니다. 나머지는 풋터와 에필로그!
        PUT(HDRP(bp), size - DSIZE);           
        PUT(bp + size - DSIZE, 1);    
        PUT(bp + size - WSIZE,PACK(0,1));
    }
    #endif

    /*  Coalesce if the previous block was free */
    #ifndef SIMPLE_SEGREGATED
    return coaleasce(bp);
    #endif
    #ifdef SIMPLE_SEGREGATED
    // SIMPLE_SEGREGATED 는 코~얼러싱을 따로 하지않기 떄문에 블럭 포인터만 리턴합니다.
    return bp;
    #endif
}


/* 
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    size_t asize;   /* Adjusted block size  */
    size_t extendsize; /*   Amount to extend heap if no fit */
    char *ptr;

    /*  Ignore spurious requests    */
    if(size == 0){
        return NULL;
    }
    #ifndef SIMPLE_SEGREGATED
    /*  Adjust block size to include overhead and alignment reqs    */
    if (size<= DSIZE)
    {
        asize = 2*DSIZE;
    }
    else
    {
        asize = DSIZE * ((size + (DSIZE) + (DSIZE -1)) / DSIZE);
        // asize = ALIGN(size) + DSIZE;
    }

    #endif
    #ifdef SIMPLE_SEGREGATED
    // SIMPLE_SEGREGATED 는 값의 크기가 정해져 있기 떄문에 필요 크기를 알기위해서, 정해놓은 값의 분류 안에서
    // 큰수로 사이즈를 변경해줍니다?
    asize = size_changer(size);
    #endif
    /* Search the free list for a fit   */
    if((ptr = find_fit(asize)) != NULL){
        place(ptr,asize);
        return ptr; 
    }

    /* No fit found, Get more memory and place the block */
    #ifdef SIMPLE_SEGREGATED
    if (asize > (CHUNKSIZE))
    {   
        // SIMPLE_SEGREGATED 는 2^12 를 넘어가면 단순히 1만 필요해도 무조건 큰 블럭(페이지)이 2개가 필요하기
        // 떄문에 몫을 구해서 1 더해주고 페이지 수를 더해줍니다. ( 주소 방식식으로 크기를 알아야 하기때문에
        // 블럭 덩이의 크기가 모두 일정해야 해더를 찾아 갈수 있고, 나의 크기를 알수 있습니다.)
        asize = (((asize/(CHUNKSIZE)) + 1) * (CHUNKSIZE));
    }
    #endif

    extendsize = MAX(asize,(CHUNKSIZE));
    #ifndef SIMPLE_SEGREGATED
    if((ptr = extend_heap(extendsize/WSIZE)) == NULL){
         return NULL;
    }

    #endif

    #ifdef SIMPLE_SEGREGATED
    // 페이지의 헤더에 값을 저장해야 하기때문에, 기준의 값도 같이 인자로 넘겨줍니다. 
    if((ptr = extend_heap(extendsize/WSIZE,asize)) == NULL){
         return NULL;
    }
    //  만약 블럭이 청크보다 작으면 잘라야하기 떄문에 값보다 작으면 잘라줍니다.
    if(asize < (CHUNKSIZE)){
        ptr = split_block(ptr,asize);
    }
    #endif
    // 할당!
    place(ptr,asize);
    return ptr;
}

/*
 * mm_free - Freeing a block does nothing.
 */
void mm_free(void *ptr)
{
        
    #ifndef SIMPLE_SEGREGATED
    size_t size = GET_SIZE(HDRP(ptr));
    PUT(HDRP(ptr), PACK(size,0));
    PUT(FTRP(ptr), PACK(size,0));
    coaleasce(ptr);
    #endif
    #ifdef SIMPLE_SEGREGATED
    // SIMPLE_SEGREGATED 는 해제하면 가용 리스트에 붙여주기만 하면 됩니다.
    put_explicit_list(ptr);
    #endif
}

#ifdef SIMPLE_SEGREGATED
// heap_listp 에서 기준을 찾아가야하기 때문에 얼마나 떨어져있는지 구하는 함수입니다.
// 급해서 다듬지는 못했습니다.
static int get_offset(size_t size){

    int offset = 0;
    if (size <= 64){
        return 0;
    }
    if (size > (1<<12)){
        offset = 3;
    }else{
         while (size > 64)
        {
            size = size >> 2;
            offset+=1;
            if(offset ==3){
                break;
            }
        }
    }
    return offset*WSIZE;
}
// 앞서 얘기했듯이 크기를 조절해주는 함수입니다. 2^n 승으로 만들어주기 위해 비트연산을 사용했습니다.
static size_t size_changer(size_t size){
    size_t change_size = 64;

    if(size > CHUNKSIZE){
        return size;
    }
    if(size <= 64){
        return 64;
    }
    while ((size) > 64)
        {
        size = size >> 1;
        change_size = change_size << 1;
        }
    return change_size;
}

// 지금 현재 위치에서 사이즈를 찾기위해 해더를 찾는 연산입니다.
// 블록의 크기가 무조건 동일하기때문에 나머지 연산을 사용했습니다.
static size_t get_size_with_position(char * ptr){
    char * head_ptr = ptr -((ptr - start_ptr) % (CHUNKSIZE)) -4;
    return GET(head_ptr);
}

// 블럭을 잘라주는 함수입니다. 크기는 2^12로 고정입니다. 더 큰 크기는 자를 필요가 없기 떄문입니다.
static void* split_block(void* ptr,size_t need_size){
   
        size_t totalSize = 4096;
        int count = (totalSize) / need_size;
        void * cur;
        cur = ptr;
        while (count >0)
        {
            // 자르면서 바로바로 자기에게 맞는 위치로 붙여줍니다. 1을 만나거나 count가 0이되면 탈출합니다.
            put_explicit_list(cur);
            if(GET(cur + need_size) == 1 || count == 0){
                break;
            }
            cur = cur + need_size;
            count -=1;
        }
    return cur;
}

// 포인터들 끼리 SUC로 연결하는 함수 입니다.
 static void put_explicit_list(void * ptr){
    char * first_ptr;
    // 현재 위치에서 크기를 받아옵니다. heap_listp에서 기준까지 가기위해서 offset을 구합니다.
    int offset = get_offset(get_size_with_position(ptr));
    first_ptr = heap_listp + (offset);

    // 블럭이 여러개일때 처리입니다. 맨 앞으로 보내주고 원래 있던 블록을 나의 뒷쪽으로 붙여줍니다.
    if(GET(first_ptr) != 0){
        PUT(ptr,GET(first_ptr));
        PUT(first_ptr,ptr);
    }else{
        // 블럭이 처음일떄의 처리 입니다.
        PUT(first_ptr,ptr);
        PUT(ptr , 0);
    }
 }

// 가용 리스트에서 삭제하는 함수 입니다.
static void del_explicit_list(void * delete_ptr){
    char * first_ptr;
    int offset = get_offset(get_size_with_position(delete_ptr));
    first_ptr = heap_listp + (offset);

    // offset 이 12 이상이라는 얘기는 전부 2^12 이상이라는 애기 입니다.
    if(offset >= 3 * WSIZE){
        // 처음에 바로 발견할때
        if(delete_ptr == (char*)GET(first_ptr)){
            // 블럭이 2개일때
            if(GET(GET(first_ptr)) != 0 ){
                PUT(first_ptr,GET(GET(first_ptr)));
            }else{
                // 블럭이 처음 하나였을떄. 0으로 리셋
                PUT(first_ptr,0);
            }
        }
        // 처음이 아닐때. 탐색을 통해서 찾아야 합니다.
        else {
                char * cur = GET(first_ptr);
                // SUCC 밖에 없기 때문에 다음을 확인해줘야 합니다.
                while (cur != 0)
                {
                    char * next = GET(cur);
                    if(delete_ptr == next){
                        // 만약 다음이 나와 같다면 현재에 다음의 다음 포인터를 넣어줍니다.
                        PUT(cur,GET(next));
                        return;
                    }
                    // 찾을때 까지 한칸씩 앞으로 갑니다.
                    cur = GET(cur);
                }
            }
    }else{
        if(GET(first_ptr)!=0){
            // 3 미만의 offset을 가질 때.
            // 다음 다음이 널이 아닐때.
            if (GET(GET(first_ptr)) !=0)
            {
                PUT(first_ptr,GET(GET(first_ptr)));
            }else{
                PUT(first_ptr,0);
            }
        }
    }
}
 #endif

#ifdef EXPLICIT
static void put_explicit_list(void * ptr){
    #ifdef SIMPLE_SEGREGATED
    char * first_ptr;
    int offset = get_offset(GET_SIZE(HDRP(ptr)));
    first_ptr = GET(heap_listp + (offset));
    if (first_ptr == 0)
    {   
        PUT(heap_listp+(offset*WSIZE),ptr);
        PUT(ptr, 0);
        PUT(ptr + WSIZE, 0);
    }else{
        PUT(first_ptr, ptr);
        PUT(ptr + WSIZE, first_ptr);
        PUT(ptr, 0);
        PUT(heap_listp+(offset*WSIZE),ptr);
    }
    #endif

    #ifndef SIMPLE_SEGREGATED
    if (explicit_listp == 0)
    {
        explicit_listp = ptr;
        PUT(ptr, 0);
        PUT(ptr + WSIZE, 0);
    ;
    }else
    {
        // 0이 아님. 가용 리스트가 있음.
        // 첫 부분의 연결지점을 새로운 포인터로 함
        #ifndef EXPLICIT_ADDRESS
        PUT(explicit_listp, ptr);
        PUT(ptr + WSIZE, explicit_listp);
        PUT(ptr, 0);
        explicit_listp = ptr;
        #endif
        #ifdef EXPLICIT_ADDRESS
        // 처음부터 돌면서 주소 확인
        char * cur = explicit_listp;
        while (cur < ptr)
        {
            if(GET(cur+WSIZE) == 0){
                break;
            }
            cur = GET(cur+WSIZE);
        }
        // ptr이 제일 작을때는 explicit_listp가 봐야함
        if (cur == explicit_listp)
        {
            PUT(explicit_listp, ptr);
            PUT(ptr + WSIZE, explicit_listp);
            PUT(ptr, 0);
            explicit_listp = ptr;
        }else
        {
            // 맨 앞은 아님
            // 맨뒤로 갈 경우
            if(GET(cur + WSIZE) == 0){
                PUT(ptr,cur);
                PUT(ptr + WSIZE,0);
                PUT(cur+WSIZE,ptr);
            }else{
                // 중간에 갈 경우
                PUT(GET(cur) + WSIZE,ptr);
                PUT(ptr,GET(cur));

                PUT(ptr+WSIZE,cur);
                PUT(cur,ptr);
            }
           
        }
        #endif
    }
    #endif
}


static void del_explicit_list(void * delete_ptr){
    char * deletePtr =delete_ptr;
    char * prePtr;
    char * nextPtr;
    char * cur = explicit_listp;

    #ifdef SIMPLE_SEGREGATED
    int offset = get_offset(GET_SIZE(HDRP(delete_ptr)));
    cur = GET(heap_listp +(offset));
    #endif
     while (cur != 0)
        {
            if (cur == deletePtr)
            {   
                prePtr =(char*) GET(deletePtr);
                nextPtr =(char*) GET(deletePtr + WSIZE);

                if (prePtr != 0){
                    // prePtr이 존재.
                    if(nextPtr != 0){
                    PUT(prePtr + WSIZE,nextPtr);
                    PUT(nextPtr,prePtr);
                    }else{
                        // nextPtr이 없음 
                        // prePtr의 다음을 0(NULL)로 교체
                        PUT(prePtr+WSIZE,0);
                    }
                }else{
                    // prePtr == 0 처음 블록 이란 소리.

                    if(nextPtr != 0){
                    // nextPtr이 존재.
                    // 처음이므로 explicit_listp가 nextPtr을 바라보게함.
                    PUT(nextPtr,0); 
                        #ifndef SIMPLE_SEGREGATED
                        explicit_listp = nextPtr;
                        #endif
                        #ifdef SIMPLE_SEGREGATED
                        PUT(cur,nextPtr);
                        #endif
                    }else{
                        // nextPtr이 없음 
                        // prePtr도 없음.
                        #ifndef SIMPLE_SEGREGATED
                        explicit_listp = 0;
                        #endif
                        #ifdef SIMPLE_SEGREGATED
                        PUT(cur,0);
                        #endif
                    }
                }
                break;
            }
            cur =(char*) GET(cur + WSIZE);
        }
}
#endif

#ifndef SIMPLE_SEGREGATED
static void * coaleasce(void *ptr)
{

    size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(ptr)));
    size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(ptr)));
    size_t size = GET_SIZE(HDRP(ptr));
    /* case 1 : 둘다 할당 됐을 때*/
    if (prev_alloc && next_alloc) 
    {   

        #ifdef EXPLICIT
        if(explicit_listp != ptr){
             put_explicit_list(ptr);
        }
        #endif
        return ptr;
    }
    /* case 2 : next 미할당 일 경우 */
    else if (prev_alloc && !next_alloc) 
    {

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
    /* case 3 : prev 미할당 일 경우 */ 
    else if(!prev_alloc && next_alloc) 
    {
       size += GET_SIZE(HDRP(PREV_BLKP(ptr)));
       PUT(FTRP(ptr), PACK(size,0));
       PUT(HDRP(PREV_BLKP(ptr)), PACK(size, 0));
       ptr = PREV_BLKP(ptr);
    }
     /*  case 4 : 둘다 미할당 일 경우    */
    else{       
                
        #ifdef EXPLICIT
        del_explicit_list(NEXT_BLKP(ptr));
        #endif
        size += GET_SIZE(HDRP(PREV_BLKP(ptr))) + GET_SIZE(FTRP(NEXT_BLKP(ptr)));
        PUT(HDRP(PREV_BLKP(ptr)), PACK(size, 0));
        PUT(FTRP(NEXT_BLKP(ptr)), PACK(size,0));
        ptr = PREV_BLKP(ptr);
    }

    return ptr;
}
#endif

/* find_fit (first fit)*/
static void *find_fit(size_t size){

    char * ptr;
    #ifdef SIMPLE_SEGREGATED
    // 사이즈의 크기로 얼마나 떨어진 블럭인지 찾습니다.
    int offset = 0;
    char *first_ptr;
    offset =  get_offset(size);
    first_ptr = heap_listp + offset;

    // 범위가 무한대인 애들은 만나면 0을 리턴해줍니다. ( 왜했는지 기억이 안나요...)
    if(offset == 3 * WSIZE){
        if (GET(first_ptr) == 0)
        {
            return NULL;
        }
        
        // 찾은 블럭의 크기를 비교해주기위해서 블럭의 해더에서 사이즈를 가져옵니다.
        size_t compare_size = GET(GET(first_ptr) - WSIZE);
        char * cur = GET(first_ptr);

        while (cur != 0)
        {
           // 찾은 사이즈가 나보다 작다! 리턴해줍니다.
            if(size <= compare_size){
                return cur;
            }
            // 찾을때 까지 다음으로 넘어 갑니다.
            cur = GET(cur);
            // 더이상 값이 없으면 널을 리턴!
            if(cur == 0){
                return NULL;
            }
            // 다음 블럭으로 가면 다음 블럭의 크기로 갱신해줍니다.
            compare_size = GET(cur - WSIZE);
        }
        
    }else{
        // 3 미만인 애들은 그냥 처음에 값이 있으면 바로 넘겨주면 됩니다. 어차피 똑같은거 쓰니까...
        if(GET(first_ptr) !=0){
        return GET(first_ptr);
        }
    }
   
    #endif



#ifdef EXPLICIT
    #ifndef SIMPLE_SEGREGATED
    if(explicit_listp != 0){
        for(ptr = explicit_listp; GET_SIZE(HDRP(ptr)) > 0; ptr = GET(ptr + WSIZE))
        {
            if((size <= GET_SIZE(HDRP(ptr))))
            {
                return ptr;
            }
            if(GET(ptr + WSIZE) == 0){
                break;
            }
        }
    }
    #endif

 
#endif
   #ifndef EXPLICIT
    #ifndef SIMPLE_SEGREGATED

    // Search from next_fit to the end of the heap
    for(ptr = heap_listp; GET_SIZE(HDRP(ptr)) > 0; ptr = NEXT_BLKP(ptr)){
        if(!GET_ALLOC(HDRP(ptr)) && (size <= GET_SIZE(HDRP(ptr))))
        {
            return ptr;
        }
    }
    #endif
    #endif
    return NULL;
}
// 할당해주는 함수
static void place(void * ptr, size_t size){
    #ifdef SIMPLE_SEGREGATED
    // SIMPLE_SEGREGATED 은 그냥 따로 해주는게 없습니다.
    // 할당 해주면 가용 리스트에서 삭제합니다 그럼 끝!
    del_explicit_list(ptr);
    #endif

    #ifndef SIMPLE_SEGREGATED
    size_t totalSize = GET_SIZE(HDRP(ptr));
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
    #endif
}
/*
 * mm_realloc - Implemented simply in terms of mm_malloc and mm_free
 */
// 손도 못댐 그냥 그대로 썼습니다...
void *mm_realloc(void *ptr, size_t size)
{
    void *oldptr = ptr;
    void *newptr;
    size_t copySize;
    
    newptr = mm_malloc(size);
    if (newptr == NULL){
        return NULL;
    }   
    copySize = GET_SIZE(HDRP(oldptr));
    if (size < copySize){
         copySize = size;
    }
    memcpy(newptr, oldptr, copySize);
    mm_free(oldptr);
    return newptr;
}













