// project
#include <aoclib_solutionsrunner.h>

// stdlib
#include <cctype>
#include <numeric>
#include <ranges>
#include <string>
#include <unordered_map>
#include <vector>

namespace {

const std::unordered_map<std::string, int> _SPELLING_TO_INT = {
    {"one", 1},
    {"two", 2},
    {"three", 3},
    {"four", 4},
    {"five", 5},
    {"six", 6},
    {"seven", 7},
    {"eight", 8},
    {"nine", 9}
};

struct ParseOptions {
    bool englishAware;
};

std::vector<int> parseDigits(std::string_view line, ParseOptions options)
{
    std::vector<int> digits;
    for (int idx = 0; idx < line.size(); ++idx) {
        if (std::isdigit(line[idx])) {
            digits.push_back(line[idx] - '0');
        }
        else if (options.englishAware) {
            for (const auto& [spelling, number] : _SPELLING_TO_INT) {
                if (line.substr(idx, spelling.size()) == spelling) {
                    digits.push_back(number);
                    break;
                }
            }
        }
    }

    return digits;
}

int parseCalibrationValue(std::string_view line, ParseOptions options)
{
    const auto& digits = parseDigits(line, options);
    return (digits.front() * 10) + digits.back();
}

int part1(const std::vector<std::string> &lines)
{
    auto parseCalibration = [](std::string_view line) {
        return parseCalibrationValue(line, {.englishAware = false});
    };

    auto calibrationValues = lines
                           | std::views::transform(parseCalibration);
    return std::accumulate(calibrationValues.begin(), calibrationValues.end(), 0);
}

int part2(const std::vector<std::string> &lines)
{
    auto parseCalibration = [](std::string_view line) {
        return parseCalibrationValue(line, {.englishAware = true});
    };

    auto calibrationValues = lines
                           | std::views::transform(parseCalibration);
    return std::accumulate(calibrationValues.begin(), calibrationValues.end(), 0);
}

std::string formatAnswer(int answer) {
    // NOTE: hope to move away from this once we have a fix
    // in 'aoclib_solutionsrunner'!

    return std::to_string(answer);
}

}   // closing unnamed namespace

int main(int argc, char const *argv[])
{
    return aoclib::SolutionsRunner{part1, part2, formatAnswer}.main(argc, argv);
}