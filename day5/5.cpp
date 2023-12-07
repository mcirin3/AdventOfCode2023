#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

// Function to clean the line and return a tuple of three integers
std::tuple<int, int, int> cleanLine(const std::string& line) {
    std::istringstream iss(line);
    int x, y, z;
    iss >> x >> y >> z;
    return std::make_tuple(x, y, z);
}

int main() {
    std::string fileName = "day5in.txt";
    std::ifstream file(fileName);

    if (!file.is_open()) {
        std::cerr << "File " << fileName << " not found" << std::endl;
        return 1;
    }

    std::vector<int> seeds;
    std::vector<int> locations;

    // Read seeds
    std::string line;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        if (line.find("seeds") != std::string::npos) {
            int seed;
            while (ss >> seed) {
                seeds.push_back(seed);
            }
            break;
        }
    }

    // Traverse seeds
    for (int seedNum : seeds) {
        int nodeNum = seedNum;
        bool desFound = false;

        // Traverse graph
        while (std::getline(file, line)) {
            if (line.empty() || line.find("map") != std::string::npos || line.find("seeds") != std::string::npos) {
                desFound = false;
                continue;
            }
            if (desFound) {
                continue;
            }

            int desRanStr, srcRanStr, ranLen;
            std::tie(desRanStr, srcRanStr, ranLen) = cleanLine(line);

            // Check if nodeNum is in the interval
            if (nodeNum >= srcRanStr && nodeNum <= srcRanStr + ranLen - 1) {
                int diff = srcRanStr - desRanStr;
                std::cout << nodeNum << std::endl;
                nodeNum -= diff;
                std::cout << diff << std::endl;
                std::cout << desRanStr << std::endl;
                std::cout << srcRanStr << std::endl;
                std::cout << ranLen << std::endl;
                std::cout << nodeNum << std::endl;
                desFound = true;
            }
        }

        locations.push_back(nodeNum);
        file.clear();
        file.seekg(0, std::ios::beg);
    }

    // Output the locations
    for (int location : locations) {
        std::cout << location << " ";
    }

    // Find and output the minimum location
    int minLocation = *std::min_element(locations.begin(), locations.end());
    std::cout << "Minimum Location: " << minLocation << std::endl;

    return 0;
}

