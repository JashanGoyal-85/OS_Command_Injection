
#include <cstdlib>   // system()
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: ./ping_vuln <host>\n";
        return 1;
    }

    std::string host = argv[1];

    std::string cmd = "ping -c 3 " + host;

    std::cout << "[VULN] Running: " << cmd << "\n\n";
    int ret = system(cmd.c_str());   // <-- injection point
    return ret;
}
