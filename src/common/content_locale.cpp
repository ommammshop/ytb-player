#include "newpipe/content_locale.hpp"

#include <atomic>
#include <ctime>
#include <string>
#include <unordered_map>

#ifdef __SWITCH__
#include <switch.h>
#endif

namespace newpipe {
namespace {

// Written once on the UI thread, read by the loaders' threads.
std::atomic<int> g_language{static_cast<int>(ContentLanguage::english)};
std::atomic<int> g_utc_offset_minutes{0};

int device_utc_offset_minutes() {
#ifdef __SWITCH__
    u64 now = 0;
    TimeCalendarTime calendar{};
    TimeCalendarAdditionalInfo info{};
    if (R_SUCCEEDED(timeGetCurrentTime(TimeType_Default, &now))
        && R_SUCCEEDED(timeToCalendarTimeWithMyRule(now, &calendar, &info))) {
        return info.offset / 60;
    }
    return 0;
#else
    const std::time_t now = std::time(nullptr);
    std::tm utc = *std::gmtime(&now);
    utc.tm_isdst = -1;
    // UTC's fields read as local time: the offset is how far that lands from now.
    return static_cast<int>(std::difftime(now, std::mktime(&utc)) / 60);
#endif
}

}  // namespace

void set_content_language(const std::string& locale) {
    ContentLanguage language = ContentLanguage::english;
    if (locale.rfind("tr", 0) == 0) {
        language = ContentLanguage::turkish;
    } else if (locale.rfind("ko", 0) == 0) {
        language = ContentLanguage::korean;
    } else if (locale.rfind("th", 0) == 0) {
        language = ContentLanguage::thai;
    }
    g_language.store(static_cast<int>(language));
    g_utc_offset_minutes.store(device_utc_offset_minutes());
}

ContentLanguage content_language() {
    return static_cast<ContentLanguage>(g_language.load());
}

const char* content_hl() {
    switch (content_language()) {
        case ContentLanguage::turkish:
            return "tr";
        case ContentLanguage::korean:
            return "ko";
        case ContentLanguage::thai:
            return "th";
        default:
            return "en";
    }
}

const char* content_gl() {
    switch (content_language()) {
        case ContentLanguage::turkish:
            return "TR";
        case ContentLanguage::korean:
            return "KR";
        case ContentLanguage::thai:
            return "TH";
        default:
            return "US";
    }
}

const char* accept_language() {
    switch (content_language()) {
        case ContentLanguage::turkish:
            return "tr-TR,tr;q=0.9,en-US;q=0.8";
        case ContentLanguage::korean:
            return "ko-KR,ko;q=0.9,en-US;q=0.8";
        case ContentLanguage::thai:
            return "th-TH,th;q=0.9,en-US;q=0.8";
        default:
            return "en-US,en;q=0.9";
    }
}

std::string pref_cookie() {
    return std::string("PREF=hl=") + content_hl() + "&gl=" + content_gl();
}

int utc_offset_minutes() {
    return g_utc_offset_minutes.load();
}

namespace {

// The Thai for the texts the service writes itself, by their English.
const std::unordered_map<std::string, const char*>& thai_texts() {
    static const std::unordered_map<std::string, const char*> texts = {
        {"The login file is empty", "ไฟล์เข้าสู่ระบบว่างเปล่า"},
        {"No SAPISID in the cookies", "ไม่พบ SAPISID ในคุกกี้"},
        {"Could not read the saved session file", "อ่านไฟล์เซสชันที่บันทึกไว้ไม่ได้"},
        {"Not signed in", "ยังไม่ได้เข้าสู่ระบบ"},
        {"Could not read the cookies", "อ่านคุกกี้ไม่ได้"},
        {"Could not open the login file: ", "เปิดไฟล์เข้าสู่ระบบไม่ได้: "},
        {"Could not read the login file", "อ่านไฟล์เข้าสู่ระบบไม่ได้"},
        {"Could not delete the session file", "ลบไฟล์เซสชันไม่ได้"},
        {"Could not save the session file", "บันทึกไฟล์เซสชันไม่ได้"},
        {"Could not read the library file", "อ่านไฟล์คลังไม่ได้"},
        {"Could not save the library", "บันทึกคลังไม่ได้"},
        {"Could not read the settings file", "อ่านไฟล์การตั้งค่าไม่ได้"},
        {"Could not save the settings", "บันทึกการตั้งค่าไม่ได้"},
        {"just now", "เมื่อสักครู่"},
        {"Unsupported Home category", "ไม่รองรับหมวดหน้าแรกนี้"},
        {"Could not load the login session", "โหลดเซสชันเข้าสู่ระบบไม่ได้"},
        {"Sign in to see your subscriptions", "เข้าสู่ระบบเพื่อดูช่องที่ติดตาม"},
        {"The subscriptions request failed", "โหลดช่องที่ติดตามไม่สำเร็จ"},
        {"Could not read the subscriptions feed", "อ่านฟีดช่องที่ติดตามไม่ได้"},
        {"No videos in the subscriptions feed", "ไม่มีวิดีโอในฟีดช่องที่ติดตาม"},
        {"No video ID found", "ไม่พบรหัสวิดีโอ"},
        {"The video details request failed", "โหลดรายละเอียดวิดีโอไม่สำเร็จ"},
        {"Could not read the video details", "อ่านรายละเอียดวิดีโอไม่ได้"},
        {"Could not load the video details: ", "โหลดรายละเอียดวิดีโอไม่ได้: "},
        {"No channel ID found", "ไม่พบรหัสช่อง"},
        {"The channel request failed", "โหลดช่องไม่สำเร็จ"},
        {"No videos on this channel", "ช่องนี้ไม่มีวิดีโอ"},
        {"No playlist ID found", "ไม่พบรหัสเพลย์ลิสต์"},
        {"The playlist request failed", "โหลดเพลย์ลิสต์ไม่สำเร็จ"},
        {"Could not read the playlist", "อ่านเพลย์ลิสต์ไม่ได้"},
        {"No videos in this playlist", "เพลย์ลิสต์นี้ไม่มีวิดีโอ"},
        {"No comments address", "ไม่มีที่อยู่ความคิดเห็น"},
        {"The comments request failed", "โหลดความคิดเห็นไม่สำเร็จ"},
        {"No more comments found", "ไม่มีความคิดเห็นเพิ่มเติม"},
        {"Could not read the comments", "อ่านความคิดเห็นไม่ได้"},
        {"The YouTube search request failed", "ค้นหาใน YouTube ไม่สำเร็จ"},
        {"Could not read the YouTube search results", "อ่านผลการค้นหา YouTube ไม่ได้"},
        {"No YouTube search results", "ไม่พบผลการค้นหาใน YouTube"},
        {"No next page", "ไม่มีหน้าถัดไป"},
        {"The next page request failed", "โหลดหน้าถัดไปไม่สำเร็จ"},
        {"Could not read the next page", "อ่านหน้าถัดไปไม่ได้"},
        {"No related videos found", "ไม่พบวิดีโอที่เกี่ยวข้อง"},
        {"Could not load the channel tab", "โหลดแท็บของช่องไม่ได้"},
        {"Could not load the Shorts queue", "โหลดคิว Shorts ไม่ได้"},
        {"Could not load Shorts", "โหลด Shorts ไม่ได้"},
        {"The list request failed", "โหลดรายการไม่สำเร็จ"},
        {"Could not read the notifications", "อ่านการแจ้งเตือนไม่ได้"},
        {"This video is not in a playlist", "วิดีโอนี้ไม่ได้อยู่ในเพลย์ลิสต์"},
        {"Could not get the account list", "ดึงรายชื่อบัญชีไม่ได้"},
    };
    return texts;
}

}  // namespace

const char* localized(const char* turkish, const char* english) {
    switch (content_language()) {
        case ContentLanguage::turkish:
            return turkish;
        case ContentLanguage::thai: {
            const auto& texts = thai_texts();
            const auto found = texts.find(english);
            return found != texts.end() ? found->second : english;
        }
        default:
            return english;
    }
}

}  // namespace newpipe
