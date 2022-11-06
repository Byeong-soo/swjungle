/*
 * adder.c - a minimal CGI program that adds two numbers together
 */
/* $begin adder */
#include "csapp.h"

int main(void) {
  char *buf, *p;
  char arg1[MAXLINE], arg2[MAXLINE], content[MAXLINE], temp[MAXLINE];
  int n1 =0, n2=0;

  /* Extract the two arguments */
  if((buf = getenv("QUERY_STRING")) != NULL){
    p = strchr(buf, '&');
    *p = '\0';
    strcpy(arg1, buf);
    strcpy(arg2, p+1);

    p = strchr(arg1,'=');
    *p = '\0';
    strcpy(arg1,p+1);

    p = strchr(arg2,'=');
    *p = '\0';
    strcpy(arg2,p+1);

    n1 = atoi(arg1);
    n2 = atoi(arg2);
  }
  /*  Make the response body  */
  sprintf(content, "QUERY_STRING = %s", buf);
  sprintf(content, "Welcome to add.com: ");
  sprintf(content, "%sThe Internet addition portal.\r\n<p>",content);
  sprintf(content, "%sThe answer is: %d + %d = %d\r\n<p>",content, n1, n2, n1 + n2);
  sprintf(content, "%sThanks for visiting! \r\n",content);

  printf("Connection: close\r\n");
  printf("Content-length: %d\r\n", (int)strlen(content));
  printf("Content-type: text/html\r\n\r\n");

  // sprintf(temp,"Connection: close\r\n");
  // sprintf(temp,"%sContent-length: %d\r\n",temp ,(int)strlen(content));
  // sprintf(temp,"%sContent-type: text/html\r\n",temp);
  // printf("%s", temp);


  /*  Generate the HTTP response  */
  printf("%s",content);



  fflush(stdout);
  
  exit(0);
}
/* $end adder */
