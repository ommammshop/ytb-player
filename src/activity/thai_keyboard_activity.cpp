#include "activity/thai_keyboard_activity.hpp"

#include <algorithm>
#include <cmath>

#include "newpipe/i18n.hpp"
#include "newpipe/log.hpp"

namespace {
// One key is this wide with its gap; the special keys are counted in these units.
constexpr float kUnit = 84.0f;
constexpr float kGap = 8.0f;
constexpr float kKeyHeight = 56.0f;

using Layout = std::vector<std::vector<const char*>>;

// Kedmanee, as printed on Thai keyboards: the rows of 1, Q, A and Z.
const Layout kThai = {
    {"ๅ", "/", "-", "ภ", "ถ", "ุ", "ึ", "ค", "ต", "จ", "ข", "ช"},
    {"ๆ", "ไ", "ำ", "พ", "ะ", "ั", "ี", "ร", "น", "ย", "บ", "ล", "ฃ"},
    {"ฟ", "ห", "ก", "ด", "เ", "้", "่", "า", "ส", "ว", "ง"},
    {"ผ", "ป", "แ", "อ", "ิ", "ื", "ท", "ม", "ใ", "ฝ"},
};
const Layout kThaiShift = {
    {"+", "๑", "๒", "๓", "๔", "ู", "฿", "๕", "๖", "๗", "๘", "๙"},
    {"๐", "\"", "ฎ", "ฑ", "ธ", "ํ", "๊", "ณ", "ฯ", "ญ", "ฐ", ",", "ฅ"},
    {"ฤ", "ฆ", "ฏ", "โ", "ฌ", "็", "๋", "ษ", "ศ", "ซ", "."},
    {"(", ")", "ฉ", "ฮ", "ฺ", "์", "?", "ฒ", "ฬ", "ฦ"},
};
const Layout kEnglish = {
    {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"},
    {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"},
    {"a", "s", "d", "f", "g", "h", "j", "k", "l", "'"},
    {"z", "x", "c", "v", "b", "n", "m", ",", ".", "-"},
};
const Layout kEnglishShift = {
    {"!", "@", "#", "$", "%", "&", "*", "(", ")", "_"},
    {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"},
    {"A", "S", "D", "F", "G", "H", "J", "K", "L", "\""},
    {"Z", "X", "C", "V", "B", "N", "M", ";", ":", "?"},
};

const Layout& layout_for(bool thai, bool shift) {
    if (thai) {
        return shift ? kThaiShift : kThai;
    }
    return shift ? kEnglishShift : kEnglish;
}

uint32_t first_codepoint(const std::string& text) {
    const auto* s = reinterpret_cast<const unsigned char*>(text.c_str());
    if (s[0] < 0x80) return s[0];
    if ((s[0] & 0xE0) == 0xC0) return ((s[0] & 0x1F) << 6) | (s[1] & 0x3F);
    if ((s[0] & 0xF0) == 0xE0) return ((s[0] & 0x0F) << 12) | ((s[1] & 0x3F) << 6) | (s[2] & 0x3F);
    return 0;
}

// Vowels and tone marks written above or below a consonant have no width of their own.
bool is_thai_mark(uint32_t c) {
    return c == 0x0E31 || (c >= 0x0E34 && c <= 0x0E3A) || (c >= 0x0E47 && c <= 0x0E4E);
}

// Alone on a key such a mark would hang off its left edge: it sits on a no-break space instead.
std::string key_caption(const char* text) {
    return is_thai_mark(first_codepoint(text)) ? std::string(" ") + text : std::string(text);
}

size_t count_characters(const std::string& text) {
    size_t count = 0;
    for (unsigned char c : text) {
        if ((c & 0xC0) != 0x80) count++;
    }
    return count;
}
}  // namespace

ThaiKeyboardActivity::ThaiKeyboardActivity(std::function<void(const std::string&)> on_done,
                                           const std::string& title,
                                           const std::string& initial_text,
                                           size_t max_characters)
    : onDone_(std::move(on_done)), title_(title), text_(initial_text), maxCharacters_(max_characters) {
}

brls::View* ThaiKeyboardActivity::createContentView() {
    auto* root = new brls::Box(brls::Axis::COLUMN);
    root->setWidthPercentage(100);
    root->setGrow(1.0f);
    root->setAlignItems(brls::AlignItems::CENTER);
    root->setJustifyContent(brls::JustifyContent::CENTER);
    root->setBackgroundColor(nvgRGB(0x0F, 0x0F, 0x0F));

    // Something focusable outside the keys: focus waits here while the keys are rebuilt.
    auto* holder = new brls::Box();
    holder->setId("thai_kb/holder");
    holder->setWidth(1);
    holder->setHeight(1);
    holder->setFocusable(true);
    holder->setHideHighlight(true);
    root->addView(holder);

    auto* title = new brls::Label();
    title->setText(this->title_);
    title->setFontSize(22);
    title->setTextColor(nvgRGB(0xAA, 0xAA, 0xAA));
    title->setMarginBottom(12);
    root->addView(title);

    auto* field = new brls::Box(brls::Axis::ROW);
    field->setWidth(13 * kUnit - kGap);
    field->setHeight(64);
    field->setCornerRadius(32);
    field->setBackgroundColor(nvgRGB(0x27, 0x27, 0x27));
    field->setAlignItems(brls::AlignItems::CENTER);
    field->setPadding(0, 28, 0, 28);
    field->setMarginBottom(10);
    this->textLabel_ = new brls::Label();
    this->textLabel_->setFontSize(28);
    this->textLabel_->setSingleLine(true);
    this->textLabel_->setGrow(1.0f);
    this->textLabel_->setTextColor(nvgRGB(0xF1, 0xF1, 0xF1));
    field->addView(this->textLabel_);
    root->addView(field);

    this->modeLabel_ = new brls::Label();
    this->modeLabel_->setFontSize(16);
    this->modeLabel_->setTextColor(nvgRGB(0x3E, 0xA6, 0xFF));
    this->modeLabel_->setMarginBottom(14);
    root->addView(this->modeLabel_);

    this->keysBox_ = new brls::Box(brls::Axis::COLUMN);
    this->keysBox_->setAlignItems(brls::AlignItems::CENTER);
    root->addView(this->keysBox_);

    auto* frame = new brls::AppletFrame(root);
    frame->setHeaderVisibility(brls::Visibility::GONE);
    return frame;
}

void ThaiKeyboardActivity::onContentAvailable() {
    this->registerAction(newpipe::tr("thai_kb/delete"), brls::BUTTON_B, [this](brls::View*) {
        this->backspace();
        return true;
    }, false, true);
    this->registerAction(newpipe::tr("thai_kb/space"), brls::BUTTON_Y, [this](brls::View*) {
        this->space();
        return true;
    }, false, true);
    this->registerAction("Shift", brls::BUTTON_X, [this](brls::View*) {
        this->toggleShift();
        return true;
    });
    this->registerAction(newpipe::tr("thai_kb/language"), brls::BUTTON_LB, [this](brls::View*) {
        this->toggleLanguage();
        return true;
    });
    this->registerAction(newpipe::tr("thai_kb/done"), brls::BUTTON_START, [this](brls::View*) {
        this->submit();
        return true;
    });
    this->registerAction(newpipe::tr("hints/cancel"), brls::BUTTON_BACK, [this](brls::View*) {
        this->cancel();
        return true;
    });

    this->refreshText();
    this->buildKeys(1, 0);
}

brls::Box* ThaiKeyboardActivity::makeKey(const std::string& text, float units, std::function<void()> action, bool accent) {
    auto* key = new brls::Box(brls::Axis::ROW);
    key->setWidth(units * kUnit - kGap);
    key->setHeight(kKeyHeight);
    key->setMargins(kGap / 2, kGap / 2, kGap / 2, kGap / 2);
    key->setCornerRadius(10);
    key->setHighlightCornerRadius(10);
    key->setFocusable(true);
    key->setJustifyContent(brls::JustifyContent::CENTER);
    key->setAlignItems(brls::AlignItems::CENTER);
    key->setBackgroundColor(accent ? nvgRGB(0x3E, 0xA6, 0xFF) : nvgRGB(0x3A, 0x3A, 0x3A));

    auto* label = new brls::Label();
    label->setFontSize(26);
    label->setSingleLine(true);
    label->setHorizontalAlign(brls::HorizontalAlign::CENTER);
    label->setTextColor(accent ? nvgRGB(0x0F, 0x0F, 0x0F) : nvgRGB(0xF1, 0xF1, 0xF1));
    label->setText(text);
    key->addView(label);

    key->registerClickAction([action](brls::View*) {
        action();
        return true;
    });
    key->addGestureRecognizer(new brls::TapGestureRecognizer(key));
    return key;
}

// The keys are made again when the language changes, since the rows are not as long.
void ThaiKeyboardActivity::buildKeys(int focus_row, int focus_column) {
    brls::Application::giveFocus(this->getView("thai_kb/holder"));
    this->keysBox_->clearViews();
    this->rows_.clear();

    const Layout& layout = layout_for(this->thai_, this->shift_);
    for (size_t r = 0; r < layout.size(); r++) {
        auto* rowBox = new brls::Box(brls::Axis::ROW);
        std::vector<Key> row;
        const float width = static_cast<float>(layout[r].size());
        for (size_t c = 0; c < layout[r].size(); c++) {
            Key key;
            key.row = static_cast<int>(r);
            key.column = static_cast<int>(c);
            key.center = static_cast<float>(c) + 0.5f - width / 2;
            key.box = this->makeKey(key_caption(layout[r][c]), 1.0f, [this, r, c]() {
                this->type(layout_for(this->thai_, this->shift_)[r][c]);
            });
            key.label = static_cast<brls::Label*>(key.box->getChildren()[0]);
            rowBox->addView(key.box);
            row.push_back(key);
        }
        this->keysBox_->addView(rowBox);
        this->rows_.push_back(row);
    }

    // The bottom row: language, Shift, space, delete and search, as on a phone.
    struct Special {
        std::string text;
        float units;
        std::function<void()> action;
        bool accent;
    };
    const std::vector<Special> specials = {
        {this->thai_ ? "ABC" : "ไทย", 2.0f, [this]() { this->toggleLanguage(); }, false},
        {"⇧ Shift", 2.0f, [this]() { this->toggleShift(); }, false},
        {newpipe::tr("thai_kb/space"), 4.5f, [this]() { this->space(); }, false},
        {"⌫", 2.0f, [this]() { this->backspace(); }, false},
        {newpipe::tr("thai_kb/done"), 2.5f, [this]() { this->submit(); }, true},
    };
    float total = 0;
    for (const auto& special : specials) total += special.units;
    auto* bottom = new brls::Box(brls::Axis::ROW);
    std::vector<Key> bottomRow;
    float left = -total / 2;
    for (size_t i = 0; i < specials.size(); i++) {
        Key key;
        key.row = static_cast<int>(layout.size());
        key.column = static_cast<int>(i);
        key.center = left + specials[i].units / 2;
        left += specials[i].units;
        key.box = this->makeKey(specials[i].text, specials[i].units, specials[i].action, specials[i].accent);
        key.label = static_cast<brls::Label*>(key.box->getChildren()[0]);
        bottom->addView(key.box);
        bottomRow.push_back(key);
    }
    this->languageLabel_ = bottomRow[0].label;
    this->shiftLabel_ = bottomRow[1].label;
    this->keysBox_->addView(bottom);
    this->rows_.push_back(bottomRow);

    this->linkNavigation();
    this->relabel();

    focus_row = std::max(0, std::min(focus_row, static_cast<int>(this->rows_.size()) - 1));
    const auto& row = this->rows_[focus_row];
    focus_column = std::max(0, std::min(focus_column, static_cast<int>(row.size()) - 1));
    brls::Application::giveFocus(row[focus_column].box);
}

// Up and down go to the key most nearly above or below, as the rows are not as long.
void ThaiKeyboardActivity::linkNavigation() {
    auto nearest = [](const std::vector<Key>& row, float center) {
        const Key* best = &row.front();
        for (const auto& key : row) {
            if (std::fabs(key.center - center) < std::fabs(best->center - center)) best = &key;
        }
        return best->box;
    };
    for (size_t r = 0; r < this->rows_.size(); r++) {
        for (auto& key : this->rows_[r]) {
            if (r > 0) {
                key.box->setCustomNavigationRoute(brls::FocusDirection::UP, nearest(this->rows_[r - 1], key.center));
            }
            if (r + 1 < this->rows_.size()) {
                key.box->setCustomNavigationRoute(brls::FocusDirection::DOWN, nearest(this->rows_[r + 1], key.center));
            }
        }
    }
}

void ThaiKeyboardActivity::relabel() {
    const Layout& layout = layout_for(this->thai_, this->shift_);
    for (size_t r = 0; r < layout.size() && r < this->rows_.size(); r++) {
        for (size_t c = 0; c < layout[r].size() && c < this->rows_[r].size(); c++) {
            this->rows_[r][c].label->setText(key_caption(layout[r][c]));
        }
    }
    if (this->shiftLabel_) {
        this->shiftLabel_->setTextColor(this->shift_ ? nvgRGB(0x3E, 0xA6, 0xFF) : nvgRGB(0xF1, 0xF1, 0xF1));
    }
    if (this->modeLabel_) {
        std::string mode = this->thai_ ? "ไทย" : "English";
        if (this->shift_) mode += "  •  Shift";
        this->modeLabel_->setText(mode);
    }
}

void ThaiKeyboardActivity::type(const std::string& text) {
    if (count_characters(this->text_) >= this->maxCharacters_) {
        return;
    }
    this->text_ += text;
    // Shift holds for one key, like a phone's.
    if (this->shift_) {
        this->shift_ = false;
        this->relabel();
    }
    this->refreshText();
}

void ThaiKeyboardActivity::backspace() {
    if (this->text_.empty()) {
        return;
    }
    size_t end = this->text_.size() - 1;
    while (end > 0 && (static_cast<unsigned char>(this->text_[end]) & 0xC0) == 0x80) {
        end--;
    }
    this->text_.erase(end);
    this->refreshText();
}

void ThaiKeyboardActivity::space() {
    if (!this->text_.empty() && this->text_.back() != ' ') {
        this->type(" ");
    }
}

void ThaiKeyboardActivity::toggleShift() {
    this->shift_ = !this->shift_;
    this->relabel();
}

void ThaiKeyboardActivity::toggleLanguage() {
    int row = 0;
    int column = 0;
    for (const auto& keys : this->rows_) {
        for (const auto& key : keys) {
            if (key.box == brls::Application::getCurrentFocus()) {
                row = key.row;
                column = key.column;
            }
        }
    }
    this->thai_ = !this->thai_;
    this->shift_ = false;
    this->buildKeys(row, column);
}

void ThaiKeyboardActivity::refreshText() {
    if (this->textLabel_) {
        this->textLabel_->setText(this->text_ + "|");
    }
}

void ThaiKeyboardActivity::submit() {
    if (this->closing_) {
        return;
    }
    this->closing_ = true;
    std::string text = this->text_;
    while (!text.empty() && text.back() == ' ') text.pop_back();
    auto done = this->onDone_;
    newpipe::logf("thai keyboard: submit chars=%zu", count_characters(text));
    brls::Application::popActivity(brls::TransitionAnimation::FADE, [done, text]() {
        if (done && !text.empty()) {
            done(text);
        }
    });
}

void ThaiKeyboardActivity::cancel() {
    if (this->closing_) {
        return;
    }
    this->closing_ = true;
    brls::Application::popActivity();
}
