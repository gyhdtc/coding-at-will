#include <iostream>
#include <vector>
#include <list>
#include <iomanip>
using namespace std;
#define SideLength 10
#define random(x) (rand()%x)
class TcsGame {
    private:
        int score;
        int food;
        char move;

        vector<int> board;
        int n = SideLength * SideLength;
        
        int SnakeLength;
        vector<int> snake;
    public:
        TcsGame();
        void TcsShow();
        void TcsMove();
        void TcsJudge();
};
TcsGame::TcsGame(){
    // score
    score = 0;
    // board
    board.assign(n, 0);
    // snake
    SnakeLength = 2;
    snake.push_back(45);
    snake.push_back(55);
    board[45] = 1;
    board[55] = 1;
    // init food
    for (int i = 0, x = random(100-SnakeLength); i <= x;) {
        if (board[i] == 0) i++;
        if (i > x) {
            food = i-1;
            board[i-1] = 2;
        }
    }
}
void TcsGame::TcsShow(){
    for (int i = 0; i < SideLength; i++){
        for (int j = 0; j < SideLength; j++)
            cout << board[i * SideLength + j] << " ";
        cout << endl;
    }
    cout << "---------------------" << endl;
    cout << "| Food Location : " << setw(2) << food        << "|" << endl;
    cout << "|         Score : " << setw(2) << score       << "|" << endl;
    cout << "|   SnakeLength : " << setw(2) << SnakeLength << "|" << endl;
    cout << "---------------------" << endl;
}

int main(){
    TcsGame gyh;
    gyh.TcsShow();
    return 0;
}