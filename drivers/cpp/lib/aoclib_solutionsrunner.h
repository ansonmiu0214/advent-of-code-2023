#pragma once

// stdlib
#include <concepts>
#include <format>
#include <functional>
#include <fstream>
#include <iostream>
#include <string>
#include <type_traits>
#include <vector>

namespace aoclib {

// template <typename T, typename U>
// concept Formatter = requires (T formatter, std::invoke_result_t<U, const std::vector<std::string>&> answer) {
//     { formatter(answer) -> std::template convertible_to<std::string> };
// };

                            // =====================
                            // class SolutionsRunner
                            // =====================

// template <
//     typename T,
//     typename U = std::function<
//         std::string(
//             std::invoke_result_t<T, const std::vector<std::string>&>
//         )
//     >
// >
// template <typename T, Formatter<T> U>
template <typename T, typename U>
class SolutionsRunner {
  private:  
    T& d_solveForPart1;
    T& d_solveForPart2;
    U& d_formatAnswer;

  public:
    // CREATORS
    SolutionsRunner(const T &solveForPart1,
                    const T &solveForPart2,
                    const U &formatter = std::to_string);

    // ACCESSORS
    int main(int argc, const char **argv) const;
};

                            // ---------------------
                            // class SolutionsRunner
                            // ---------------------

// CREATORS
// template <typename T, Formatter<T> U>
template <typename T, typename U>
SolutionsRunner<T, U>::SolutionsRunner(const T &solveForPart1,
                                       const T &solveForPart2,
                                       const U &formatter)
: d_solveForPart1(solveForPart1)
, d_solveForPart2(solveForPart2)
, d_formatAnswer(formatter)
{
}

// ACCESSORS
// template <typename T, Formatter<T> U>
template <typename T, typename U>
int SolutionsRunner<T, U>::main(int argc, const char **argv) const
{
    // Parse command line arguments.
    // TODO: find a library that actually does this?

    #define ASSERT(expr, message)           \
        if (!(expr)) {                      \
            std::cerr << (message) << "\n"    \
                      << "Terminating\n";   \
            return 1;                       \
        }

    ASSERT(argc == 7,
           std::format("Expected {} arguments, got {}", 7, argc));

    ASSERT(std::string(argv[1]) == "--day", "'--day' not supplied");
    std::string day(argv[2]);

    ASSERT(std::string(argv[3]) == "--part", "'--part' not supplied");
    std::string part(argv[4]);
    ASSERT(part == "part1" or part == "part2",
           std::format("For '--part', expected 'part(1|2)', got '{}'", part));

    ASSERT(std::string(argv[5]) == "--input-type", "'--input-type' not supplied");
    std::string inputType(argv[6]);

    auto dataFilePath = std::format("/data/{}/{}.in", day, inputType);
    std::ifstream file(dataFilePath);
    ASSERT(file.is_open(),
           std::format("Could not open data file: {}", dataFilePath));

    #undef ASSERT

    // Read the lines from the data file.

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    // Run the solution.

    auto answer = ([&]() {
        if (part == "part1") {
            return d_solveForPart1(lines);
        }
        else {
            return d_solveForPart2(lines);
        }
    })();

    // Print out the answer.

    std::cout << "Answer for "
              << day << " " << part
              << " using " << inputType << " input: "
              << d_formatAnswer(answer)
              << "\n";

    return 0;
}

} // closing namespace aoclib