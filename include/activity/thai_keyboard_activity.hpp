#pragma once

#include <functional>
#include <string>
#include <vector>

#include <borealis.hpp>

// An on-screen keyboard with the Thai Kedmanee layout and an English one, drawn by the app: the
// system keyboard has no Thai. Keys are picked with the stick or the D-pad and A, or by touch.
// B deletes, Y is a space, X is Shift, L switches ไทย/ABC, + searches and - closes.
class ThaiKeyboardActivity : public brls::Activity {
public:
    ThaiKeyboardActivity(std::function<void(const std::string&)> on_done,
                         const std::string& title,
                         const std::string& initial_text,
                         size_t max_characters);

    brls::View* createContentView() override;
    void onContentAvailable() override;

private:
    struct Key {
        brls::Box* box = nullptr;
        brls::Label* label = nullptr;
        float center = 0;  // in key units, from the middle of the keyboard
        int row = 0;
        int column = 0;
    };

    void buildKeys(int focus_row, int focus_column);
    void relabel();
    void linkNavigation();
    brls::Box* makeKey(const std::string& text, float units, std::function<void()> action, bool accent = false);

    void type(const std::string& text);
    void backspace();
    void space();
    void toggleShift();
    void toggleLanguage();
    void submit();
    void cancel();
    void refreshText();

    std::function<void(const std::string&)> onDone_;
    std::string title_;
    std::string text_;
    size_t maxCharacters_;
    bool thai_ = true;
    bool shift_ = false;
    bool closing_ = false;

    brls::Label* textLabel_ = nullptr;
    brls::Label* modeLabel_ = nullptr;
    brls::Box* keysBox_ = nullptr;
    brls::Label* shiftLabel_ = nullptr;
    brls::Label* languageLabel_ = nullptr;
    std::vector<std::vector<Key>> rows_;
};
