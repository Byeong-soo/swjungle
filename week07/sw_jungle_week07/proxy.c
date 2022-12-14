#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include "csapp.h"
#include "sbuf.h"

/* Recommended max cache and object sizes */
#define MAX_CACHE_SIZE 1049000
#define MAX_OBJECT_SIZE 102400

char* indexList[26];
unsigned int totalSize;
char* LRUP_first;
char* LRUP_end;

typedef struct LRU_list {
	struct LRU_list * prev; 
  char * key;
  unsigned int size;
	struct LRU_list * next;
}LRU_list;

typedef struct DLinked_list {
	struct DLinked_list * prev; 
  char * key;
  char * header;
  char * body;
  unsigned int size;
	struct DLinked_list * next;
}DLinked_list;



// Double linked list
struct DLinked_list* DL_init(char* key,unsigned int size,char *header,char *body);
void DL_insert(int index, DLinked_list* newNode);
void DL_delete(DLinked_list* delete_node,char* indexList);

struct LRU_list* LRU_list_init(char* key,int size);
void LRU_list_insert(LRU_list* newNode);
void LRU_list_delete(LRU_list* delete_node);

// hash
int charToHashInt(char* firstCahr);
void* thread(void *vargp);
void do_it(int fd, int clientfd,char* method,char* path,char* version);
void get_connection(int fd);
void read_requesthdrs(rio_t *rp);
void read_body(rio_t *rp,char* send);
void *thread(void *vargp);
sbuf_t sbuf;

/* You won't lose style points for including this long line in your code */
static const char *user_agent_hdr =
    "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Gecko/20120305 "
    "Firefox/10.0.3\r\n";

int main(int argc, char **argv) {

  int listenfd, connfd;
  char hostname[MAXLINE], port[MAXLINE];
  socklen_t clientlen;
  struct sockaddr_storage clientaddr;
  pthread_t tid;

  /* Check command line args */
  if (argc != 2) {
    fprintf(stderr, "usage: %s <port>\n", argv[0]);
    exit(1);
  }

  listenfd = Open_listenfd(argv[1]);

  sbuf_init(&sbuf,SBUFSIZE);
  for (int i = 0; i < NTHREADS; i++)
  {
    Pthread_create(&tid,NULL,thread,NULL);
  }
  
  while (1) {
    clientlen = sizeof(clientaddr);
    connfd = Accept(listenfd, (SA *)&clientaddr,&clientlen);  // line:netp:tiny:accept
    sbuf_insert(&sbuf,connfd);
  }
}


void get_connection(int coonfd){
  int clientfd;
  struct stat sbuf;
  char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE], header[MAXLINE], content[MAXLINE];
  char filename[MAXLINE], cgiargs[MAXLINE],temp[MAXLINE], hostname[MAXLINE],port[MAXLINE],path[MAXLINE],send[MAXLINE];
  rio_t rio;
  char * p;
  unsigned int contentlength;
  /* Rad request line and headers */
  Rio_readinitb(&rio, coonfd);
  Rio_readlineb(&rio, buf, MAXLINE);
  sscanf(buf, "%s %s %s ", method, uri, version);
  // http:// ???????????? temp??? ?????? ??????(localhost:8000/home.html)
  strcpy(temp, uri+7);
  p = strchr(temp, '/');
  // localhost:8000/home.html (/)???????????? home.html ??????
  strcpy(path,p+1);
  *p = '\0';
  p = strchr(temp,':');
  *p = '\0';
  //(:) ???????????? localhost ??? 8000 ??????
  strcpy(hostname,temp);
  strcpy(port,p+1);

  // ?????? ??????(??????)
  read_requesthdrs(&rio);

  // ?????? ??????
  int hashIndex = charToHashInt((char*)path);
  DLinked_list* node = (DLinked_list*) indexList[hashIndex];

   while (node!= NULL)
    {
      node = node->next;
    }
  node = (DLinked_list*) indexList[hashIndex];
  // ????????? ?????? ?????????
  if(node != NULL){
    // while??? ????????? ??????
    while (node!= NULL)
    {
      // ????????? key(??????)??? ????????? ??????
      if (!strcmp(node->key,path))
      {
        // ????????? ?????? ?????? ????????? ????????? ????????? ????????? ???????????? ?????? ??????.
        Rio_writen(coonfd,node->header,strlen(node->header));
        Rio_writen(coonfd,node->body,(node->size) - strlen(node->header));
        // ?????? tiny ??? ????????? ???????????? ????????? ?????? ??????

        LRU_list * moveNode = (LRU_list *)LRUP_first;
        while (moveNode!=NULL)
        {
          // ?????? ??????
          // LRU ???????????? ????????????.
          if(!strcmp(moveNode->key,path)){
            LRU_list_move_first(moveNode);
            break;
          }

          moveNode = moveNode->next;
        }
        return;
      }
      // ????????? ????????? ????????????, ????????? ????????? ????????? ?????? ??????
      // sprintf(stderr,"%s",(char*)node->key);
      node = node->next;
    }
  }
  // while?????? ????????????????????? ????????? ???????????? tiny??? ??????
  clientfd = Open_clientfd(hostname,port);

  // proxy -> tiny??? ?????? ?????? ??????
  sprintf(buf,"%s /%s HTTP/1.0\r\n",method,path);
  sprintf(buf, "%sHost: %s\r\n",buf,hostname);
  sprintf(buf, "%s%s",buf,user_agent_hdr);
  sprintf(buf, "%sConnection: close\r\n",buf);
  sprintf(buf, "%sProxy-Connection: close\r\n\r\n",buf);
  // ?????? ?????? ??????
  Rio_writen(clientfd,buf,strlen(buf));

  // ?????? ?????? ????????????
  Rio_readinitb(&rio, clientfd);
  Rio_readlineb(&rio, buf, MAXLINE);
  Rio_writen(coonfd,buf,strlen(buf));
  // ????????? ???????????? ?????? header??? ??????
  sprintf(header,buf);



  // ???????????? ????????? ????????? ???????????? ??????????????? ????????? ???????????? client??? ???????????? header??? ????????????
  // header??? ?????? ?????? ????????? ????????? ?????????????????? ??????.
  while (strcmp(buf, "\r\n"))
  {
    Rio_readlineb(&rio, buf, MAXLINE);
    sprintf(header,"%s%s",header,buf);
    Rio_writen(coonfd,buf,strlen(buf));
    // ????????? ????????? ?????? ?????? Content-length ?????? ??????????????? ????????? ?????? ????????? ????????????.
    if (strstr(buf,"Content-length:"))
    {
      char* temp;
      p = index(buf,":");
      temp = (char*)buf+15;
      contentlength = atoi(temp);
    }
  }

  char *mm_header,*mm_body,*mm_path;
  if(contentlength){
    // contentlength??? 0??? ???????????? (???????????? ?????????) malloc??? Content-length?????? ???????????????.
    mm_body =(char*) malloc(contentlength);
    // Content-length ?????? ????????? ???????????? ????????????.
    Rio_readnb(&rio,mm_body,contentlength);
    // client ????????? ?????? ?????????.
    Rio_writen(coonfd,mm_body,contentlength);
  }

  // content??? ?????? ???????????? ????????? ????????? ????????????.
  if (contentlength <= MAX_OBJECT_SIZE)
  {
    //?????? ????????? ?????? ??????????????? ???????????? ????????????
    while ((totalSize + (unsigned int)strlen(header) + contentlength) >(unsigned int) MAX_CACHE_SIZE)
    {
      //while??? ????????? ?????? ?????????????????? ?????? ??????
      // ????????? ?????? ????????????
      LRU_list* delete_LRU_Node = (LRU_list*)LRUP_end;
      char path2 = delete_LRU_Node->key;
      int tempindex = charToHashInt(path2);
      DLinked_list* cur = (DLinked_list*) indexList[tempindex];

      // ?????? ?????? ??????
      while (cur!= NULL)
      {
        // ????????? key(??????)??? ????????? ??????
        if (!strcmp(cur->key,path2))
        {
          // ?????? ??????
          DL_delete(cur,indexList[tempindex]);
          LRU_list_delete(delete_LRU_Node);
          break;
        }
        // ????????? ????????? ????????????, ????????? ????????? ????????? ?????? ??????
        cur = cur->next;
        // LRU ?????? ???????????? ??? ?????? ???????????? hash ???????????? ????????? ??????.
      }
    }
  
    // ???????????? ???????????????.
    mm_header =(char*) malloc(strlen(header));
    mm_path =(char*) malloc(strlen(path));
    // ????????? ?????? ?????????????????? ???????????? ??????. ????????? ????????? ????????? ?????? ?????? ??????.
    mm_header = header;
    mm_path = path;
    
    // ?????? ?????? ????????? ???????????? ???????????? ?????? ?????? ???????????? ????????? ??????
    struct DLinked_list* newNode =  DL_init(mm_path,strlen(header) + contentlength,mm_header,mm_body);
    DL_insert(hashIndex,newNode);
    totalSize += strlen(header) + contentlength;

    DLinked_list* node = (DLinked_list*) indexList[hashIndex];
    while (node!= NULL)
    {
      node = node->next;
    }

    //LRU ??? ?????? ?????? ????????? ?????? ??????
    LRU_list* new_LRU_list = LRU_list_init(path,strlen(header) + contentlength);
    LRU_list_insert(new_LRU_list);
    Close(clientfd);
    return;
  }
  free(mm_body);
  Close(clientfd);
  return;
}

void read_requesthdrs(rio_t *rp){
  char buf[MAXLINE];
  Rio_readlineb(rp, buf, MAXLINE);
  while (strcmp(buf, "\r\n"))
  {
    Rio_readlineb(rp, buf, MAXLINE);
    // printf("%s",buf);
  }
  return;
}

// ????????? ?????? ??????. ?????? ?????? ?????? ??????
void *thread(void *vargp){
 pthread_detach(pthread_self());
 while (1)
 {
  int connfd = sbuf_remove(&sbuf);
  get_connection(connfd);
  Close(connfd);
 }
}

// ?????? ??????. ???????????? ???????????? ????????? ????????? ??????.
int charToHashInt(char*path){

    char firstChar = path[0];
    if (firstChar >= 65 && firstChar <= 90){
      firstChar += 32;
    } 
    return (int) (firstChar%26);
}

//????????? ??????, ???????????? ???????????? path??? ?????? ?????? ?????? ??????
struct DLinked_list* DL_init(char* key,unsigned int size,char *header,char *body){
  DLinked_list *newNode;
  newNode = (DLinked_list *)malloc(sizeof(DLinked_list));
  newNode->key = key;
  newNode->prev = NULL;
  newNode->next = NULL;
  newNode->size = size;
  newNode->header = header;
  newNode->body = body;
  return newNode;
}

// ????????? ????????? ???????????? ??????. ????????? ????????????.
void DL_insert(int index, DLinked_list* newNode){
  DLinked_list* firstNode =(DLinked_list *) indexList[index];
  if (firstNode == NULL)
  {
    indexList[index] = newNode;
  }
  else{
    newNode->next = firstNode;
    firstNode->prev = newNode;
    indexList[index] = newNode;
    
    firstNode =(DLinked_list *) indexList[index];

  }
}

//??????
void DL_delete(DLinked_list* delete_node,char* indexList){
  struct DLinked_list * prev_node = delete_node->prev;
  struct DLinked_list * next_node = delete_node->next;
  // prev??? Null ??????.
  if (prev_node == NULL){
    // ????????????.
    if (next_node == NULL){
      // next??? null ?????? ??????
      indexList = NULL;
    }else{
      // ????????? ?????? ??????
      next_node->prev = NULL;
      indexList = next_node;
    }
  }else{
    // prev??? ??????.
    // next??? ??????
    if (next_node == NULL)
    {
      prev_node->next = NULL;
    // next??? ??????
    }else{
      prev_node->next = next_node;
      next_node->prev = prev_node;
    }
  }
  // ?????? ?????????????????? ?????? ??????.
  free(delete_node->key);
  free(delete_node->header);
  free(delete_node->body);
  free(delete_node);
}

// LRU_list?????? ?????? ??????
struct LRU_list* LRU_list_init(char* key,int size){
  LRU_list * newNode;
  newNode = (LRU_list *)malloc(sizeof(LRU_list));
  newNode->key = key;
  newNode->size = size;
  newNode->prev = NULL;
  newNode->next = NULL;
  return newNode;
}

// ????????? ????????? ????????????.
void LRU_list_insert(LRU_list* newNode){
  LRU_list* firstNode =(LRU_list *) LRUP_first;
  if (firstNode == NULL)
  {
    LRUP_first = newNode;
    LRUP_end = newNode;
  }
  else{
    newNode->next = firstNode;
    firstNode->prev = newNode;
    LRUP_first = newNode;
  }
}

void LRU_list_move_first(LRU_list* move_node){
  LRU_list* firstNode =(LRU_list *) LRUP_first;
  struct LRU_list * prev_node = move_node->prev;
  struct LRU_list * next_node = move_node->next;

  // prev??? Null??? ????????? (???????????? ??????)
  if (prev_node != NULL)
 {
    // prev??? ??????.
    // next??? ??????
    if (next_node == NULL)
    {
      prev_node->next = NULL;
      LRUP_end = prev_node;
    // next??? ??????
    }else{
      prev_node->next = next_node;
      next_node->prev = prev_node;
    }
      move_node->next = firstNode;
      firstNode->prev = move_node;
      LRUP_first = move_node;
  }
  move_node->prev = NULL;
}

void LRU_list_delete(LRU_list* delete_node){
  struct LRU_list * prev_node = delete_node->prev;
  struct LRU_list * next_node = delete_node->next;

  // prev??? Null ??????.
  if (prev_node == NULL){
    // ????????????.
    if (next_node == NULL){
      // next??? null ?????? ??????
      LRUP_first = NULL;
      LRUP_end = NULL;
    }else{
      // ????????? ?????? ??????
      next_node->prev = NULL;
      LRUP_first = next_node;
    }
  }else{
    // prev??? ??????.
    // next??? ??????
    if (next_node == NULL)
    {
      prev_node->next = NULL;
      LRUP_end = prev_node;
    // next??? ??????
    }else{
      prev_node->next = next_node;
      next_node->prev = prev_node;
    }
  }
  // ?????? ?????????????????? ?????? ??????.
  free(delete_node->key);
  free(delete_node);
}
