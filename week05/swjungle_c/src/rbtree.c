#include "rbtree.h"
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

rbtree *new_rbtree(void) {
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));

  node_t * nilNode = (node_t *)calloc(1,sizeof(node_t));
  nilNode->color = RBTREE_BLACK;
  nilNode->left = NULL;
  nilNode->right = NULL;
  nilNode->parent = NULL;
  nilNode->key = -1;

  p->nil = nilNode;
  p->root = nilNode;
  return p;
}

node_t* turnNode(node_t * me,rbtree * t){
    node_t * parents = me->parent;
    node_t * grandParents = parents->parent;

    // 왼쪽 회전 직선
    if(me->key>=parents->key && parents->key>=grandParents->key){

      if (grandParents != t->root)
      {
        if(grandParents->parent->key <= grandParents->key){
          grandParents->parent->right = parents;
        }else{
          grandParents->parent->left = parents;
        }
         parents->parent = grandParents->parent;
         
      } else{
         t->root = parents;
         parents->parent = t->nil;
      }

      grandParents->parent = parents;

      grandParents->right = parents->left;
      parents->left = grandParents;
      

      grandParents->color = RBTREE_RED;
      parents->color = RBTREE_BLACK;
      
      return parents;
    }
    // 왼쪽 회전 꺽임
    else if(me->key<parents->key && parents->key>=grandParents->key){

      if (grandParents != t->root)
      {
        if(grandParents->parent->key <= me->key){
          grandParents->parent->right = me;
        }else{
          grandParents->parent->left = me;
        }
          me->parent = grandParents->parent;
      }else{
         t->root = me;
         me->parent = t->nil;
      }

      grandParents->right = me->left;
      parents->left = me->right;
      grandParents->parent = me;
      parents->parent = me;

      me->right->parent = parents;
      me->right = parents;
      
      me->left->parent = grandParents;
      me->left = grandParents;
      

      grandParents->color = RBTREE_RED;
      me->color = RBTREE_BLACK;
      return me;
    }
    // 오른쪽 회전 직선
    else if(me->key<parents->key && parents->key<grandParents->key){

      if (grandParents != t->root)
      {
        if(grandParents->parent->key < grandParents->key){
          grandParents->parent->right = parents;
        }else{
          grandParents->parent->left = parents;
        }
         parents->parent = grandParents->parent;
      }else{
        t->root = parents;
        parents->parent = t->nil;
      }
      
      grandParents->left = parents->right;
      parents->right = grandParents;
      grandParents->parent = parents;

      grandParents->color = RBTREE_RED;
      parents->color = RBTREE_BLACK;

      return parents;
    }
    // 오른쪽 회전 꺽임
    else if(me->key>=parents->key && parents->key<grandParents->key){

      if (grandParents != t->root)
      {
        if(grandParents->parent->key < me->key){
          grandParents->parent->right = me;
        }else{
          grandParents->parent->left = me;
        }
        me->parent = grandParents->parent;
      }else{
         t->root = me;
         me->parent = t->nil;
      }

      grandParents->left = me->right;
      parents->right = me->left;
      grandParents->parent = me;
      parents->parent = me;

      me->right->parent = grandParents;
      me->right = grandParents;

      me->left->parent = parents;
      me->left = parents;
      
      me->color = RBTREE_BLACK;
      grandParents->color = RBTREE_RED;

      return me;
    }
  return NULL;
}


node_t *new_node_t(rbtree *t,const key_t key){
  node_t *newNode = (node_t*)calloc(1,sizeof(node_t));
  newNode->key = key;
  newNode->color = RBTREE_RED;
  newNode->parent = t->nil;
  newNode->right = t->nil;
  newNode->left = t->nil;
  return newNode;
}

node_t *rbtree_insert(rbtree *t, const key_t key) {

  node_t *newNode = new_node_t(t,key);
  node_t * nilNode = t->nil;

  if(t->root == nilNode){
    // root 노드가 없을 경우 검정으로 칠해줌
    newNode->color = RBTREE_BLACK;
    t->root = newNode;
  }else{
    // root 노드가 존재
    node_t *cur = t->root;
    node_t *parentNode;
    // cur이 nil에 도착하면 종료
    while (cur != t->nil)
    {
      parentNode = cur;
      if(cur->key <= key){
        cur = cur->right;
      }else{
        cur = cur->left;
      }
    }
    // 새로운 노드에 입력
    newNode->parent = parentNode;
    // 부모노드의 오른쪽 왼쪽 확인
    if(parentNode->key <= newNode->key){
      parentNode->right = newNode;
    }else{
      parentNode->left = newNode;
    }

    // 부모노드 검정인지 확인
    // 빨강(0) 이면 확인 검정(1)이면 그냥 리턴
    cur = newNode;
    while (cur->parent->color == RBTREE_RED)
    {
      parentNode = cur->parent;
      // 삼촌을 확인
      node_t * uncleNode = parentNode->parent->right;
      if(parentNode->key == parentNode->parent->right->key){
        uncleNode = parentNode->parent->left;
      }

       // 삼촌 색이 빨강임 - 검정으로 변환
      if(uncleNode->color == RBTREE_RED){
        uncleNode->color = RBTREE_BLACK;
        parentNode->color = RBTREE_BLACK;

         // 부모의 부모(조부모)가 루트인 경우는 그냥 리턴
        if(parentNode->parent == t->root){
          return t->root;
        }else{
        // 루트가 아닐경우 확인, 색깔 먼저 변경
          parentNode->parent->color = RBTREE_RED;
          //조부모의 부모가 빨강이면 다시 확인.
          cur = parentNode->parent;
        }
      }else{
        // 삼촌 색이 검정 or nill(색은 검정이므로) 회전!
        turnNode(cur,t);
      }
    }
  }
  return t->root;
}


node_t *rbtree_find(const rbtree *t, const key_t key) {

  node_t* cur = t->root;
  
  while (cur->parent != NULL)
  {
    if (cur->key > key)
    {
      cur = cur->left;
    }
    else if(cur->key < key)
    {
      cur = cur->right;
    }
    else{
       return cur;
    }
     
  }
  return NULL;
}

void delete_rbtree_traversal_postorder(node_t * root,node_t * nilNode){

  if (root == nilNode){
    return;
  }
  
  if (root->left != nilNode)
  {
    delete_rbtree_traversal_postorder(root->left,nilNode);
  }

   if (root->right != nilNode)
  {
    delete_rbtree_traversal_postorder(root->right,nilNode);
  }

  free(root);
  return;
}

void delete_rbtree(rbtree *t) {
  // TODO: reclaim the tree nodes's memory
  delete_rbtree_traversal_postorder(t->root,t->nil);
  free(t->nil);
  free(t);
}


node_t *rbtree_min(const rbtree *t) {
  // TODO: implement find
  return t->root;
}

node_t *rbtree_max(const rbtree *t) {
  // TODO: implement find
  return t->root;
}

int rbtree_erase(rbtree *t, node_t *p) {
  // TODO: implement erase
  return 0;
}

int search_rbtree_traversal_inorder(node_t * root,node_t * nilNode, key_t *arr,int index){

  if (root == nilNode){
    return index;
  }
  
  if (root->left != nilNode)
  {
    index =search_rbtree_traversal_inorder(root->left,nilNode, arr,index);
  }

  arr[index] = root->key;
  printf("key =%d   color = %d  parent=%d  left= %d right = %d \n", root->key,root->color,root->parent->key,root->left->key,root->right->key);
  index+=1;

   if (root->right != nilNode)
  {
    index=search_rbtree_traversal_inorder(root->right,nilNode,arr , index);
  }
  return index;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
  // TODO: implement to_array
  search_rbtree_traversal_inorder(t->root,t->nil,arr,0);

  return 0;
}


