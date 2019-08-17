#include <iostream>
#include <vector>
#include <list>
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
        list<int> snake;
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
    // food
    for (int i = 0, x = random(100-SnakeLength); i <= x; (board[i] == 0 ? i++ : i)) {
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
    cout << "_" << endl;
    cout << "|Food Location : " << food        << "|" << endl;
    cout << "|        Score : " << score       << "|" << endl;
    cout << "|  SnakeLength : " << SnakeLength << "|" << endl;
    cout << "-------------------" << endl;
}
int main(){
    TcsGame gyh;
    gyh.TcsShow();
    return 0;
}