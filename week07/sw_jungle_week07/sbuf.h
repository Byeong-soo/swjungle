#include "csapp.h"

#define NTHREADS 4
#define SBUFSIZE 16

typedef struct
{
  int *buf;
  int n;
  int front;
  int rear;
  sem_t mutex;
  sem_t slots;
  sem_t items;
}sbuf_t;

void sbuf_init(sbuf_t *sp, int n);
void sbuf_deinit(sbuf_t *sp);
void subf_insert(sbuf_t *sp,int item);
int sbuf_remove(sbuf_t *sp);