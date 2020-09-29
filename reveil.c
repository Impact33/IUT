#include <stdio.h>

int main(){

    _Bool frigo = 1;
    const int c = 420;
    int hib, e, hb, r;
    int hc = 0;
    int hc2 = 0;
    printf("le frigo est plein ?(oui:1 / non:0) :");
    scanf("%d",&frigo);
    printf("debut des cours   (heure) :");
    scanf("%d",&hc);
    printf("                           h\n");
    printf("debut des cours (minutes) :");
    scanf("%d",&hc2);
    hc = hc*60;
    hib = hc2+hc-c-12;
    e = (hib/11)*11;
    hb = c + e;
    if(frigo == 1){
        r = hb-25;
    }
    else{
        r = hb-30;
    }
    printf("heure_reveil:%d:%d", r/60, r-((r/60)*60));

    return 0;       
}