#include<iostream>
#include<map>
using namespace std;

class node{
    public:
    int data;
    node* next;
    node(int data){
        this ->data =data;
        this ->next =NULL;
    }
    ~node() {
        int value=this->data;
        if(this->next != NULL){
            delete next;
            this->next=NULL;
        }
        cout<<" Memory is free for node with data "<<value<<endl;
    }
};
void insteratHead(node* &head,int d){
    node* temp=new node(d);
    temp->next=head;
    head=temp;
}
void IsertArTail(node* &tail,int d){
    node* temp=new node(d);
    tail->next=temp;
    tail = temp;
}
void print(node* &head){
    node* temp=head;
    while(temp!=NULL){
        cout<<temp->data<<" ";
        // cout<<temp->next<<endl;
        temp = temp->next;
    }
    cout<<endl;
}
void insertAtPosition(node* head,int position,int d){
    if(position==1){
        insteratHead(head,d);
        return;
    }
    // if (len==position-1){
    //     IsertArTail(tail,h);       we can do this to sortout 1st index change issue but we dont't know the size so we can not do this,
    // }
    node* temp=head;
    int cnt=1;
    while(cnt<position-1){
        temp=temp->next;
        cnt++;
    }
    node* nodeToInsert=new node(d);
    nodeToInsert->next=temp->next;
    temp->next=nodeToInsert;

}

int DeletNode(int position, node* & head){
    if(position ==1){
        node* temp=head;
        head=head->next;
        temp->next=NULL;
        delete temp;
    }
    else{
        node* curr =head;
        node* prev =NULL;

        int cnt=1;
        while(cnt<position){
            prev=curr;
            curr=curr->next;
            cnt++;
        }
        prev->next=curr->next;
        delete curr;
    }

}
int main(){
    node* node1= new node(10);
    // cout<< node1->data <<endl;
    // cout<< node1->next <<endl;

    node* head =node1;
    node* tail=node1;


    insteratHead(head,12);
    // print(head);
    IsertArTail(tail,9);
    // print(head);
    IsertArTail(tail,8);
    // print(head);
   
    
    insertAtPosition(head,4,22);
    print(head);

    IsertArTail(tail,7);
    print(head);
    insertAtPosition(head,1,0);
    print(head);

    DeletNode(1,head);
    print(head);
}