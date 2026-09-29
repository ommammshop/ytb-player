# Writes resources/i18n/th/strings.json and adds the favorite-channel and Thai-option keys to
# the other languages. The Switch button glyphs are written as \ue0xx escapes:
# A= B= X= Y= L= R= -=
import collections
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "resources" / "i18n"
A, X, Y, L, R, MINUS = "", "", "", "", "", ""

HOWTO_TH = (
    "ช่องโปรด (ไม่ต้องเข้าสู่ระบบ)\n"
    f"1. เปิดหน้าช่อง: กด {Y} ที่คลิปเพื่อดูข้อมูล แล้วกด {X} \"ช่อง\"\n"
    f"2. กดปุ่ม \"☆ เพิ่มช่องโปรด\" ใต้ชื่อช่อง (หรือกด {X})\n"
    f"3. คลิปใหม่จากทุกช่องโปรดจะขึ้นที่แท็บนี้ กด {X} เพื่อรีเฟรช\n"
    "กดปุ่มเดิมอีกครั้งเพื่อเอาช่องออก"
)
HOWTO_EN = (
    "Favorite channels (no sign-in needed)\n"
    f"1. Open a channel: press {Y} on a video for its details, then {X} \"Channel\"\n"
    f"2. Press \"☆ Add to favorites\" under the channel's name (or {X})\n"
    f"3. New videos from all favorite channels show on this tab; {X} refreshes\n"
    "Press the same button again to remove a channel"
)

FAVORITES = {
    "th": {
        "title": "ช่องโปรด",
        "action": "ช่องโปรด",
        "add": "เพิ่มช่องโปรด",
        "remove": "อยู่ในช่องโปรด",
        "added": "เพิ่ม {} ในช่องโปรดแล้ว",
        "removed": "เอา {} ออกจากช่องโปรดแล้ว",
        "save_failed": "บันทึกช่องโปรดไม่ได้",
        "howto": HOWTO_TH,
    },
    "en-US": {
        "title": "Favorite channels",
        "action": "Favorite",
        "add": "Add to favorites",
        "remove": "In favorites",
        "added": "Added {} to favorite channels",
        "removed": "Removed {} from favorite channels",
        "save_failed": "Could not save favorite channels",
        "howto": HOWTO_EN,
    },
}

THAI_OPTION = {"th": "ภาษาไทย", "en-US": "Thai", "ko": "태국어", "tr": "Tayca"}

TH = {
    "app": {
        "title": "ยูทูปไทย",
        "home": "หน้าแรก",
        "search": "ค้นหา",
        "subscriptions": "ช่องที่ติดตาม",
        "library": "คลัง",
        "settings": "ตั้งค่า",
        "info_body": "ยูทูปไทย • เวอร์ชัน {}\nฉบับภาษาไทย อัปเดตและดูแลโดยร้าน Ommamm\n\nดู YouTube บน Switch พร้อมเมนูไทย คีย์บอร์ดไทย\nค้นหาช่อง และช่องโปรด\n\nพัฒนาต่อจาก YTB Player (muratgokce)\nและ Switch-NewPipe (mirusu400)\nGPLv3 ไม่มีการรับประกัน • github.com/ommammshop/ytb-player",
        "playback_failed": "เล่นไม่สำเร็จ: {}",
        "notifications": "การแจ้งเตือน",
    },
    "hints": {
        "ok": "ตกลง",
        "cancel": "ยกเลิก",
        "back": "กลับ",
        "exit": "ออก",
        "exit_hint": "จะออกจากแอปนี้",
        "open": "เปิด",
        "on": "เปิด",
        "off": "ปิด",
        "delete": "ลบ",
        "save": "บันทึก",
        "input": "กรุณาพิมพ์...",
        "submit": "ส่ง",
        "tabs": "แท็บ",
    },
    "common": {
        "close": "ปิด",
        "info": "ข้อมูล",
        "none": "ไม่มี",
        "refresh": "รีเฟรช",
        "service_init_failed": "เริ่มบริการไม่สำเร็จ: {}",
        "count_with_title": "{} • {} รายการ",
    },
    "home": {
        "preparing": "กำลังเตรียมหน้าแรก",
        "no_kiosk": "ไม่มีหมวดให้แสดง",
        "load_failed": "โหลดหน้าแรกไม่ได้",
    },
    "search": {
        "action": "ค้นหา",
        "ime_title": "พิมพ์คำค้นหา",
        "ime_subtitle": "วิดีโอหรือช่อง",
        "prompt": "กด X เพื่อค้นหา",
        "placeholder": "ค้นหาใน YouTube",
        "no_results": "ไม่พบผลลัพธ์สำหรับ \"{}\"",
        "results_count": "\"{}\" • {} รายการ",
        "history_remove": "ลบคำนี้",
        "history_clear": "ล้างประวัติ",
        "history_clear_confirm": "ล้างประวัติการค้นหาทั้งหมดใช่ไหม?",
        "history_cleared": "ล้างประวัติการค้นหาแล้ว",
    },
    "subscriptions": {
        "filter": {
            "all": "ทั้งหมด",
            "today": "วันนี้",
            "videos": "วิดีโอ",
            "live": "ไลฟ์",
            "shorts": "Shorts",
            "empty": "ไม่มีวิดีโอที่ตรงกับตัวกรองนี้",
        },
        "session_action": "เซสชัน",
        "session_load_failed": "โหลดเซสชันไม่สำเร็จ",
        "session_load_failed_body": f"ลบไฟล์เซสชันที่บันทึกไว้แล้วนำเข้าใหม่ หรือกด {MINUS} เพื่อใส่คุกกี้ใหม่",
        "feed_load_failed": "โหลดฟีดช่องที่ติดตามไม่ได้",
        "feed_load_failed_body": f"มีเซสชันบันทึกไว้แล้ว แต่ YouTube ไม่ส่งฟีดกลับมา\nลองนำเข้าไฟล์เข้าสู่ระบบใหม่ด้วย {MINUS} หรือใช้คุกกี้จากบัญชีอื่น",
        "current_source": "แหล่งที่ใช้อยู่:\n{}",
        "session_prefix": "เซสชัน: {}",
        "controls": f"{A} เล่น • {Y} ข้อมูล • {X} รีเฟรช • {L}{R} ตัวกรอง • {MINUS} เซสชัน",
        "signed_out_title": "ต้องเข้าสู่ระบบ",
        "signed_out_body": f"เข้าสู่ระบบด้วยบัญชี YouTube เพื่อดูช่องที่ติดตาม: กด {MINUS} แล้วเลือก \"ส่งผ่าน Wi-Fi\" จากนั้นบนคอมพิวเตอร์หรือมือถือที่ต่อ Wi-Fi เดียวกัน ให้ส่งคุกกี้ YouTube จากหน้าเว็บที่แสดงขึ้นมา\n\nหรือวางไฟล์คุกกี้ไว้ที่นี่แล้วเลือก \"โหลดจากไฟล์\":\n{{}}",
        "session_dialog": {
            "saved": "มีเซสชันเข้าสู่ระบบบันทึกไว้แล้ว\n\nแหล่งของเซสชัน: {}",
            "signed_out": "ยังไม่มีเซสชันเข้าสู่ระบบ\n\nเข้าสู่ระบบจากคอมพิวเตอร์ด้วย \"ส่งผ่าน Wi-Fi\" หรือวางไฟล์คุกกี้ไว้ที่นี่:\n{}",
            "wifi": "ส่งผ่าน Wi-Fi",
            "load_file": "โหลดจากไฟล์",
            "logout": "ออกจากระบบ",
            "load_file_done": "นำเข้าไฟล์เข้าสู่ระบบแล้ว",
            "load_file_failed": "นำเข้าไฟล์เข้าสู่ระบบไม่สำเร็จ",
            "logout_done": "ลบเซสชันเข้าสู่ระบบแล้ว",
            "logout_failed": "ออกจากระบบไม่สำเร็จ",
        },
    },
    "library": {
        "clear_action": "ล้าง",
        "clear_history_confirm": "ล้างประวัติการดูทั้งหมดใช่ไหม?",
        "clear_favorites_confirm": "ลบรายการโปรดทั้งหมดใช่ไหม?",
        "favorites": "รายการโปรด",
        "history": "ประวัติ",
        "favorites_empty": f"ยังไม่มีรายการโปรด\n{L} และ {R} สลับระหว่าง ประวัติ, รายการโปรด, ดูภายหลัง และวิดีโอที่ชอบ",
        "history_empty": f"วิดีโอที่คุณเล่นจะแสดงที่นี่\n{L} และ {R} สลับระหว่าง ประวัติ, รายการโปรด, ดูภายหลัง และวิดีโอที่ชอบ",
        "clear_failed": "ล้างคลังไม่สำเร็จ",
        "favorites_cleared": "ล้างรายการโปรดแล้ว",
        "history_cleared": "ล้างประวัติแล้ว",
        "watch_later": "ดูภายหลัง",
        "liked": "วิดีโอที่ชอบ",
        "loading": "กำลังโหลดจากบัญชี YouTube...",
        "login_required": "รายการนี้มาจากบัญชี YouTube ต้องเข้าสู่ระบบก่อน (ตั้งค่า > เซสชันเข้าสู่ระบบ)",
        "account_failed": "โหลดรายการไม่ได้",
        "account_empty": "รายการนี้ว่างเปล่า",
        "cannot_clear_account": "ล้างรายการของ YouTube จากที่นี่ไม่ได้",
        "playlists": "เพลย์ลิสต์",
    },
    "settings": {
        "reset_action": "ค่าเริ่มต้น",
        "reset_failed": "รีเซ็ตการตั้งค่าไม่สำเร็จ",
        "reset_done": "คืนค่าเริ่มต้นแล้ว",
        "language": {
            "title": "ภาษา",
            "save_failed": "บันทึกภาษาไม่สำเร็จ",
            "saved": "บันทึกภาษาแล้ว เปิดแอปใหม่เพื่อให้ใช้ทุกหน้า",
            "options": {
                "auto": "ตามระบบ",
                "korean": "ภาษาเกาหลี",
                "english": "ภาษาอังกฤษ",
                "turkish": "ภาษาตุรกี",
                "thai": "ภาษาไทย",
            },
        },
        "playback_quality": {
            "title": "คุณภาพวิดีโอ",
            "save_failed": "บันทึกคุณภาพวิดีโอไม่สำเร็จ",
            "saved": "บันทึกคุณภาพวิดีโอแล้ว",
            "options": {
                "best": "ดีที่สุด (ต่อทีวี 1080p / มือถือ 720p)",
                "hd_1080": "1080p",
                "hd_720": "720p",
                "low_320": "320p",
            },
        },
        "startup_tab": {
            "title": "แท็บเริ่มต้น",
            "save_failed": "บันทึกแท็บเริ่มต้นไม่สำเร็จ",
            "saved": "แท็บเริ่มต้นจะเปลี่ยนเมื่อเปิดแอปครั้งถัดไป",
        },
        "home_kiosk": {
            "title": "หมวดเริ่มต้นของหน้าแรก",
            "save_failed": "บันทึกหมวดหน้าแรกไม่สำเร็จ",
            "saved": "มีผลเมื่อรีเฟรชหน้าแรกครั้งถัดไป",
            "options": {
                "recommended": "แนะนำ",
                "live": "ไลฟ์",
                "music": "เพลง",
                "gaming": "เกม",
                "shorts": "Shorts",
            },
        },
        "hide_shorts": {
            "title": "ซ่อนวิดีโอสั้น",
            "save_failed": "บันทึกการตั้งค่าวิดีโอสั้นไม่สำเร็จ",
            "enabled": "จะซ่อนวิดีโอสั้น",
            "disabled": "จะแสดงวิดีโอสั้นอีกครั้ง",
        },
        "hardware_decoding": {
            "title": "ถอดรหัสด้วยฮาร์ดแวร์",
            "save_failed": "บันทึกการตั้งค่าการถอดรหัสไม่สำเร็จ",
            "enabled": "วิดีโอจะใช้ตัวถอดรหัสฮาร์ดแวร์",
            "disabled": "วิดีโอจะถอดรหัสด้วยซอฟต์แวร์",
        },
        "session": {
            "title": "เซสชันเข้าสู่ระบบ",
            "load_failed": "โหลดเซสชันไม่สำเร็จ",
            "saved": "บันทึกแล้ว",
            "signed_out": "ยังไม่ได้เข้าสู่ระบบ",
            "dialog": {
                "load_failed": "โหลดเซสชันไม่สำเร็จ\n\n{}",
                "signed_out": f"ไม่มีเซสชันเข้าสู่ระบบที่บันทึกไว้\n\nเปิดแท็บ ช่องที่ติดตาม แล้วกด {MINUS} เพื่อนำเข้าคุกกี้",
                "saved": "มีเซสชันเข้าสู่ระบบบันทึกไว้\n\nชื่อที่แสดง: {}\nไฟล์เซสชัน: {}",
                "source": "แหล่ง: {}",
            },
        },
        "account": {
            "title": "บัญชี YouTube",
            "default": "ช่องของเซสชัน",
            "loading": "กำลังดึงบัญชีจาก YouTube...",
            "failed": "ดึงรายชื่อบัญชีไม่ได้",
            "login_required": f"เข้าสู่ระบบก่อน (ช่องที่ติดตาม > {MINUS})",
            "chosen": "บัญชี YouTube: {} (กด X เพื่อรีเฟรชรายการ)",
            "picker_title": "ใช้งานในนามช่องไหน?",
        },
        "storage": {
            "title": "ตำแหน่งไฟล์",
            "detail": "ไฟล์ตั้งค่า / เซสชัน / คลัง",
            "dialog": {
                "body": "ไฟล์ตั้งค่า:\n{}\n\nเซสชันเข้าสู่ระบบ:\n{}\n\nนำเข้าคุกกี้:\n{}\n\nคลัง:\n{}",
            },
        },
        "autoplay_next": {
            "title": "เล่นอัตโนมัติ",
            "save_failed": "บันทึกการตั้งค่าเล่นอัตโนมัติไม่สำเร็จ",
            "enabled": "เล่นวิดีโอถัดไปเมื่อจบ",
            "disabled": "หยุดรอเมื่อวิดีโอจบ",
        },
        "skip_sponsors": {
            "title": "ข้ามช่วงสปอนเซอร์",
            "save_failed": "บันทึกการตั้งค่าสปอนเซอร์ไม่สำเร็จ",
            "enabled": "จะข้ามช่วงสปอนเซอร์ (SponsorBlock)",
            "disabled": "จะเล่นช่วงสปอนเซอร์ตามปกติ",
        },
        "subtitles": {
            "title": "แสดงคำบรรยาย",
            "save_failed": "บันทึกการตั้งค่าคำบรรยายไม่สำเร็จ",
            "enabled": "จะแสดงคำบรรยาย (กด + ในเครื่องเล่นเพื่อเลือกภาษา)",
            "disabled": "ปิดคำบรรยาย",
        },
        "categories": {
            "general": "ทั่วไป",
            "video": "วิดีโอและคำบรรยาย",
            "account": "บัญชี",
            "storage": "พื้นที่จัดเก็บ",
        },
        "reset_confirm": "คืนการตั้งค่าทั้งหมดเป็นค่าเริ่มต้นใช่ไหม?",
    },
    "detail": {
        "play_action": "เล่น",
        "channel_action": "ช่อง",
        "related_action": "ที่เกี่ยวข้อง",
        "more_action": "เพิ่มเติม",
        "favorite_action": "รายการโปรด",
        "unfavorite_action": "เอาออกจากรายการโปรด",
        "default_title": "รายละเอียดวิดีโอ",
        "no_description": "ยังไม่มีคำอธิบาย",
        "status_play": "A เล่น",
        "status_channel": " • X ช่อง",
        "status_related": " • Y ที่เกี่ยวข้อง",
        "playback_url_failed": "สร้างลิงก์สำหรับเล่นไม่ได้",
        "channel_load_failed": "โหลดวิดีโอของช่องไม่ได้",
        "related_load_failed": "โหลดวิดีโอที่เกี่ยวข้องไม่ได้",
        "extras_title": "คำสั่งเพิ่มเติม",
        "playlist_action": "เพลย์ลิสต์",
        "comments_action": "ความคิดเห็น",
        "playlist_load_failed": "โหลดเพลย์ลิสต์ไม่ได้",
        "comments_load_failed": "โหลดความคิดเห็นไม่ได้",
        "favorite_save_failed": "บันทึกรายการโปรดไม่สำเร็จ",
        "favorite_added": "เพิ่มในรายการโปรดแล้ว",
        "favorite_removed": "เอาออกจากรายการโปรดแล้ว",
        "loading": "กำลังโหลดคำอธิบาย...",
        "comments_none": "ไม่มีความคิดเห็น หรือปิดความคิดเห็นไว้",
    },
    "feed": {
        "subtitle": "A เล่น • Y รายละเอียด • B กลับ",
        "loading": "กำลังโหลด...",
        "tab_empty": "แท็บนี้ไม่มีอะไรให้แสดง",
        "tab_failed": "โหลดแท็บนี้ไม่ได้",
        "play_all": "เล่นทั้งหมด",
    },
    "comments": {
        "title": "ความคิดเห็น",
        "subtitle": "B กลับ",
        "verified": "ยืนยันแล้ว",
        "unknown_author": "ผู้ใช้ไม่ทราบชื่อ",
        "likes": "ถูกใจ {}",
        "replies": "ตอบกลับ {}",
        "loading": "กำลังโหลดความคิดเห็น...",
        "count_more": "{} ความคิดเห็น • เลื่อนลงเพื่อโหลดเพิ่ม",
        "count_loading": "{} ความคิดเห็น • กำลังโหลดเพิ่ม...",
        "count_failed": "{} ความคิดเห็น • โหลดเพิ่มไม่ได้ เลื่อนลงเพื่อลองใหม่",
        "count_all": "โหลดครบทั้ง {} ความคิดเห็นแล้ว",
        "count_limit": "แสดง {} ความคิดเห็น (สูงสุด)",
        "replies_title": "การตอบกลับ",
        "reply_count_more": "{} การตอบกลับ • เลื่อนลงเพื่อโหลดเพิ่ม",
        "reply_count_loading": "{} การตอบกลับ • กำลังโหลดเพิ่ม...",
        "reply_count_failed": "{} การตอบกลับ • โหลดเพิ่มไม่ได้ เลื่อนลงเพื่อลองใหม่",
        "reply_count_all": "โหลดครบทั้ง {} การตอบกลับแล้ว",
        "reply_count_limit": "แสดง {} การตอบกลับ (สูงสุด)",
    },
    "player": {
        "status": {
            "paused": "หยุดชั่วคราว",
            "live": "สด",
            "playing": "กำลังเล่น",
            "volume": "เสียง",
        },
        "osd_controls": "A หยุด  B กลับ  X ข้อมูล  Y ความเร็ว  ปุ่มทิศ 10 วิ  L/R 60 วิ  - เริ่มใหม่  + ตั้งค่า",
        "osd": {
            "auto": "แถบข้อมูล: ซ่อนเอง",
            "locked": "แถบข้อมูล: แสดงตลอด",
            "audio_download_failed": "ดาวน์โหลดเสียงไม่สำเร็จ",
            "audio_attach_failed": "เพิ่มเสียงไม่ได้",
            "playback_ready": "พร้อมเล่น",
            "volume": "เสียง {}",
            "seek": "เลื่อนไป {} / {}",
            "seek_unavailable": "เลื่อนตรงนี้ไม่ได้",
            "seek_live": "เลื่อนในไลฟ์สดไม่ได้",
            "seek_buffer_limit": "โหลดไว้ถึง {}",
            "speed": "ความเร็ว {}x",
            "resumed": "ดูต่อที่ {}   เริ่มใหม่: (-)",
            "sponsor_skipped": "ข้ามช่วงสปอนเซอร์ ({} วิ)",
        },
        "loading": {
            "preparing_playback": "กำลังเตรียมวิดีโอ",
            "opening_media_stream": "กำลังเปิดสตรีม",
            "waiting_for_mpv_load": "กำลังโหลดเครื่องเล่น",
            "opening_direct_media": "กำลังเปิดสื่อ",
            "non_youtube_url": "ไม่ใช่ลิงก์ YouTube",
            "direct_stream_ready": "สตรีมพร้อมแล้ว",
            "opening_live_stream": "กำลังเปิดไลฟ์สด",
            "direct_playback": "เล่นโดยตรง",
            "direct_dash_playback": "เล่น DASH โดยตรง",
            "downloading_video_data": "กำลังดาวน์โหลดวิดีโอ",
            "received": "ได้รับแล้ว",
            "starting_transfer": "กำลังเริ่มรับข้อมูล",
            "initial_buffer_ready": "ส่วนแรกพร้อมแล้ว",
            "download_complete": "ดาวน์โหลดเสร็จแล้ว",
            "attaching_audio_track": "กำลังเพิ่มเสียง",
            "stream_720_failed": "สตรีมหลักล้มเหลว",
            "fallback_safe_stream": "กำลังเปลี่ยนไปใช้สตรีมสำรอง",
            "playback_started": "เริ่มเล่นแล้ว",
            "video_frame_ready": "ภาพพร้อมแล้ว",
            "reading_stream_buffer": "กำลังอ่านสตรีม",
            "contacting_video_cdn": "กำลังติดต่อเซิร์ฟเวอร์วิดีโอ",
            "buffering_first_frame": "กำลังโหลดภาพแรก",
            "following_playlist_redirect": "กำลังตามลิงก์เพลย์ลิสต์",
            "resolving_youtube_stream": "กำลังดึงวิดีโอ",
            "contacting_player_api": "กำลังติดต่อ YouTube",
            "selecting_playable_format": "กำลังเลือกคุณภาพ",
            "requesting_hls_stream": "กำลังขอสตรีม HLS",
            "requesting_avc_stream": "กำลังขอสตรีม AVC",
            "requesting_progressive_stream": "กำลังขอสตรีมแบบ progressive",
            "requesting_ump_stream": "กำลังขอสตรีม UMP",
        },
        "autoplay": {
            "countdown": "วิดีโอถัดไปใน {} วิ",
            "hint": "A เล่นเลย   B ยกเลิก",
            "cancelled": "ยกเลิกการเล่นอัตโนมัติ",
        },
        "subtitles": {
            "loading": "กำลังโหลดคำบรรยาย...",
            "off": "ปิดคำบรรยาย",
            "none": "วิดีโอนี้ไม่มีคำบรรยาย",
            "on": "เปิดคำบรรยาย: {}",
            "other": "ไม่มีคำบรรยายภาษาที่เลือก แสดง {1} แทน",
            "menu_title": "คำบรรยาย",
            "menu_off": "ปิด",
            "auto_track": "{} (สร้างอัตโนมัติ)",
        },
        "menu": {
            "hint": "A เลือก   B ปิด",
        },
        "chapters": {
            "menu_title": "ตอน",
            "current": "ตอน {}/{}: {}",
            "hint": "ZR ตอน",
            "none": "วิดีโอนี้ไม่มีการแบ่งตอน",
            "loading": "กำลังโหลดตอน...",
            "jumped": "ตอน: {}",
        },
        "shorts": {
            "hint": "▲▼ Short ก่อนหน้า / ถัดไป",
            "next_loading": "กำลังโหลด Short ถัดไป",
        },
        "settings": {
            "title": "ตั้งค่า",
            "quality": "คุณภาพ",
            "speed": "ความเร็วการเล่น",
            "normal": "ปกติ",
            "loop": "เล่นวนซ้ำ",
            "on": "เปิด",
            "off": "ปิด",
            "subtitles": "คำบรรยาย",
            "chapters": "ตอน",
            "none": "ไม่มี",
            "quality_changed": "คุณภาพ: {} (เล่นต่อจากเดิม)",
            "loop_on": "เปิดเล่นวนซ้ำ",
            "loop_off": "ปิดเล่นวนซ้ำ",
            "button": "ตั้งค่า",
            "auto": "อัตโนมัติ",
        },
    },
    "stream": {
        "live_badge": "สด",
        "playlist_view": "ดูเพลย์ลิสต์ทั้งหมด",
        "views": "ครั้ง",
    },
    "notifications": {
        "loading": "กำลังโหลดการแจ้งเตือน...",
        "login_required": "เข้าสู่ระบบด้วยบัญชี YouTube เพื่อดูการแจ้งเตือน (ตั้งค่า > บัญชี > เซสชันเข้าสู่ระบบ)",
        "empty": "ไม่มีการแจ้งเตือน",
    },
    "wifi_login": {
        "title": "เข้าสู่ระบบผ่าน Wi-Fi",
        "instructions": "บนคอมพิวเตอร์หรือมือถือที่ต่อ Wi-Fi เดียวกัน เปิดเบราว์เซอร์แล้วไปที่:",
        "explain": "ส่งคุกกี้ YouTube จากหน้านั้น แล้ว Switch จะเข้าสู่ระบบเอง คุกกี้จะถูกส่งมาที่ Switch เครื่องนี้เท่านั้น",
        "waiting": "กำลังรอ…",
        "done": "เข้าสู่ระบบแล้ว",
        "no_network": "ไม่มีเครือข่าย ต่อ Switch กับ Wi-Fi แล้วลองใหม่",
        "failed": "เข้าสู่ระบบไม่สำเร็จ",
        "closed": "หน้าจอบน Switch ถูกปิดไปแล้ว",
        "page": {
            "title": "YTB Player: เข้าสู่ระบบ",
            "heading": "เข้าสู่ระบบ YouTube บน Switch ของคุณ",
            "intro": "บนคอมพิวเตอร์เครื่องนี้:",
            "step1": "ติดตั้งส่วนขยายสำหรับส่งออกคุกกี้ \"Get cookies.txt LOCALLY\" เป็นโอเพนซอร์สและไม่ส่งคุกกี้ไปที่ไหน%links%",
            "step2": "เปิดหน้าต่างส่วนตัว (ไม่ระบุตัวตน) แล้วเข้าสู่ระบบ YouTube ใน Chrome และ Edge ต้องเปิด \"Allow in Incognito\" ในรายละเอียดของส่วนขยายก่อน",
            "step3": "ในแท็บเดิม ไปที่ `youtube.com/robots.txt`",
            "step4": "คลิกไอคอนส่วนขยาย ดาวน์โหลด `cookies.txt` ด้วยปุ่ม \"Export\" แล้วปิดหน้าต่างส่วนตัว ตราบใดที่ปิดไว้ YouTube จะไม่ต่ออายุคุกกี้ชุดนี้ Switch จึงอยู่ในระบบได้นาน",
            "step5": "ลากไฟล์ที่ดาวน์โหลดมาวางด้านล่างหรือกดเลือก แล้วกด ส่ง",
            "choose": "เลือก cookies.txt",
            "drop": "หรือลากไฟล์มาวางที่นี่",
            "chosen": "ที่เลือก:",
            "paste": "วางข้อความแทน",
            "placeholder": "คุกกี้: cookies.txt, ส่วนหัว Cookie หรือ JSON",
            "send": "ส่ง",
            "saved_title": "เข้าสู่ระบบแล้ว",
            "saved": "กลับไปที่ Switch ได้เลย และปิดหน้านี้ได้",
            "empty": "ไม่มีอะไรให้ส่ง: เลือก cookies.txt หรือวางข้อความ",
            "privacy": "หน้านี้มาจาก Switch ของคุณโดยตรง ไม่ได้มาจากอินเทอร์เน็ต คุกกี้จะถูกส่งไปที่ Switch เท่านั้น",
        },
    },
    "thai_kb": {
        "delete": "ลบ",
        "space": "เว้นวรรค",
        "language": "ไทย/ABC",
        "done": "ค้นหา",
    },
    "favorite_channels": FAVORITES["th"],
}


def keys(node, prefix=""):
    out = set()
    for key, value in node.items():
        path = f"{prefix}/{key}"
        out |= keys(value, path) if isinstance(value, dict) else {path}
    return out


def main():
    # signed_out_body is an f-string with a literal "{}" placeholder
    TH["subscriptions"]["signed_out_body"] = TH["subscriptions"]["signed_out_body"].replace("{{}}", "{}")

    english = json.loads((ROOT / "en-US" / "strings.json").read_text(encoding="utf-8"),
                         object_pairs_hook=collections.OrderedDict)
    english.setdefault("favorite_channels", FAVORITES["en-US"])
    english["settings"]["language"]["options"]["thai"] = THAI_OPTION["en-US"]
    (ROOT / "en-US" / "strings.json").write_text(
        json.dumps(english, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    for lang in ("ko", "tr"):
        path = ROOT / lang / "strings.json"
        data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
        data.setdefault("favorite_channels", FAVORITES["en-US"])
        data["settings"]["language"]["options"]["thai"] = THAI_OPTION[lang]
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    missing = keys(english) - keys(TH)
    extra = keys(TH) - keys(english)
    if missing or extra:
        raise SystemExit(f"key mismatch: missing={sorted(missing)} extra={sorted(extra)}")

    (ROOT / "th").mkdir(exist_ok=True)
    (ROOT / "th" / "strings.json").write_text(
        json.dumps(TH, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("th keys:", len(keys(TH)))


if __name__ == "__main__":
    main()
