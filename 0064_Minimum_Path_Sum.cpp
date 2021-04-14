#include<bits/stdc++.h>
using namespace std;
int f(vector<vector<int>>& grid){
    if(grid.size()<1) return 0;
    for(int i=0;i<grid.size();i++){
        for(int j=0;j<grid[i].size();j++){
            if(i==0 && j==0) continue;
            if(i==0) grid[i][j]=grid[i][j-1]+grid[i][j];
            else if(j==0) grid[i][j]=grid[i-1][j]+grid[i][j];
            else grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j];
        }
    }
    int ans=grid[grid.size()-1][grid[0].size()-1];
    return ans;
}
int main(){
    vector<vector<int>> grid={{1,3,1},{1,5,1},{4,2,1}};
    printf("%d\n",f(grid));
    return 0;
}