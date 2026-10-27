#include <cerrno>
#include <cstring>
#include <iostream>
#include <regex>
#include <string>
#include <unistd.h>   // execvp()

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: ./ping_safe <host>\n";
        return 1;
    }

    std::string host = argv[1];

    std::regex allow_list("^[a-zA-Z0-9.\\-]+$");
    if (!std::regex_match(host, allow_list)) {
        std::cerr << "[BLOCKED] Invalid input: \"" << host << "\"\n"
                  << "Only letters, digits, '.', and '-' are accepted.\n"
                  << "No command was executed.\n";
        return 1;
    }

    std::cout << "[SAFE] Running: ping -c 3 " << host << "\n\n";

    char* args[] = {
        (char*)"ping",
        (char*)"-c",
        (char*)"3",
        (char*)host.c_str(),
        nullptr          // execvp requires null-terminated array
    };

    execvp("ping", args);   // <-- replaces process; no shell

    // execvp only returns on error
    std::cerr << "[ERROR] execvp failed: " << strerror(errno) << "\n";
    return 1;
}
