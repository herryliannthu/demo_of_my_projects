#include <stdio.h>
#include <stdlib.h>
typedef struct people{
    int status;
    struct people* pre;
    struct people* next;
} people;


int main()
{
    int n=1024768,m=591,remain,s=1;
    scanf ("%d %d",&n,&m);
    people *head,*curr,*tem,*tail;
    head = (people*)malloc(sizeof(people));
    curr = head;
    curr->status = 1;
    for (int i=2;i<=n;i++){
        curr->next = (people*)malloc(sizeof(people));
        curr->next->pre=curr;
        curr = curr->next;
        curr->status=i;
    }
    curr->next=head;
    head->pre=curr;
    curr=head;
    remain = n;
    while (remain > 1){
        if (s == 1){
            for (int i=1;i<m;i++){
            tem = curr;
            curr = curr->next;
        }
        curr->next->pre = tem;
        tem->next = curr->next;
        free(curr);
        curr = tem;
        remain--;
        s=-1;
        }
        else if (s==-1){
            for (int i=1;i<m;i++){
            tem = curr;
            curr = curr->pre;
        }
        curr->pre->next = tem;
        tem->pre = curr->pre;
        free(curr);
        curr = tem;
        remain--;
        s=1;

        }

    }
    printf("%d\n",curr->status);




}
