#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
double *f;
int fsize;
double go(int n,int m){
    if(n<=0){
        return 0;
    }
    if(n>=fsize)n=fsize;
    if(n<fsize &&f[n]!=-1){
        return f[n];
    }
    double s=0;
    for(int i=0;i<n;i++){
        s+=go(i-m/2,m)+go(n-(i+m/2),m)+1;
    }
    f[n]=s/n;
    return f[n];
}
double solve(double n,double m,int ratio){
    int N=n/(m/ratio);
    int M=ratio;
    f=new double[N];
    fsize=N;
    cout<<fsize<<endl;
    for(int i=0;i<fsize;i++)f[i]=-1;
    return go(N,M);
}
int main(){
    double ans=solve(1.0,0.01,100);
    cout<<ans<<endl;
    return 0;
}