#include <iostream>
#include <stack>
#include <string>
using namespace std;
string currentText = "";
stack<string> u;
stack<string> r;
void addText() {
    string newText;
    cout << "Enter text to add: ";
    cin.ignore();
    getline(cin, newText);
    u.push(currentText); 
    while (!r.empty()) r.pop(); 
    currentText += newText;
    cout << "Text added.\n";
}
void deleteText() {
    int n;
    cout << "Enter number of characters to delete: ";
    cin >> n;
    if (n <= currentText.length()) {
        u.push(currentText); // Save current text for undo
        while (!r.empty()) r.pop(); // Clear redo stack
        currentText.erase(currentText.length() - n);
        cout << "Deleted last " << n << " characters.\n";
    } else {
        cout << "Cannot delete more characters than current text length.\n";
    }
}
void undo() {
    if (!u.empty()) {
        r.push(currentText);           // Save current state to redo
        currentText = u.top();         // Restore previous state
        u.pop();
        cout << "Undo performed.\n";
    } else {
        cout << "Nothing to undo.\n";
    }
}
void redo() {
    if (!r.empty()) {
        u.push(currentText);           // Save current state to undo
        currentText = r.top();         // Restore next state
        r.pop();
        cout << "Redo performed.\n";
    } else {
        cout << "Nothing to redo.\n";
    }
}
void showText() {
    cout << "\nCurrent Text: " << currentText << "\n";
}
void showMenu() {
    cout << "\n--- Text Editor Menu ---\n";
    cout << "1. Add Text\n";
    cout << "2. Undo\n";
    cout << "3. Redo\n";
    cout << "4. Delete Text\n";
    cout << "5. Show Current Text\n";
    cout << "6. Exit\n";
}
int main() {
    int choice;
    while (true) {
        showMenu();
        cout << "Enter your choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1:
                addText();
                break;
            case 2:
                undo();
                break;
            case 3:
                redo();
                break;
            case 4:
                deleteText();
                break;
            case 5:
                cout << "Current Text: " << currentText << endl;
                break;
            case 6:
                cout << "Exiting the program...\n";
                return 0;
            default:
                cout << "Invalid choice, please try again.\n";
        }
    }
    return 0;
}
