#pragma once

#include <mutex>
#include <string>
#include <vector>

#include "newpipe/models.hpp"

namespace newpipe {

std::string default_library_store_path();

class LibraryStore {
public:
    static LibraryStore& instance();

    bool load(std::string* error_message = nullptr);
    bool reload(std::string* error_message = nullptr);

    std::vector<StreamItem> history_items();
    std::vector<StreamItem> favorite_items();
    bool is_favorite(const std::string& url);

    bool add_history(const StreamItem& item, std::string* error_message = nullptr);
    bool toggle_favorite(
        const StreamItem& item,
        bool* is_now_favorite = nullptr,
        std::string* error_message = nullptr);
    bool clear_history(std::string* error_message = nullptr);
    bool clear_favorites(std::string* error_message = nullptr);

    // Recent search queries, newest first, shown under the search box as on YouTube.
    std::vector<std::string> search_history();
    bool add_search(const std::string& query, std::string* error_message = nullptr);

    // Favorite channels, kept on the SD card without a Google account; the Subscriptions tab
    // shows their newest videos while signed out. An item carries the channel's id, name, link
    // and picture.
    std::vector<StreamItem> favorite_channels();
    bool is_favorite_channel(const std::string& channel_id);
    bool toggle_favorite_channel(
        const StreamItem& channel,
        bool* is_now_favorite = nullptr,
        std::string* error_message = nullptr);

private:
    LibraryStore() = default;

    bool ensure_loaded(std::string* error_message);
    bool persist(std::string* error_message);

    mutable std::mutex mutex_;
    bool loaded_ = false;
    std::vector<StreamItem> history_items_;
    std::vector<StreamItem> favorite_items_;
    std::vector<std::string> searches_;
    std::vector<StreamItem> favorite_channels_;
};

}  // namespace newpipe
