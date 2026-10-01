#pragma once

#include <borealis.hpp>
#include <string>
#include <utility>

namespace newpipe {

inline std::string locale_from_setting(const std::string& language) {
    if (language == "ko") {
        return brls::LOCALE_Ko;
    }
    if (language == "en-US") {
        return brls::LOCALE_EN_US;
    }
    if (language == "tr") {
        return "tr";  // borealis has no constant for it; resources/i18n/tr is loaded by name
    }
    // "th", and "auto" too: the console has no Thai to follow, so the Thai edition's default is
    // Thai (settings saved before the change say "auto"). No borealis constant: loaded by name.
    return "th";
}

template <typename... Args>
inline std::string tr(const std::string& key, Args&&... args) {
    return brls::getStr(key, std::forward<Args>(args)...);
}

}  // namespace newpipe
