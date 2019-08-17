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
        list<int> snake;
    public:
        TcsGame();
        void TcsShow() const;
        void TcsMove();
        bool TcsJudge();
        bool TcsJudgeOutRange(int, int);
};

TcsGame::TcsGame(){
    // score
    score = 0;
    // board
    board.assign(n, 0);
    // move
    move = '\0';
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
void TcsGame::TcsShow() const{
    for (int i = 0; i < SideLength; i++){
        for (int j = 0; j < SideLength; j++){
            int num = i * SideLength + j;
            if (num == snake.front())
                cout << "[I]";
            else 
                cout << " " << board[num] << " ";
        }
        cout << endl;
    }
    cout << "---------------------" << endl;
    cout << "| Food Location : " << setw(2) << food        << "|" << endl;
    cout << "|         Score : " << setw(2) << score       << "|" << endl;
    cout << "|   SnakeLength : " << setw(2) << SnakeLength << "|" << endl;
    cout << "---------------------" << endl;
}
void TcsGame::TcsMove(){
    while(move != 'w' && move != 'a' && move != 's' && move != 'd' && move != '/')
        cin >> move;
}
bool TcsGame::TcsJudge(){
    int new_snake_head_num;
    int new_snake_head_x;
    int new_snake_head_y;
    int snake_head_x = snake.front() / SideLength;
    int snake_head_y = snake.front() % SideLength;
    // calculate input_move 
    switch(move){
        case 'w':
            new_snake_head_x = snake_head_x - 1;
            new_snake_head_y = snake_head_y;
            break;
        case 'a':
            new_snake_head_x = snake_head_x;
            new_snake_head_y = snake_head_y - 1;
            break;
        case 's':
            new_snake_head_x = snake_head_x + 1;
            new_snake_head_y = snake_head_y;
            break;
        case 'd':
            new_snake_head_x = snake_head_x;
            new_snake_head_y = snake_head_y + 1;
            break;
        case '/':
            // end of the game
            return false;
        default :
            // other input char is illegitimate
            cout << "Wrong Input" << endl;
            return true;
    }
    // whether legitimate input_move range / wall
    if (TcsJudgeOutRange(new_snake_head_x, new_snake_head_y)) return false;
    // whether legitimate input_move body
    new_snake_head_num = new_snake_head_x * SideLength + new_snake_head_y;
    if (board[new_snake_head_num] == 1){
        // new head can't equal the second head
        if (new_snake_head_num == snake[1]){
            cout << "Can't come back" << endl;
            return true;
        }
        // you will die when the new head equal other num of body
        else{
            return false;
        }
    }
    // eat food ?
    snake.push_front(new_snake_head_num);
    if (board[new_snake_head_num] == 2){
        SnakeLength ++;
    }
    else{
        snake.pop_back();
    }
}
bool TcsGame::TcsJudgeOutRange(int x, int y){
    if (x < 0 && x >= SideLength && y < 0 && y >= SideLength) 
        return true;
    else
        return false;
}
int main(){
    TcsGame gyh;
    gyh.TcsShow();
    gyh.TcsMove();
    return 0;
}